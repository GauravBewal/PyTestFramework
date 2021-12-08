from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Action:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def sendKeys(self, inputfield, value):
        inputfield.send_keys(value)

    def selectFromDD(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def getText(self, element):
        return element.text

    def getTitle(self):
        return self.driver.title
