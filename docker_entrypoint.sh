#!/bin/bash
cd csol_automation_suite
ls -la
./venv_setup_mac.sh
source venv/bin/activate
echo "$marker"
echo "$URL"
echo "$Email"
echo "$Password"
py.test -s -v -m $marker --url=$URL --email=$Email --password=$Password --html=./reports/report.html --junitxml=./reports/result.xml --capture sys
echo "Test Execution Completed!"
#[ -f jenkins/bridge.sh ] && chmod +x jenkins/bridge.sh && . jenkins/bridge.sh;
