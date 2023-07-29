install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv app/tests/test.py
	
lint:
	python -m flake8 app/

build:
	git add . && git commit -m 'dev_to_main' && git push origin main