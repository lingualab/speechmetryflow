#!/usr/bin/env nextflow

include { glob_files as glob_audiofiles } from './modules/utils'
include { glob_files as glob_textfiles } from './modules/utils'
include { merge_jsons as merge_audio } from './modules/utils'
include { merge_jsons as merge_text } from './modules/utils'


log.info "Input CSV: $params.input"
log.info "Audio folder: $params.audio_folder"
log.info "Text folder: $params.text_folder"


process Audio_Metrics {
    publishDir = "./results/Audio_Metrics"

    input:
    val args

    output:
    file "*.json"

    script:
    """
    lingualabpy_audio_metrics --sex ${args.sex} -p ${args.participant_id} ${args.file}
    """
}

process Uhmometer_Metrics {
    publishDir = "./results/Uhmometer_Metrics"

    input:
    val args
    val uhmometer

    output:
    file "*.csv"

    script:
    """
    praat --run ${PRAAT_SCRIPTS_DIR}/syllablenucleiv3.praat $(pwd)/ \
        ${uhmometer.preprocessing} \
        ${uhmometer.silence_threshold} \
        ${uhmometer.minimum_dip_near_peak} \
        ${uhmometer.minimum_pause_duration} \
        ${uhmometer.detect_filled_pauses} \
        ${uhmometer.language} \
        ${uhmometer.filled_pause_threshold} \
        "Praat Info window" \
        ${uhmometer.data_collection_type} \
        ${uhmometer.keep_objects} > metric.csv
    """
}

process Text_Metrics {
    publishDir = "./results/Text_metrics"

    input:
    val args

    output:
    file "*.json"

    script:
    """
    text2variable --pid ${args.participant_id} -d . -l ${args.language} ${args.file} lg
    """
}


workflow {
    participants_args = channel
        .fromPath(params.input)
        .splitCsv(header: true)

    audiofiles = glob_audiofiles(
        participants_args,
        params.audio_folder,
        params.audio_extension)
        .flatten()

    textfiles = glob_textfiles(
        participants_args,
        params.text_folder,
        params.text_extension)
        .flatten()

    audio_jsons = Audio_Metrics(audiofiles).collect()
    uhmometer_jsons = Uhmometer_Metrics(audiofiles, params.uhmometer).collect()
    text_jsons = Text_Metrics(textfiles).collect()

    merge_audio(audio_jsons, params.audio_output)
    merge_text(text_jsons, params.text_output)
}
