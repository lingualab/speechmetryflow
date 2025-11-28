# Variables
PYTHON := python3

# Default target: show help
help:
	@echo "Available commands:"
	@echo "  make test           - Run tests"
	@echo "  make lint           - Run linters"
	@echo "  make format         - Auto-format code"
	@echo "  make build          - Build wheel and sdist"
	@echo "  make clean          - Remove build artifacts"

test:
	$(PYTHON) -m pytest -q

lint:
	ruff check src/speechmetryflow tests

format:
	ruff format src/speechmetryflow tests
	black src/speechmetryflow tests

build:
	hatch build

clean:
	rm -rf dist build *.egg-info
	find src/ -type d -name "__pycache__" -exec rm -r {} +
