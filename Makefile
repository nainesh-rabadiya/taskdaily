.PHONY: clean install test build publish

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

install:
	pip install -e .

test:
	python -m pytest tests/

build: clean
	python setup.py sdist bdist_wheel

publish: build
	twine upload dist/*

lint:
	flake8 nainesh_daily
	mypy nainesh_daily
	black nainesh_daily --check

format:
	black nainesh_daily

dev-setup:
	pip install -e ".[dev]"
	pre-commit install 