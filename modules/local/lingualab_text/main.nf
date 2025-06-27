process LINGUALAB_TEXT {
    tag "$meta.filename"

    input:
    tuple val(meta), path(text_file)

    output:
    tuple val(meta), path("*.json"), emit: text_metric
    path "versions.yml", emit: versions

    script:
    """
    text2variable --pid ${meta.participant_id} -d . -t ${meta.task} -l ${meta.language} ${text_file} lg
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