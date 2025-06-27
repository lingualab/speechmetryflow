include { LINGUALAB_AUDIO as LINGUALAB_AUDIO_PROCESS } from '../../../modules/local/lingualab_audio/main'
include { merge_jsons as MERGE_AUDIO } from '../../../modules/local/merge_jsons/main'

params.population_dir = null
params.audio_output = "population_lingualab_audio.csv"

workflow LINGUALAB_AUDIO {
    take:
        ch_audio            // channel: [ val(meta), audio_file ]

    main:
        LINGUALAB_AUDIO_PROCESS(ch_audio)
        MERGE_AUDIO(
            LINGUALAB_AUDIO_PROCESS.out.audio_metric.collect { it[1] },
            params.population_dir,
            params.audio_output,
        )

    emit:
    MERGE_AUDIO.out
}