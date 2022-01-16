import os.path
import time

import pytest

from configuration.readConfiguration import ReadConfig
from utilities.webdriver_factory import WebDriverFactory

webapp_driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--url", action="store", default=ReadConfig.getAppURL())
    parser.addoption("--email", action="store", default=ReadConfig.getUserEmail())
    parser.addoption("--password", action="store", default=ReadConfig.getPassword())


@pytest.fixture(scope="class", autouse=True)
def setup(request):
    global webapp_driver
    browser_name = request.config.getoption("browser_name")
    base_url = request.config.getoption("url")
    getEmail = request.config.getoption("email")
    getPassword = request.config.getoption("password")
    wd = WebDriverFactory(browser_name, base_url)
    webapp_driver = wd.getWebDriverInstance()
    login(getEmail, getPassword)
    request.cls.driver = webapp_driver
    yield
    webapp_driver.close()


def login(getEmail, getPassword):

    text_field_emailID = "//input[@aria-placeholder='Enter your e-mail address']"
    text_filed_password = "//input[@aria-placeholder='Enter your password']"
    button_login = "//button[contains(text(),'Login')]"

    try:
        put_emailId = webapp_driver.find_element_by_xpath(text_field_emailID)
        put_emailId.send_keys(getEmail)
        put_password = webapp_driver.find_element_by_xpath(text_filed_password)
        put_password.send_keys(getPassword)
        click_Login = webapp_driver.find_element_by_xpath(button_login)
        click_Login.click()
        time.sleep(2)
    except Exception as e:
        print(e)


def _capture_screenshot(name):
    global webapp_driver
    webapp_driver.get_screenshot_as_file(name)


@pytest.mark.hookwrapper()
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
            tc_name = report.nodeid.split("::")[-1]
            current_folder = os.path.dirname(os.path.abspath(__file__))
            report_path = os.path.join(current_folder, '../', 'reports', 'screenshots')
            # Check whether the specified path exists or not
            isExist = os.path.exists(report_path)
            if not isExist:
                # Create a new directory because it does not exist
                os.makedirs(report_path)
                print("screenshots directory is created!")
            file_name = report_path + "/" + tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Cyware Orchestrate UI Testcases Execution Report"


def pytest_configure(config):
    config._metadata["Instance URL"] = getUrl


def getUrl(request):
    return request.config.getoption("url")
