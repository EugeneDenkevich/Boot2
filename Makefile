install:
	pip install --upgrade pip &&\
	pip install -r app/requirements.txt

test:
	python -m pytest -vv app/tests/test.py
	
lint:
	python -m flake8 app/
