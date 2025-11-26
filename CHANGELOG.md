# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Added, Changed, Deprecated, Removed, Fixed, Security. 

### Added

- `.gitattributes` to enforce consistent end-of-line.

## [v0.2.2] – 2025-11-21

### Fixed

- hatch build includes CSV and JSON files.

### Changed

- Updated file permissions for `containers/build.sh`.

## [v0.2.1] – 2025-11-21

### Added

- `optional-dependencies` in `pyproject.toml`.
- `build.sh` script for container image generation with apptainer.
- `Makefile` to simplify development workflows.
- project URLs to `pyproject.toml` metadata.

### Changed

- apptainer recipes to use new `build-arg` syntax.
- nextflow configuration to define a dedicated container directory.

### Fixed

- linting and formatting to speechmetryflow python.

## [v0.2.0] – 2025-11-19

### Added

- text2variable is now a python module inside this repository.
- extraction of TextDescriptives metrics.
- speechmetryflow apptainer container recipes:
  - Whisper
  - lingualabpy
  - OpenSMILE
  - speechmetryflow python

### Changed

- container paths in `nextflow.config`.
- documentation is now in english.

## [v0.1.0] – 2025-07-03

First public release of speechmetryflow.

### Added

- github workflow to build the documentation.
- transfert the notion documentation to the repository.
- whisper module in nextflow.
- opensmile module in nextflow.
- a license.
- whisper, opensmile and praat container for UNF nextflow profile

### Changed

- switch nextflow to DSL2

## [0.0.5] – 2025-01-31

### Changed

- Updated container version to 0.0.5.

## [0.0.4] – 2025-01-30

### Fixed

- default parameters to define audio and text folders.

## [0.0.3] – 2024-12-10

### Added

- link to the notion documentation.
- a nextflow profile for UNF-Montréal.
- a `task` argument (cookie_theft or picnic) to extract the associated metrics.

## [0.0.2] – 2024-07-08

### Added

- uhm-o-meter process integration in nextflow.
- example how to launch on elm server at UNF-Montréal.

## [0.0.1] – 2024-06-27

### Added

- Basic nextflow pipeline to interact with two scripts:
  - `text2variable` for text metrics.
  - `lingualabpy_audio_metrics` for adio metrics.
