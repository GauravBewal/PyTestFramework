from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC



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

    def getcountfromapps(self,element):
        count = element.text
        return  count.split(' ')[0]

    def sendKeys(self, inputfield, value):
        inputfield.send_keys(value)

    def clear_field(self,element):
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def clickEnter(self, inputfield):
        inputfield.send_keys(Keys.ENTER)
        action1 = ActionChains(self.driver)
        action1.send_keys(Keys.ENTER)
        action1.perform()

    def selectFromDD(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def getText(self, element):
        return element.text

    def getTitle(self):
        return self.driver.title

    def CurrentTime(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def getrandomdigit(self):
        res = ''.join(random.choices(string.digits, k=4))
        return res
