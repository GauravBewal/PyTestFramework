import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from configuration.readConfiguration import *

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",
                     default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get(ReadConfig.getAppURL())
    driver.implicitly_wait(ReadConfig.defaultWait())  # seconds
    login()
    # get the url from conf file
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the Pytest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.replace("::", "_")[-1]
            os.environ["PYTHONPATH"] = os.path.join(os.getcwd().split("CSOL_Automation_Test")[0],
                                                    "CSOL_Automation_Test")
            file_path = os.path.join(os.environ["PYTHONPATH"], "./reports/screenshots/")
            file_name = file_path + tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def login():
    emailId = driver.find_element_by_xpath("//input[@aria-placeholder='Enter your e-mail address']")
    emailId.send_keys(ReadConfig.getUserEmail())
    password = driver.find_element_by_xpath("//input[@aria-placeholder='Enter your password']")
    password.send_keys(ReadConfig.getPassword())
    clickLogin = driver.find_element_by_xpath("//button[contains(text(),'Login')]")
    clickLogin.click()
