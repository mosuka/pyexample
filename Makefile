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
	poetry run pytest --benchmark-skip

coverage:
	poetry run pytest --cov=pyexample --cov-report=html -v ./tests

benchmark:
	poetry run pytest --benchmark-only --benchmark-autosave

build:
	poetry build

.PHONY: docs
docs:
	poetry run sphinx-apidoc -o ./docs_src ./pyexample
	poetry run sphinx-build ./docs_src ./docs
	echo "" > ./docs/.nojekyll
