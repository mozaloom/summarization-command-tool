install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702 summarize/main.py

format:
	black *.py

build:
	python setup.py develop

all: install lint format