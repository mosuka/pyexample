.DEFAULT_GOAL := build

init:
	poetry config virtualenvs.in-project true
	poetry install

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

format:
	poetry run isort docs pyexample tests
	poetry run black docs pyexample tests

lint:
	poetry run isort --check --diff docs pyexample tests
	poetry run black --check docs pyexample tests

test:
	poetry run pytest --benchmark-skip --disable-warnings

coverage:
	poetry run pytest --benchmark-skip --disable-warnings --cov=pyexample --cov-report=html -v ./tests

benchmark:
	poetry run pytest --benchmark-only --disable-warnings --benchmark-autosave

build:
	poetry build

.PHONY: docs
docs:
	poetry run sphinx-apidoc -o ./docs_src ./pyexample
	poetry run sphinx-build ./docs_src ./docs
	echo "" > ./docs/.nojekyll

run:
	poetry run pyexample
