# Getting started

## Files needed

### Your input structure

Your files should be organized in the following types of structure.

The input data may consist of audio, text, or a combination of both modalities. It is not required to provide all modalities for each participants. It is also possible to provide multiple audio or text files for one participant.

Each files should have a distinct name.

Two example of a good input:

```
/project/
|-- data/
|   |-- audio/
|   |   |-- sub-ABC123_task-naming01.wav
|   |   |-- sub-ABC456_task-naming03.wav
|   |-- text/
|   |   |-- sub-ABC123_task-speech.txt
|   |   |-- sub-ABC456_task-speech.txt
```

```
/project/
|-- data/
|   |-- audio/
|   |   |-- sub-ABC123/
|   |   |   |-- sub-ABC123_task-naming01.wav
|   |   |-- sub-ABC456/
|   |   |   |-- sub-ABC456_task-naming03.wav
|   |-- text/
|   |   |-- sub-ABC123/
|   |   |   |-- sub-ABC123_task-speech.txt
|   |   |-- sub-ABC456/
|   |   |   |-- sub-ABC456_task-speech.txt
|   |   |-- sub-ABC456_task-otherspeech.txt
```

The next example is a bad input because of filenames collision for the last two text files:

```
/project/
|-- data/
|   |-- audio/
|   |   |-- sub-ABC123/
|   |   |   |-- sub-ABC123_task-naming01.wav
|   |   |-- sub-ABC456/
|   |   |   |-- sub-ABC456_task-naming03.wav
|   |-- text/
|   |   |-- sub-ABC123/
|   |   |   |-- sub-ABC123_task-speech.txt
|   |   |-- sub-ABC456/
|   |   |   |-- sub-ABC456_task-speech.txt
|   |   |-- sub-ABC456_task-speech.txt
```

### participant_ids.csv

This CSV file must contain at least 4 columns:

- participant_id is required for the pipeline to find your audio and text files. **These filenames must begin by the participant_id**.
- language: 2 choices, `en` or `fr`.
- sex: 2 choices, `male` or `female`.
- task: 3 choices, `cookie`, `picnic` or nothing.

Example:

| participant_id | language |   sex  |     task     |
|:--------------:|:--------:|:------:|:------------:|
|   sub-ABC123   |    en    |  male  |    cookie    |
|   sub-ABC456   |    en    | female |    picnic    |

### nextflow.config

Here the content of your `nextflow.config` file:

```
apptainer.enabled = true
params {
    audio_folder = "/project/data/audio"
    text_folder = "/project/data/text"
    container_dir = "/your/folder/to/save/containers"
}
```

See `Installation` for the `container_dir` parameter.

If you are a member of the [UNF](https://unf-montreal.ca/), you only need to specify the `audio_folder` and `text_folder` parameters.

## Running

```
nextflow run lingualab/speechmetryflow -r {last_release_or_tag} --input participant_ids.csv
```

Replace the `-r` option with the release you want to use.

If you are a member of the [UNF](https://unf-montreal.ca/), do not forget to add `-profile unf_elm`.

## output

The pipeline produces csv files in the `results/Statistics` directory:

| | |
| - | - |
| `OPENSMILE/population_opensmile_metrics_{set}.csv` | metrics compute with [opensmile](audio/opensmile.md) |
| `LINGUALAB_AUDIO/population_lingualab_audio.csv` | metrics compute with [parselmouth](audio/parselmouth.md) |
| `UHMOMETER/population_uhmometer_metrics.csv` | metrics compute with [uhm-o-meter](audio/uhmometer.md) |
| `LINGUALAB_TEXT/population_textdescriptives_text.csv` | metrics compute with [TextDescriptives](https://hlasse.github.io/TextDescriptives/) |
| `LINGUALAB_TEXT/population_speechmetryflow_text.csv` | metrics compute within speechmetryflow, See `Text Features` section |