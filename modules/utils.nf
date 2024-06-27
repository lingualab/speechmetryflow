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
    allfiles = files("${folder}/**/${pid}*${extension}")
    if (allfiles.size() == 1) {
        out = args.clone()
        out.file = allfiles[0]
        outputs << out
    } else {
        allfiles.eachWithIndex { onefile, i ->
            out = args.clone()
            out.file = onefile
            run = onefile.getSimpleName().split("_").find { it.startsWith("run") }
            if (run) {
                out.participant_id += "_${run}"
            } else {
                out.participant_id += "_run-${i+1}"
            }
            outputs << out
        }
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
    lingualabpy_jsons2csv *.json ${output}
    """
}

