# Adapted from cookiecutter version:
https://github.com/audreyr/cookiecutter/blob/master/Makefile
PYPI_SERVER = pypitest

.DEFAULT_GOAL := help

.PHONY: clean
clean: ## Remove all file artifacts
	@echo "+ $@"
	## Remove build artifacts
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

	## Remove Python file artifacts
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

	## Clean docs
	@$(MAKE) -C docs clean

.PHONY: lint
lint: ## Check code style with flake8
	@echo "+ $@"
	@flake8 setup.py tests mould ##tox -e flake8

.PHONY: ci
ci: test lint ## Run continuous integration check
	@echo "+ $@"

.PHONY: test
test: ## Run tests quickly with the default Python
	@echo "+ $@"
	@py.test -vv --cov=mould --cov-report=term-missing

.PHONY: testwatch
testwatch: test ## Run tests automatically
	@echo "+ $@"
	@watchmedo shell-command -p '*.py' -c '$(MAKE) test' -R -D .

.PHONY: docs
docs: ## Generate Sphinx HTML documentation, including API docs
	@echo "+ $@"
	@sphinx-apidoc -o docs/ mould
	@rm -f docs/modules.rst
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html

.PHONY: servedocs
servedocs: docs ## Rebuild docs automatically
	@echo "+ $@"
	@watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

.PHONY: release
release: clean package ## Package and upload release
	@echo "+ $@ ##changes"

.PHONY: package
package: clean ## Build distribution
	@echo "+ $@"
	@python setup.py sdist bdist_wheel
	@ls -l dist

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
