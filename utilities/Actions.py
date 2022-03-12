import random
import string
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
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

    def javascript_click(self, by, path):
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, path)
            self.driver.execute_script("arguments[0].click();", element)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.javascript_click(by, path)

    def wait_and_click(self, by, path):
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, path)
            element.click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.wait_and_click(by, path)

    def normal_click(self, by, path):
        try:
            self.driver.find_element(by, path).click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.normal_click(by, path)

    def click_if_element_found(self, by, path):
        log = self.getlogger()
        try:
            self.Webdriver_Wait_until_element_clickable(by, path).click()
        except (NoSuchElementException, TimeoutException):
            log.info("Automatic walk through was not initiated. Hence passing this testcase")
            pass

    def Apply_Pagination_if_element_not_found(self, by, element_path, pagination_path):
        try:
            element = self.Webdriver_Wait_until_element_visible(by, element_path)
            self.scroll_to_element_view(element)
        except (NoSuchElementException, TimeoutException):
            self.Webdriver_Wait_until_element_clickable(by, pagination_path).click()
            self.Apply_Pagination_if_element_not_found(by, element_path, pagination_path)

    def get_no_of_elements_present(self, by, path):
        elements = self.driver.find_elements(by, path)
        return len(elements)

    def scroll_to_element_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

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
        ele = self.Webdriver_Wait_until_element_visible(by, path)
        hover = ActionChains(self.driver).move_to_element(ele)
        hover.perform()

    def get_app_version_id(self, version):
        return str(version.split(': ')[1])

    def get_count_from_string(self, by, path):
        ele = self.Webdriver_Wait_until_element_clickable(by, path)
        count = ele.text
        return int(float(count.split('(')[1].split(')')[0]))

    def get_no_of_walkthrough_and_pagination_count(self, by, path):
        element = self.Webdriver_Wait_until_element_visible(by, path)
        count = element.text.split(' ')[2]
        return int(count)

    def get_current_page_number(self, by, path):
        element = self.Webdriver_Wait_until_element_visible(by, path)
        count = element.text
        return int(count.split(' ')[0])

    def send_keys(self, by, path, value):
        element = self.Webdriver_Wait_until_element_visible(by, path)
        element.send_keys(value)

    def clear_field(self, by, path):
        element = self.driver.find_element(by, path)
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def click_enter(self):
        action1 = ActionChains(self.driver)
        action1.send_keys(Keys.ENTER)
        action1.perform()

    def drag_and_drop_element_by_target(self, by, source_path, target_path):
        source = self.Webdriver_Wait_until_element_visible(by, source_path)
        target = self.Webdriver_Wait_until_element_visible(by, target_path)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def drag_and_drop_by_offset(self, by, source_path, width, height):
        source = self.Webdriver_Wait_until_element_visible(by, source_path)
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(width, height).release().perform()

    def click_and_hold_and_release_element(self, by, source_path, destination_path):
        try:
            source = self.Webdriver_Wait_until_element_visible(by, source_path)
            destination = self.Webdriver_Wait_until_element_visible(by, destination_path)
            action = ActionChains(self.driver)
            action.click_and_hold(source).move_to_element(destination).release(source).perform()
        except StaleElementReferenceException:
            self.click_and_hold_and_release_element(by, source_path, destination_path)

    def Webdriver_Wait_until_element_visible(self, by, path):
        try:
            element = WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((by, path)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not visible with locator" + path)

    def Webdriver_Wait_until_element_clickable(self, by, path):
        try:
            element = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((by, path)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not found/clickable with locator" + path)

    def check_visibility_of_element(self, by, path):
        try:
            ele = self.Webdriver_Wait_until_element_visible(by, path)
            if ele.is_displayed():
                return True
        except (NoSuchElementException, TimeoutException):
            return False

    def check_app_is_installed_or_not(self, by, installed_path, install_btn_path, slider_install_btn_path):
        try:
            self.Webdriver_Wait_until_element_visible(by, installed_path)
        except(NoSuchElementException, TimeoutException):
            self.Webdriver_Wait_until_element_clickable(by, install_btn_path).click()
            self.Webdriver_Wait_until_element_clickable(by, slider_install_btn_path).click()

    def select_from_drop_down(self, dropdown, value):
        ddelement = Select(dropdown)
        ddelement.select_by_value(value)

    def get_text(self, by, path):
        ele = self.Webdriver_Wait_until_element_visible(by, path)
        return ele.text

    def read_search_result(self, by, path, value):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.text_to_be_present_in_element((by, path), value))
        if ele is True:
            return self.driver.find_element(by, path).text

    def get_title(self):
        return self.driver.title

    def get_attribute(self, by, path, attribute_value):
        ele = self.Webdriver_Wait_until_element_visible(by, path)
        return ele.get_attribute(attribute_value)

    def get_current_time(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def get_css_property_value(self, by, path, css_property):
        ele = self.Webdriver_Wait_until_element_visible(by, path)
        rgb = ele.value_of_css_property(css_property)
        return Color.from_string(rgb).hex

    def get_html_attribute_value(self, by, path, attribute_name):
        element = self.Webdriver_Wait_until_element_visible(by, path)
        return element.get_attribute(attribute_name)

    def convert_12to24hrs_time_format(self, time):
        return datetime.strptime(time, '%b %d, %Y, %I:%M %p')

    def convert_string_to_lower(self, string):
        return string.lower()

    def get_random_digit(self):
        res = ''.join(random.choices(string.digits, k=4))
        return res

    def accept_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to_alert()
        alert.dismiss()
