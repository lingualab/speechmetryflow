#!/usr/bin/env nextflow


process merge_csvs {

    input:
    path csv_files
    val meta
    val output

    output:
    path "${output}"

    script:
    """
    echo ${csv_files}
    head -n 1 ${csv_files[0]} > ${output}
    for csv_file in ${csv_files}
    do
        tail -n 1 \${csv_file} >> ${output}
    done
    """
}

