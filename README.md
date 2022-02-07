**Cyware Orchestrate UI Automation Test Framework**  

**Pre-requisite :**  
1. This framework will support only for Cyware Orchestrate 3.X version instances only.  
2. Google Captcha\OTP should not be enabled for automation running instance.    
3. Don't login with system admin credentials while automation suite jenkins job run status is in progress.   

**Bitbucket URL:** https://bitbucket.org/cywarelabs/csol_automation_suite  
**Jenkins Job URL:** https://jenkins.cyware.com/job/csol-ui-automation/

- Selenium python UI testing framework
- Docker enable framework for execution in isolated environment
- Supports Window/Mac/Linux

  
**Directory Structure**    
**configuration** - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration  
**testCases** - Place to put all test scripts\conftest  
**testData** - All data will be placed related to testCases will be placed here  
**reports** - All the output reports xml/html and screenshots will come in this directory  
**testdata** - Any testdata related to testing will be put here. eg files, csv, png etc    
**utilities** - Base and all common actions related classes files are placed here  
**pageObjects** - All module related pages and elements are placed here    
  

**How to Configure on a User's System**

- First run command "git clone git@bitbucket.org:cywarelabs/csol_automation_suite.git" in any workspace via terminal
- Open PyCharm editor, Select File -> Open project and open git cloned folder
- Run the script from pycharm terminal "venv_setup_mac.sh"
- If venv doesn't set run command again on terminal "source venv/bin/activate"

**Installation Requirements**
Although latest version of python and the modules can be used, below are the tested versions.  

Python Version - 3.9 (pre-install)  
setuptools==56.1.0 (pre-install)  
pip==21.1.1 (pre-install)  
selenium==3.141.0  
webdriver-manager==3.5.2  
pytest==6.2.5  
pytest-html==3.1.1  
pytest-xdist==2.4.0  
configparser==5.2.0  

**NOTE:** webdriver-manager should automatically install the drivers required for automation.  