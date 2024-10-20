# speechmetryflow

## Running

`nextflow run lingualab/speechmetryflow -r 0.0.2 --input participant_ids.csv`

Replace the `-r` option with the release you want to use

## Files needed

### participant_ids.csv

This CSV file must contain at least 3 columns:

- participant_id is required for the pipeline to find your files. These files must begin by the participant_id. To specify the folder where your files are located, see nextflow.config.
- language: 2 choices, `en` or `fr`.
- sex: 2 choices, `male` or `female`.

Example:

| participant_id | language |   sex  |
|:--------------:|:--------:|:------:|
|   sub-PKM8767  |    en    |  male  |
|   sub-SBK4467  |    en    | female |

### nextflow.config

Example for elm server:

```
params {
    audio_folder = "/data/brambati/dataset/CCNA/derivatives/audio_extract"
    text_folder = "/data/brambati/dataset/CCNA/derivatives/cookie_txt"
}

process {
    container = "/data/brambati/local/containers/lingualab/speechmetryflow_0.0.2.sif"
}

apptainer {
    runOptions = "-B /data/brambati"
}

executor {
    cpus = 20
}
```

## output

The pipeline produces 3 csv files:

- `population_audio_metrics`: metrics compute with `lingualabpy_audio_metrics` from [lingualabpy](https://github.com/lingualab/lingualabpy)
- `population_uhmometer_metrics`: metrics compute with [uhm-o-meter](https://sites.google.com/view/uhm-o-meter/home)
- `population_text_metrics`: metrics compute with [Text2Variable](https://github.com/lingualab/Text2Variable)

[Metrics description](https://metayer-pierre-briac.notion.site/Extractions-des-variables-fd2a68ee01044a1d9b0874518e78dd86)
