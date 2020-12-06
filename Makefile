PY_ENV_EXEC ?= PYTHONPATH=src poetry run

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

# Initialize for a new day
init_day:
	touch data/day$(DAY).csv
	touch test/data/day$(DAY).csv
	cp template_day.py src/day$(DAY).py
	cp template_day_test.py test/day$(DAY)_test.py

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