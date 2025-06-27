process UHMOMETER {

    input:
    path audio_files
    val meta

    output:
    path "*.csv", emit: uhmometer_metric
    // path "versions.yml", emit: versions

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
        ${params.uhmometer.keep_objects} > ${params.uhmometer.output}

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        praat: \$(praat --version)
    END_VERSIONS
    """

    stub:
    def prefix = "${params.uhmometer.output}"

    """
    touch ${prefix}
    touch versions.yml
    """
}