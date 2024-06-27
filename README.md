# speechmetryflow

## Running

`nextflow run lingualab/speechmetryflow -r 0.0.1 --input participant_ids.csv`

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

Example:

```
params {
    audio_folder = "<your folder with .wav files>"
    text_folder = "<your folder with .txt files>"
}

process {
    container = "<path to your apptainer file>"
}

apptainer {
    runOptions = "-B <path to bind to your container>"
}
```