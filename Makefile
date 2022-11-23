
#python setup.py develop # ничего не генерировать, просто установить локально
#python setup.py bdist_egg # сгенерировать дистрибутив «яйцо», не включать зависимости
#python setup.py bdist_wheel # сгенерировать версионированное «колесо», включить зависимости
#python setup.py sdist --formats=zip,gztar,bztar,ztar,tar # исходный код

upgrade: ## Upgrade pip.
	python -m pip install --upgrade pip

run: ## run
	pipenv run python src/pynn/main.py

lint: ## lint
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

venv: ## Init .venv
	python -m venv .venv
	source .venv/Scripts/activate

pipenv-install: ## Install pipenv.
	pip install --user pipenv
	pipenv install -d requests mypy autopep8 flake8 pytest bandit pydocstyle
	pipenv lock

pipenv-shell: ## Shell.
	pipenv shell

pipenv-shell-deactivate: ## Deactivate shell.
	deactivate

pipenv-where: ## Locate the project.
	pipenv --where

pipenv-venv: ## Locate the virtualenv.
	pipenv --venv

pipenv-py: ## Locate the Python interpreter.
	pipenv --py

pipenv-new-project: ## Create a new project using Python 3.7, specifically.
	pipenv --python 3.7

pipenv-remove: ## Remove project virtualenv (inferred from current directory).
	pipenv --rm

pipenv-install-dev: ## Install all dependencies for a project (including dev).
	pipenv install --dev

pipenv-lock-pre: ## Create a lockfile containing pre-releases.
	pipenv lock --pre

pipenv-graph: ## Show a graph of your installed dependencies.
	pipenv graph

pipenv-clean: ## Uninstalls all packages not specified in Pipfile.lock.
	pipenv clean

pipenv-check: ## Check your installed dependencies for security vulnerabilities.
	pipenv check

pipenv-install-env: ## Install a local setup.py into your virtual environment/Pipfile.
	pipenv install -e .

pipenv-pip-freeze: ## Use a lower-level pip command.
	pipenv run pip freeze

pipenv-upgrade: ## Upgrade pipenv.
	pip install --user --upgrade pipenv

sphinx-init: ## venv ## init sphinx
	python -m pip install sphinx
	sphinx-build --version
	sphinx-quickstart docs

sphinx-clean: ## clean sphinx
	@rm -rf docs/build/

sphinx-build-html: sphinx-clean ## build sphinx
	sphinx-build -b html docs/source/ docs/build/html

packaging: ## New project
	python -m venv .venv
	source .venv/bin/activate
	pip install --user pipenv
	pipenv install -d requests mypy autopep8 flake8 pytest bandit pydocstyle sphinx
	pipenv lock
	sphinx-quickstart docs

set-url: ## git remote set-url origin git@github.com:login/repo.git
	git remote set-url origin git@github.com:teratron/pynn.git

message = Tests
branch = master
add-commit-push: ## add commit push
	git add .
	git commit -m "$(message)"
	git push origin $(branch)

.PHONY: help
help:
	@echo "Tasks in \033[1;32mnettix\033[0m:"
	@awk '                                             \
		BEGIN {FS = ":.*?## "}                         \
		/^[a-zA-Z_-]+:.*?## /                          \
		{printf "\033[36m%-24s\033[0m %s\n", $$1, $$2} \
	'                                                  \
	$(MAKEFILE_LIST)

.DEFAULT_GOAL := help
