from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime


class Action:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def sendKeys(self, inputfield, value):
        inputfield.send_keys(value)

    def clickEnter(self, inputfield):
        inputfield.send_keys(Keys.ENTER)

    def selectFromDD(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def getText(self, element):
        return element.text

    def getTitle(self):
        return self.driver.title

    def CurrentTime(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

