#!/usr/bin/env bash


set -e

print_step () {
    printf "\n\n>>> $1\n\n"
}

COVERAGE_MIN=94

# Need to activate the virtualenv when running tests locally
if [ -e venv ]; then
    source venv/bin/activate
fi

print_step "Running unit/integration tests"
coverage erase
coverage run manage.py test --parallel --failfast
coverage combine && coverage report --fail-under=${COVERAGE_MIN}
