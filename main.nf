#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { WHISPER } from './modules/local/whisper/main'
include { LINGUALAB_AUDIO } from './modules/local/lingualab_audio/main'
include { LINGUALAB_TEXT } from './modules/local/lingualab_text/main'
include { UHMOMETER } from './modules/local/uhmometer/main'
include { merge_jsons as MERGE_AUDIO } from './modules/local/merge_jsons/main'
include { merge_jsons as MERGE_TEXT } from './modules/local/merge_jsons/main'

// Header info
def summary = [:]
summary['Pipeline Name']   = workflow.manifest.name
summary['Version']         = workflow.manifest.version
summary['Input']           = params.input
summary['Audio folder']    = params.audio_folder
summary['Text folder']     = params.text_folder
summary['Working dir']     = workflow.workDir
summary['Execution']       = workflow.commandLine

log.info """
===============================================================================
${summary.collect { key, value -> "${key.padRight(15)}: $value" }.join("\n")}
===============================================================================
"""

workflow get_data {
    main:
        // Input validation
        if (!params.input) {
            error "Input path not specified!"
        }

        // Read participants meta informations
        participants_meta = Channel
            .fromPath(params.input)
            .splitCsv(header: true)
            .map{ it -> tuple(it.participant_id, it)}
        
        // Glob text files
        text_folder = file(params.text_folder)
        text_channel = Channel.fromPath("$text_folder/**$params.text_extension")
            .map{ it -> tuple(it.name.split("_")[0], it)} // Extract participant_id from filename
            .combine(participants_meta, by: 0) // Keep only participants from participants_meta
            .map{ participant_id, filename, meta ->
                def new_meta = meta + [filename: filename.name]
                tuple(new_meta, filename)
            }

        // Glob audio files
        audio_folder = file(params.audio_folder)
        audio_channel = Channel.fromPath("$audio_folder/**$params.audio_extension")
            .map{ it -> tuple(it.name.split("_")[0], it)} // Extract participant_id from filename
            .combine(participants_meta, by: 0) // Keep only participants from participants_meta
            .map{ participant_id, filename, meta ->
                def new_meta = meta + [filename: filename.name]
                tuple(new_meta, filename)
            }

    emit:
        text     = text_channel     // channel: [ val(meta), text_file ]
        audio    = audio_channel    // channel: [ val(meta), audio_file ]
}

workflow {
    data = get_data()

    WHISPER(data.audio)
    LINGUALAB_AUDIO(data.audio)
    LINGUALAB_TEXT(data.text.mix(WHISPER.out.transcription))

    UHMOMETER(data.audio.collect { it[1] }, params.population_dir)

    MERGE_AUDIO(
        LINGUALAB_AUDIO.out.audio_metric.collect { it[1] },
        params.population_dir,
        params.audio_output,
    )
    MERGE_TEXT(
        LINGUALAB_TEXT.out.text_metric.collect { it[1] },
        params.population_dir,
        params.text_output,
    )
}

workflow.onComplete {
    log.info "Pipeline completed at: $workflow.complete"
    log.info "Execution status: ${ workflow.success ? 'OK' : 'failed' }"
    log.info "Execution duration: $workflow.duration"
} 