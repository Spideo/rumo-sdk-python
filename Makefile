#Makefile
SHELL=/bin/bash -o pipefail
CMD:=poetry run

install:
	poetry install

format-black:
	$(CMD) black .
format-isort:
	$(CMD) isort .

lint-black:
	$(CMD) black . --check --diff
lint-isort:
	$(CMD) isort . --check
lint-flake8:
	$(CMD) flake8 .

pytype:
	$(CMD) pytype .

format: format-black format-isort

lint: lint-black lint-isort lint-flake8

test:
	$(CMD) pytest -v

test-cov:
	$(CMD) pytest --cov=src --cov-report term-missing --cov-report=html --junitxml=pytest.xml | tee pytest-coverage.txt

clean-cov:
	@rm -rf htmlcov
	@rm -f .coverage pytest-coverage.txt pytest.xml
