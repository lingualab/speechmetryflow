#!/usr/bin/env bash

container_name="speechmetryflow_dev.sif"
apptainer build -F ${container_name} container.def
rsync -av ${container_name} elm:/data/brambati/local/containers/lingualab/
