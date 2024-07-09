targets = setup install run lint format test clean

.PHONY: help $(targets)

help:
	@echo "Available targets: $(targets)"

setup:
	chmod +x ./setup.sh
	./setup.sh

install:
	pip install -r requirements.txt

run:
	python3 main.py

lint:
	ruff check --fix

format:
	ruff format

test:
	pytest -s

clean:
	rm -r __pycache__ .pytest_cache .ruff_cache .venv
