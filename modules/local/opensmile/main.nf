process OPENSMILE {

    input:
    path audio_files
    val meta
    val feature_set

    output:
    path "*.csv", emit: opensmile_metric
    path "versions.yml", emit: versions

    script:
    """
    #!/usr/bin/env python3

    import yaml
    import opensmile
    from pathlib import Path

    smile = opensmile.Smile(
        feature_set="$feature_set",
        feature_level="func",
    )

    data = smile.process_files(list(Path().glob("*.wav")))

    data.to_csv("${params.opensmile.output_base}${feature_set}.csv")

    versions = {
        "opensmile": opensmile.__version__
    }
    with open('versions.yml', 'w') as file_obj:
        yaml.dump(versions, file_obj)
    """

    stub:
    def prefix = "${params.opensmile.output_base}${feature_set}.csv"

    """
    touch ${prefix}
    touch versions.yml
    """
}