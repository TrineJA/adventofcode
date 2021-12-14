PY_ENV_EXEC ?= PYTHONPATH=src pipenv run

# Shorthands for editors
.PHONY: jupyter-notebook
jupyter-notebook: export PYTHONPATH=src/
jupyter-notebook:
	$(PY_ENV_EXEC) jupyter notebook

# Initialize for a new day
init_day:
	touch data/2021/day$(DAY).csv
	touch test/2021/data/day$(DAY).csv
	cp -n template_day.py src/year2021/day$(DAY).py
	cp -n template_day_test.py test/2021/day$(DAY)_test.py

# tests
.PHONY: test
test:
	$(PY_ENV_EXEC) pytest test/2021

# get answer ARG from command line
answer:
	$(PY_ENV_EXEC) python src/year2021/day$(DAY).py
