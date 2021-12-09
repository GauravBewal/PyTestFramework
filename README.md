**CSOL UI Automation Test**  
Bitbucket URL: https://bitbucket.org/cywarelabs/csol_automation_suite \
QA Jenkins PROJECTS: https://jenkins.cyware.com/view/Pipelines-CSOL/job/csol-ui-automation/


- Selenium python UI testing framework
- Docker enable framework for execution in isolated environment
- Supports Window/Mac/Linux

  
**Directory Structure**    
**configuration** - Defines a place to put all the configuration related stuff, use config.ini to edit the run configuration  
**testCases** - Place to put all test scripts\conftest  
**reports** - All the output reports xml/html and screenshots will come in this directory.  
**testdata** - Any testdata related to testing will be put here. eg files, csv, png etc  
**utilities** - Base and all common actions related classes files are placed here.\
**pageObjects** - All module related pages and elements are placed here.  
  

**How to Configure on a User's System**

- First run command "git clone git@bitbucket.org:cywarelabs/csol_automation_suite.git" in any workspace via terminal
- Open PyCharm editor, Select Open project and open git cloned folder
- Run the script from pycharm terminal "venv_setup_mac.sh"
- If venv doesn't set run command again on terminal "source venv/bin/activate"

**Installation Requirements**
Although latest version of python and the modules can be used, below are the tested versions.  

Python Version - 3.9 (pre-install)\
setuptools==56.1.0 (pre-install)\
pip==21.1.1 (pre-install)\
selenium==3.141.0\
webdriver-manager==3.5.2\
pytest==6.2.5\
pytest-html==3.1.1\
pytest-xdist==2.4.0\
configparser==5.2.0

NOTE: webdriver-manager should automatically install the drivers required for automation.


