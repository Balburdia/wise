#!/usr/bin/env bash

set -x

mypy app
isort --recursive --check-only app
flake8
