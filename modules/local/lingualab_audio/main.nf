process LINGUALAB_AUDIO {
    tag "$meta.filename"

    input:
    tuple val(meta), path(audio_file)

    output:
    tuple val(meta), path("*.json"), emit: audio_metric
    path "versions.yml", emit: versions

    script:
    """
    lingualabpy_audio_metrics --sex ${meta.sex} -p ${meta.participant_id} ${audio_file}
    touch versions.yml
    """

    stub:
    def prefix = "${meta.filename.baseName}"

    """
    touch ${prefix}.json
    touch ${prefix}.txt
    touch versions.yml
    """
}