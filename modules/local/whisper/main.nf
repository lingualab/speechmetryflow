process WHISPER {
    tag "$meta.filename"
    // label 'process_medium'

    input:
    tuple val(meta), path(audio_file)

    output:
    tuple val(meta), path("*.txt"), emit: transcription
    tuple val(meta), path("*.json"), emit: metadata
    path "versions.yml", emit: versions

    script:
    """
    # Run Whisper transcription
    whisper "$audio_file" \\
        --model ${params.whisper_model} \\
        --language ${meta.language} \\
        --output_dir . \\
        --output_format all \\
        --model_dir ${params.whisper_model_dir}

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        whisper: \$(/app/.venv/bin/pip list | grep openai-whisper | tr -s ' ' | cut -d' ' -f2)
        model_dir: ${params.whisper_model_dir}
        model: ${params.whisper_model}
        language: ${meta.language}
    END_VERSIONS
    """

    stub:
    def prefix = "${meta.filename.baseName}"

    """
    touch ${prefix}.json
    touch ${prefix}.txt
    touch versions.yml
    """
}