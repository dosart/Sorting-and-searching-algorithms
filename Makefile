install:
	@poetry install

test:
	poetry run coverage run --source=algorithms -m pytest tests

lint:
	poetry run flake8 algorithms

check:
	@make selfcheck
	@make test
	@make lint

build:
	@make check
	@poetry build
