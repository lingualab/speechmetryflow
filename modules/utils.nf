#!/usr/bin/env nextflow


process glob_files {
    input:
    val args
    val folder
    val extension

    output:
    val outputs

    exec:
    pid = args.participant_id
    outputs = []
    files("${folder}/**/${pid}*${extension}").each { it ->
        out = args.clone()
        out.file = it
        outputs << out
    }
}


process merge_jsons {
    publishDir './results', mode: 'link'

    input:
    file jsons
    val output

    output:
    file "${output}"

    script:
    """
    lingualabpy_jsons2csv -c filename *.json ${output}
    """
}

