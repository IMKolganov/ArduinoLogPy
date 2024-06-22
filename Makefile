# Makefile

.PHONY: venv install run

venv:
	python3 -m venv venv

install: venv
	. venv/bin/activate && pip install -r requirements.txt

run: install
	. venv/bin/activate && python app.py
