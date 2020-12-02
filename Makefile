PY_ENV_EXEC ?= PYTHONPATH=src poetry run

# Repository setup
.PHONY: setup
setup:
	poetry install

# Cleaning
.PHONY: poetry-clean
poetry-clean:
	rm -rf $(poetry env info --path)

# Shorthands for editors
.PHONY: jupyter-notebook
jupyter-notebook: export PYTHONPATH=src/
jupyter-notebook:
	$(PY_ENV_EXEC) jupyter notebook

.PHONY: code
code:
	PYTHONPATH=src code .

# tests
.PHONY: test
test:
	$(PY_ENV_EXEC) pytest test/


# get answer ARG from command line
answer:
	$(PY_ENV_EXEC) python src/day$(DAY).py

# get specific answer
answer1:
	$(PY_ENV_EXEC) python src/day1.py