.DEFAULT_GOAL := build

init:
	poetry config virtualenvs.in-project true
	poetry install
	source $(poetry env info --path)/bin/activate

format:
	poetry run isort docs pyexample tests
	poetry run black docs pyexample tests

lint:
	poetry run isort --check --diff docs pyexample tests
	poetry run black --check docs pyexample tests

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=pyexample --cov-report=html -v ./tests

build:
	poetry build

.PHONY: docs
docs:
	poetry run sphinx-apidoc -o ./docs ./pyexample
	poetry run sphinx-build ./docs ./docs/_build
