#!/bin/bash
COPY . /csol_automation_suite
WORKDIR /csol_automation_suite
python3 --version
export PYTHONPATH=/csol_automation_suite
#cd csol_automation_suite
ls -la
./venv_setup_mac.sh
source venv/bin/activate
echo "$marker"
echo "$URL"
echo "$Email"
echo "$Password"
py.test -s -v -m $marker --url=$URL --email=$Email --password=$Password --html=./reports/report.html --junitxml=./reports/result.xml --capture sys
echo "Test Execution Completed!"
python3 jenkins/xml_to_simplified_html.py -n reports/simplified_html.html -r reports

#[ -f jenkins/bridge.sh ] && chmod +x jenkins/bridge.sh && . jenkins/bridge.sh;
