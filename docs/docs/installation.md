# Installation

If you are a member of the [UNF](https://unf-montreal.ca/), speechmetryflow is already installed on their server. Just do `module load nextflow` and add `-profile unf_elm` to the nextflow commands you encounter in the next pages.

## Building the containers

You first need to install [apptainer](https://apptainer.org/) on your system.

When it's done, you can execute the `build.sh` script from speechmetryflow specifying the folder where you want to save the containers.

```
git clone https://github.com/lingualab/speechmetryflow.git
cd speechmetryflow/containers
chmod u+x build.sh
./build.sh --output /your/folder/to/save/containers
```

See `./build.sh --help` for more information.

You will need to add these line to your `nextflow.config` file.

```
params.container_dir = "/your/folder/to/save/containers"
apptainer.enabled = true
```

## nextflow

You will need to install nextflow on your system: [https://www.nextflow.io/](https://www.nextflow.io/)
