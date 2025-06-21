.PHONY: install test lint format clean build publish

install:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest test_taskdaily --cov=taskdaily --cov-report=term-missing

lint:
	flake8 taskdaily
	mypy taskdaily
	black --check taskdaily
	isort --check-only taskdaily

format:
	black taskdaily test_taskdaily
	isort taskdaily test_taskdaily

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

build: clean
	python -m build

publish: build
	twine upload dist/*
