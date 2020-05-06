install:
	@poetry install

selfcheck:
	poetry check

lint:
	poetry run flake8 brain_games

check: selfcheck lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build