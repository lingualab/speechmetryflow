# Variables
PYTHON := python3

# Default target: show help
help:
	@echo "Available commands:"
	@echo "  make lint           - Run linters"
	@echo "  make format         - Auto-format code"
	@echo "  make build          - Build wheel and sdist"
	@echo "  make clean          - Remove build artifacts"

lint:
	ruff check src/speechmetryflow

format:
	ruff format src/speechmetryflow
	black src/speechmetryflow

build:
	hatch build

clean:
	rm -rf dist build *.egg-info
	find src/ -type d -name "__pycache__" -exec rm -r {} +
