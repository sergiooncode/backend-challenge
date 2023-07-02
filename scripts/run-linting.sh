#!/usr/bin/env bash

set -e

GREEN='\33[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

cd /code

if [ "$1" = "yes" ]
then
    echo -e "${RED}Running${NC} pycln to remove unused imports..."
    pycln src/ --all
    echo -e "${RED}Running${NC} isort to sort imports..."
    isort src/
    echo -e "${RED}Running${NC} black to format python code..."
    black src/
else
    echo -e "${GREEN}Running${NC} pycln to check for unused imports..."
    pycln src/ --check
    echo -e "${GREEN}Running${NC} isort to check for imports ordering..."
    isort --check-only src/
    echo -e "${GREEN}Running${NC} black to check python formatting..."
    black --check src/
fi
