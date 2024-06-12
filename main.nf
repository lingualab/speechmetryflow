#!/usr/bin/env nextflow

log.info "Input: $params.input"
root = file(params.input)

transcriptions = channel
    .fromPath("$root/*.json", maxDepth:1)
    .map{[it.getSimpleName(), it]}


process Extract_Variables {
    input:
    tuple val(pid), file(transcription)

    output:
    file "${pid}_metrics.json"

    script:
    """
    python /home/chris/dev/Text2Variable/src/main.py ${transcription} sm -o ${pid}_metrics.json
    """
}


process Combine_Jsons {
    publishDir './results', mode: 'link'

    input:
    file jsons

    output:
    file "population_metrics.csv"

    script:
    """
    lingualabpy_jsons2csv -c ID *.json population_metrics.csv
    """
}

workflow {
    transcriptions
    Extract_Variables(transcriptions)
    metrics = Extract_Variables.out.collect()
    Combine_Jsons(metrics)
}