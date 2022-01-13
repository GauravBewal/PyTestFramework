#!/bin/bash

./venv_setup_mac.sh
source venv/bin/activate
py.test -s -v -m $marker --url=$URL --email=$Email --password=$Password --html=./reports/report.html --capture sys
echo "Test Execution Completed!"