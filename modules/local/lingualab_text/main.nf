process LINGUALAB_TEXT {
    tag "$meta.filename"

    input:
    tuple val(meta), path(text_file)

    output:
    tuple val(meta), path("*_metrics-speechmetryflow.json"), emit: text_metric_smf
    tuple val(meta), path("*_metrics-textdescriptives.json"), emit: text_metric_td
    path "versions.yml", emit: versions

    script:
    """
    smf_extract --lang ${meta.language} --task ${meta.task}  ${text_file}
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