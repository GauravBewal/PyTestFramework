"""
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager


class WebDriverFactory:

    def __init__(self, browser, baseUrl):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser.lower()
        self.baseUrl = baseUrl

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

         Returns:
             'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif self.browser == "chrome":
            # Set chrome driver
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        else:
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(20)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)
        return driver

