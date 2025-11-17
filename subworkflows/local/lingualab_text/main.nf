include { LINGUALAB_TEXT as LINGUALAB_TEXT_PROCESS } from '../../../modules/local/lingualab_text/main'
include { merge_jsons as MERGE_TEXT_SMF } from '../../../modules/local/merge_jsons/main'
include { merge_jsons as MERGE_TEXT_TD } from '../../../modules/local/merge_jsons/main'

params.population_dir = null
params.output_smf = "population_speechmetryflow_text.csv"
params.output_td = "population_textdescriptives_text.csv"

workflow LINGUALAB_TEXT {
    take:
        ch_text            // channel: [ val(meta), text_file ]

    main:
        LINGUALAB_TEXT_PROCESS(ch_text)
        MERGE_TEXT_SMF(
            LINGUALAB_TEXT_PROCESS.out.text_metric_smf.collect { it[1] },
            params.population_dir,
            params.output_smf,
        )
        MERGE_TEXT_TD(
            LINGUALAB_TEXT_PROCESS.out.text_metric_td.collect { it[1] },
            params.population_dir,
            params.output_td,
        )

    emit:
    MERGE_TEXT_SMF.out
    MERGE_TEXT_TD.out
}