#!/usr/bin/env nextflow


process merge_jsons {

    input:
    path jsons
    val meta
    val output

    output:
    path "${output}"

    script:
    """
    lingualabpy_jsons2csv -c filename *.json ${output}
    """
}

