**CTIX Tests**  
Bitbucket URL: https://bitbucket.org/cywarelabs/ctix_tests  
QA Jenkins PROJECTS: https://jenkins.cyware.com/view/CTIX_TESTS/
- Selenium python UI/API testing framework
- Docker enable framework for execution in isolated environment
- Supports Windows/Mac/Linux

  
**Directory Structure**    
**config** - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration  
**jenkins** - This directory is used for jenkins related execution. Contains Docker configuration etc.  
**lib** - Contains Library methods common and application related.  
**PROJECTS** - Place to put the test scripts  
**reports** - All the output reports xml/html will come in this directory.  
**testdata** - Any testdata related to testing will be put here. eg files, csv, png etc  
**tools** - Third party tools, Keys, web drivers will be placed here.  
**execute_*** - Execution entry point to initiate testing on test plan.  
  

**How to Configure on a User's System**

**Method 1** 
- Detailed Setup Guide: https://docs.google.com/document/d/11Wwsnw68bm3fpckWRaqnlrCpeLF7p3HqhvfgXQV1TNo/edit?usp=sharing  
- Checkout Workspace
- Open in PyCharm editor , select venv environment with python 3.x and install the dependencies
- Select the script from PROJECTS and run in the editor.

**Method 2**
- Checkout Workspace
- Install Python and below dependencies
- Configure settings in config/config.ini
- Change Directory to parent ctix_tests
- Run execute_testplan.sh




**Installation Requirements**  
Although latest version of python and the modules can be used, below are the tested versions.  
Python Version - 3.8    
numpy==1.19.5  
xmlrunner==1.7.7  
webdriver-manager (Latest version)  
urllib3==1.26.4  
six==1.16.0  
selenium==3.141.0  
pytz==2021.1  
python-dateutil==2.8.1  
configparser==5.0.2  
html-testRunner==1.2.1  
Pillow==8.3.1  
matplotlib==3.4.2  
pandas==1.2.4  

setuptools==56.1.0 (pre existing)  
pip==21.1.1 (pre existing)  
  
**Browsers**
Install Chrome Browser (90.0.4430.212-1) 
Install Firefox Browser (NOTE: Console debug logs doesn't work with firefox, Driver Limitations)  

NOTE: webdriver-manager should automatically install the drivers required for automation.

**Directory Structure Detailed**  
```
├── ** config - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration  
│   ├── config.ini  
│   ├── process_config.py  
│   └── testplans  
│       └── ui_sanity.txt  
├── ** execute_testplan.sh - Entry Point to initiate test plan
├── ** jenkins - This directory is used for jenkins related execution. Contains Docker configuration etc.  
│   ├── docker_entrypoint.sh  
│   ├── Dockerfile  
│   └── email_report_generate.py  
├── ** lib - Contains Library methods common and application related.
│   ├── common_functions.py  
│   └── ui  
│       └── app_navigation.py  
├── ** PROJECTS - Place to put the test scripts
│   ├── API  
│   │   └── readme  
│   └── UI  
│       ├── test_checks.py  
│       └── test_navigation_checks.py  
├── README.md  
├── ** reports - All the output reports xml/html will come in this directory.
│   └── readme.txt  
├── ** testdata - Any testdata related to testing will be put here. eg files, csv, png etc
│   └── inviteusers.csv  
└── ** tools - Third party tools, Keys, web drivers will be placed here.
    └── macos  
        ├── chromedriver  
        └── geckodriver  
```