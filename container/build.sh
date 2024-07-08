#!/usr/bin/env bash
#
# Setup
# apptainer key newpair
# apptainer registry login --username lingualab docker://docker.io

# Building
container_name="speechmetryflow_0.0.2.sif"
apptainer build --fakeroot -F /data/brambati/local/containers/lingualab/${container_name} container.def

# Signing
# apptainer sign ${container_name}
# apptainer push ${container_name} docker://lingualab/speechmetryflow:dev

# Publishing
