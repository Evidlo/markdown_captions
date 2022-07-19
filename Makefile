# Evan Widloski - 2019-03-04
# makefile for building/testing

# run all lines in target in single shell, quit on error
.ONESHELL:
.SHELLFLAGS=-ec

.PHONY: dist
dist:
	python setup.py sdist

.PHONY: pypi
pypi: dist
	twine upload $(wildcard dist/*.tar.gz)

.PHONY: clean
clean:
	rm dist/*
