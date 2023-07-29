install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest backend/app/tests/test.py