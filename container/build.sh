#!/usr/bin/env bash

# Building
container_name="speechmetryflow_0.0.1.sif"
apptainer build -F ${container_name} container.def

# Publishing
rsync -av ${container_name} elm:/data/brambati/local/containers/lingualab/
