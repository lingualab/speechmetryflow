#!/usr/bin/env bash
set -euo pipefail

# Resolve the directory where THIS script lives
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

#####################################
# Usage message
#####################################
usage() {
    cat <<EOF
Usage: $(basename "$0") --output DIR [--container CONTAINER] [--device cpu|gpu] [--options OPTIONS] [--dry-run]

Building the containers needed for speechmetryflow

Required arguments:
  -o, --output DIR          Output directory

Optional arguments:
  --container CONTAINER     Name of the container to build (default: all).
                            It's the name of the folder inside this directory or all 
  --device cpu|gpu          Execution device (default: cpu)
  --options OPTIONS         Apptainer build local options (default:"--fakeroot")
  -n, --dry-run                Just prnt the paptainer command
  -h, --help                Show this help
EOF
    exit 1
}

#####################################
# Default values
#####################################
OUTPUT=""
CONTAINERS=("all")
DEVICE="cpu"
APPTAINER_BUILD_LOCAL_OPTIONS="--fakeroot"
DRY_RUN=0

#####################################
# Parse arguments
#####################################
while [[ $# -gt 0 ]]; do
    case "$1" in
        -o|--output)
            OUTPUT="$2"
            shift 2
            ;;
        --container)
            read -r -a containers <<< "$2"
            CONTAINERS=("${containers[@]}")
            shift 2
            ;;
        --device)
            DEVICE="$2"
            shift 2
            ;;
        --options)
            APPTAINER_BUILD_LOCAL_OPTIONS="$2"
            shift 2
            ;;
        -n|--dry-run)
            DRY_RUN=1
            shift 1
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown argument: $1"
            usage
            ;;
    esac
done

#####################################
# Validate required arguments
#####################################
if [[ -z "${OUTPUT}" ]]
then
    echo "Error: --output is required"
    usage
fi

if [[ "${DEVICE}" != "cpu" && "${DEVICE}" != "gpu" ]]
then
    echo "Error: --device must be either 'cpu' or 'gpu'"
    exit 1
fi

#####################################
# Validate argument correctness
#####################################
OUTPUT=$(realpath ${OUTPUT})
mkdir -p "${OUTPUT}"

#####################################
# Building containers
#####################################

# Find recipe.def files
if [[ ${#CONTAINERS[@]} -eq 1 && ${CONTAINERS[0]} == "all" ]]
then
    recipes=(${SCRIPT_DIR}/*/recipe.def)
else
    recipes=()
    for name in "${CONTAINERS[@]}"
    do
        recipes+=("${SCRIPT_DIR}/${name}/recipe.def")
    done
fi

# Executing apptainer
for recipe in "${recipes[@]}"
do
    [ -f "${recipe}" ] || continue

    # extract container name
    container_name=$(basename "$(dirname "${recipe}")")

    # find env.txt file
    recipe_env=$(dirname "${recipe}")/env.txt
    source ${recipe_env}

    APPTAINER_BUILD_LOCAL_OPTIONS="${APPTAINER_BUILD_LOCAL_OPTIONS} --build-arg-file ${recipe_env}"
    container_path="${OUTPUT}/${APP_NAME}_${APP_VERSION}.sif"

    if [[ "${container_name}" == "speechmetryflow" || "${container_name}" == "whisper" ]]
    then
        APPTAINER_BUILD_LOCAL_OPTIONS="${APPTAINER_BUILD_LOCAL_OPTIONS} --build-arg DEVICE=${DEVICE}"
        container_path=${container_path/.sif/_${DEVICE}.sif}
    fi

    apptainer_cmd="apptainer build ${APPTAINER_BUILD_LOCAL_OPTIONS} ${container_path} ${recipe}"
    echo "==> Running: ${apptainer_cmd}"

    if [ ${DRY_RUN} -eq 0 ]
    then
        cd ${container_name}
        ${apptainer_cmd}
        cd ..
    fi
done
