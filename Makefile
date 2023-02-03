
delete-garbage: ## delete garbage
	@find . -path './**/config.json' -delete

upgrade: ## Upgrade pip.
	python -m pip install --upgrade pip

run: ## run
	poetry run python src/pynn/main.py

lint: ## lint
	black src
	mypy src --ignore-missing-imports
	flake8 src --ignore=$(shell cat .flakeignore)

dev: ## dev
	pip install -e .

test: dev ## test
	pytest --doctest-modules --junitxml=junit/test-results.xml
	bandit -r src -f xml -o junit/security.xml || true

build: clean ## build
	pip install wheel
	python setup.py bdist_wheel

clean: ## clean
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete

poetry: ## Init .venv
	python -m venv .venv
	pip install -U pip setuptools
	pip install poetry
	source .venv/bin/activate

packaging: poetry ## New project
	poetry lock
	poetry add --group dev requests pre-commit black pylint flake8 autopep8 bandit
	poetry add --group typing mypy
	poetry add --group docs pydocstyle sphinx
	poetry add --group test pytest
	sphinx-quickstart docs

set-url: ## git remote set-url origin git@github.com:login/repo.git
	git remote set-url origin git@github.com:teratron/pynn.git

message = Properties
branch = master
add-commit-push: ## add commit push
	git add .
	git commit -m "$(message)"
	git push origin $(branch)

.PHONY: help
help:
	@echo "Tasks in \033[1;32mpynn\033[0m:"
	@awk '                                             \
		BEGIN {FS = ":.*?## "}                         \
		/^[a-zA-Z_-]+:.*?## /                          \
		{printf "\033[36m%-24s\033[0m %s\n", $$1, $$2} \
	'                                                  \
	$(MAKEFILE_LIST)

.DEFAULT_GOAL := help
