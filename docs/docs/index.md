# speechmetryflow

Automated nextflow-based workflow designed to extract both audio and text metrics from speech tasks (like picture descriptions) at scale.

## Running

`nextflow run lingualab/speechmetryflow -r {last_release_or_tag} --input participant_ids.csv`

Replace the `-r` option with the release you want to use

## Files needed

### participant_ids.csv

This CSV file must contain at least 4 columns:

- participant_id is required for the pipeline to find your files. These files must begin by the participant_id. To specify the folder where your files are located, see nextflow.config.
- language: 2 choices, `en` or `fr`.
- sex: 2 choices, `male` or `female`.
- task: 2 choices, `cookie_theft` or `picnic`.

Example:

| participant_id | language |   sex  |     task     |
|:--------------:|:--------:|:------:|:------------:|
|   sub-PKM8767  |    en    |  male  | cookie_theft |
|   sub-SBK4467  |    en    | female |    picnic    |

### nextflow.config

Example for elm server:

```
params {
    audio_folder = "/data/brambati/dataset/CCNA/derivatives/audio_extract"
    text_folder = "/data/brambati/dataset/CCNA/derivatives/cookie_txt"
}
```

And then run:

`nextflow run lingualab/speechmetryflow -r {last_release_or_tag} -profile unf_elm --input participant_ids.csv`

## output

The pipeline produces csv files in `results/Statistics` directory:

- `population_lingualab_audio.csv`: metrics compute with `lingualabpy_lingualab_audio` from [lingualabpy](https://github.com/lingualab/lingualabpy)
- `population_uhmometer_metrics.csv`: metrics compute with [uhm-o-meter](https://sites.google.com/view/uhm-o-meter/home)
- `population_lingualab_text.csv`: metrics compute with [Text2Variable](https://github.com/lingualab/Text2Variable)
- `population_opensmile_metrics_{feature_set}.csv`: metrics compute with [opensmile](https://audeering.github.io/opensmile-python/)
