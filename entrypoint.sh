#!/bin/bash

./venv_setup_mac.sh
source venv/bin/activate
pip install --upgrade --force-reinstall chromedriver-binary-auto
echo "$marker"
echo "$URL"
echo "$Email"
echo "$Password"
py.test -s -v -m $marker --url=$URL --email=$Email --password=$Password --html=./reports/report.html --capture sys
echo "Test Execution Completed!"