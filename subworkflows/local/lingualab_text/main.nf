include { LINGUALAB_TEXT as LINGUALAB_TEXT_PROCESS } from '../../../modules/local/lingualab_text/main'
include { merge_jsons as MERGE_TEXT } from '../../../modules/local/merge_jsons/main'

params.population_dir = null
params.audio_output = "population_lingualab_text.csv"

workflow LINGUALAB_TEXT {
    take:
        ch_text            // channel: [ val(meta), text_file ]

    main:
        LINGUALAB_TEXT_PROCESS(ch_text)
        MERGE_TEXT(
            LINGUALAB_TEXT_PROCESS.out.text_metric.collect { it[1] },
            params.population_dir,
            params.audio_output,
        )

    emit:
    MERGE_TEXT.out
}