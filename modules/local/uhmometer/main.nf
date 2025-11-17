process UHMOMETER {
    tag "$meta.filename"

    input:
    tuple val(meta), path(text_file)

    output:
    tuple val(meta), path("*.csv"), emit: audio_metric_uhmometer
    path "versions.yml", emit: versions

    script:
    """
    mkdir input fontconfig_cache
    export XDG_CACHE_HOME="fontconfig_cache"
    mv *.wav input/
    praat --run \${PRAAT_SCRIPTS_DIR}/syllablenucleiv3.praat \$(pwd)/input/ \
        ${params.uhmometer.preprocessing} \
        ${params.uhmometer.silence_threshold} \
        ${params.uhmometer.minimum_dip_near_peak} \
        ${params.uhmometer.minimum_pause_duration} \
        ${params.uhmometer.detect_filled_pauses} \
        ${params.uhmometer.language} \
        ${params.uhmometer.filled_pause_threshold} \
        "Praat Info window" \
        ${params.uhmometer.data_collection_type} \
        ${params.uhmometer.keep_objects} > ${text_file}.csv

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        praat: \$(praat --version)
    END_VERSIONS
    """

    stub:
    def prefix = "${text_file}.csv"

    """
    touch ${prefix}
    touch versions.yml
    """
}