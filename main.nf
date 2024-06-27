#!/usr/bin/env nextflow

include { glob_files as glob_audiofiles } from './modules/utils'
include { glob_files as glob_textfiles } from './modules/utils'
include { merge_jsons as merge_audio } from './modules/utils'
include { merge_jsons as merge_text } from './modules/utils'


log.info "Input CSV: $params.input"
log.info "Audio folder: $params.audio_folder"
log.info "Text folder: $params.text_folder"


process Audio_Metrics {
    publishDir = './results/Audio_Metrics'

    input:
    val args

    output:
    file "*.json"

    script:
    """
    lingualabpy_audio_metrics -p ${args.participant_id} ${args.file}
    """
}

process Text_Metrics {
    publishDir = './results/Text_metrics'

    input:
    val args

    output:
    file "*.json"

    script:
    """
    text2variable --pid ${args.participant_id} -d . -o ${args.participant_id}_text_metric.json -l ${args.language} ${args.file} lg
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

    Audio_Metrics(audiofiles)
    Text_Metrics(textfiles)

    audio_jsons = Audio_Metrics.out.collect()
    text_jsons = Text_Metrics.out.collect()

    merge_audio(audio_jsons, params.audio_output)
    merge_text(text_jsons, params.text_output)
}
