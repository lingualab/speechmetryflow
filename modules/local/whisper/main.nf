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
    mkdir mplconfigdir
    export MPLCONFIGDIR="mplconfigdir"

    # Run Whisper transcription
    whisperx "$audio_file" \\
        --model ${params.whisper_model} \\
        --model_cache_only True \\
        --model_dir ${params.whisper_model_dir} \\
        --device cpu \\
        --compute_type int8 \\
        --language ${meta.language} \\
        --output_dir . \\
        --output_format txt

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        faster-whisper: \$(pip list | grep faster-whisper | tr -s ' ' | cut -d' ' -f2)
        whisperx: \$(pip list | grep whisperx | tr -s ' ' | cut -d' ' -f2)
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