include { UHMOMETER as UHMOMETER_EXE } from '../../../modules/local/uhmometer/main'
include { merge_csvs as MERGE_CSV } from '../../../modules/local/merge_csvs/main'

params.population_dir = null
params.output = "population_uhmometer_metrics.csv"

workflow UHMOMETER {
    take:
        ch_audio            // channel: [ val(meta), audio_file ]

    main:
        UHMOMETER_EXE(ch_audio)
        MERGE_CSV(
            UHMOMETER_EXE.out.audio_metric_uhmometer.collect { it[1] },
            params.population_dir,
            params.output,
        )

    emit:
    MERGE_CSV.out
}