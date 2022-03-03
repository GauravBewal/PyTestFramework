import random
import string
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utilities.Base import Base


class Action(Base):

    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, by, path):
        element = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((by, path)))
        element.click()

    def normal_click(self, by, path):
        self.driver.find_element(by, path).click()

    def click_if_element_found(self, by, path):
        log = self.getlogger()
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable((by, path))).click()
        except (NoSuchElementException, TimeoutException):
            log.info("Automatic walk through was not initiated. Hence passing this testcase")
            pass

    def get_no_of_elements_present(self, by, path):
        elements = self.driver.find_elements(by, path)
        return len(elements)

    def switch_new_window(self, window_number):
        parent_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        size = len(all_windows)
        for x in range(size):
            if x == window_number:
                self.driver.switch_to.window(all_windows[x])
                break
        return parent_window

    def switch_back_parent_window(self, parent_window):
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def mouse_hover_on_element(self, by, path):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        hover = ActionChains(self.driver).move_to_element(ele)
        hover.perform()

    def javascript_click_element(self, by, path):
        element = self.driver.find_element(by, path)
        self.driver.execute_script("arguments[0].click();", element)

    def get_count_from_string(self, by, path):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((by, path)))
        count = ele.text
        return int(float(count.split('(')[1].split(')')[0]))

    def get_no_of_walkthrough_and_pagination_count(self, by, path):
        element = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        count = element.text.split(' ')[2]
        return int(count)

    def get_current_page_number(self, by, path):
        element = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        count = element.text
        return int(count.split(' ')[0])

    def send_keys(self, by, path, value):
        element = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        element.send_keys(value)

    def clear_field(self, by, path):
        element = self.driver.find_element(by, path)
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def click_enter(self, by, path):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((by, path)))
        ele.send_keys(Keys.ENTER)
        action1 = ActionChains(self.driver)
        action1.send_keys(Keys.ENTER)
        action1.perform()

    def check_visibility_of_element(self, by, path):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        if ele.is_displayed():
            return True
        else:
            return False

    def select_from_drop_down(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def get_text(self, by, path):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        return ele.text

    def read_search_result(self, by, path, value):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.text_to_be_present_in_element((by, path), value))
        if ele == True:
            return self.driver.find_element(by, path).text

    def get_title(self):
        return self.driver.title

    def get_attribute(self, by, path, attributeValue):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        return ele.get_attribute(attributeValue)

    def get_current_time(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def get_css_property_value(self, by, path, css_property):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, path)))
        rgb = ele.value_of_css_property(css_property)
        return Color.from_string(rgb).hex

    def get_random_digit(self):
        res = ''.join(random.choices(string.digits, k=4))
        return res

    def accept_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to_alert()
        alert.dismiss()
