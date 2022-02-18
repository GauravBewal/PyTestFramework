import random
import string
from datetime import datetime

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait



class Action:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        element.click()

    def switch_new_window(self, window_number):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        size = len(all_windows)
        for x in range(size):
            if(x == window_number):
                self.driver.switch_to.window(all_windows[x])
                break
        return parent_window



    def switch_back_parent_window(self, parent_window):
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def mouse_hover_on_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def javascript_click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def getCountfromString(self, element):
        count = element.text
        return int(float(count.split('(')[1].split(')')[0]))

    def get_walkthrough_slider_count(self, element):
        count = element.text
        return int(count.split(' ')[2])

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


