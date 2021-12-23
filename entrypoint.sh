#!/bin/bash

./venv_setup_mac.sh
source venv/bin/activate
py.test -s -v -m $marker --html=./reports/report.html --capture sys
echo "Test Execution COmpleted!"