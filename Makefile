SHELL := /bin/bash -e

all: full_lint

full_lint: lint mypy

lint:
	flake8 --max-line-length=100 eth_kms_signer/
	black --line-length=100 -check --diff eth_kms_signer/

mypy:
	mypy --show-error-codes --ignore-missing-imports --show-traceback eth_kms_signer/

.PHONY: all, full_lint, lint
