#!/bin/bash

py.test -s -v -m smoke --html=./reports/report.html --capture sys
