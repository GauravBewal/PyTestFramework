import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from datetime import datetime


class Action:

    def __init__(self, driver):
        self.driver = driver


    def click(self, element):
        element.click()

    def mouse_hover_on_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def getCountfromString(self, element):
        count = element.text
        return int(float(count.split('(')[1].split(')')[0]))

    def getcountfromapps(self, element):
        count = element.text
        return count.split(' ')[0]

    def sendKeys(self, inputfield, value):
        inputfield.send_keys(value)

    def clear_field(self, element):
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def clickEnter(self, inputfield):
        inputfield.send_keys(Keys.ENTER)
        action1 = ActionChains(self.driver)
        action1.send_keys(Keys.ENTER)
        action1.perform()

    def check_visibility_of_element(self, element):

        if element.is_displayed():
            return True
        else:
            return False


    def selectFromDD(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def getText(self, element):
        return element.text

    def getTitle(self):
        return self.driver.title

    def getattribute(self, element, attributeValue):
        return element.get_attribute(attributeValue)

    def currentTime(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def getElementColor(self, element):
        rgb = element.value_of_css_property('color')
        return Color.from_string(rgb).hex


    def getRandomDigit(self):
        res = ''.join(random.choices(string.digits, k=4))
        return res

    def WebdriverWait(self, element, wait):
        web_element = WebDriverWait(self.driver, wait).until(
            EC.presence_of_element_located(element))
        return web_element

    def accept_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to_alert()
        alert.dismiss()
