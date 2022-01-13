#!/usr/bin/env bash

py.test -s -v -m "readOnly" --url="https://csol-freemium.cywareqa.com/soar" --email="sandeep.kumar@cyware.com" --password="Cywarelabs@2022" --html=./reports/report.html --capture sys