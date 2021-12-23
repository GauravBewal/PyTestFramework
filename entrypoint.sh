#!/bin/bash

sudo ./venv_setup_mac.sh
source venv/bin/activate
py.test -s -v -m smoke --html=./reports/report.html --capture sys