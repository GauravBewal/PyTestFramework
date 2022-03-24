import glob
import json
import os
import random
import string
import time
from datetime import datetime

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
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

    def javascript_click(self, by, locator):
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, locator)
            self.driver.execute_script("arguments[0].click();", element)
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.javascript_click(by, locator)

    def get_tab_total_count(self, by, locator, previous_tab_count):
        count = self.get_count_from_string(by, locator)
        if count != previous_tab_count:
            return count
        else:
            self.get_tab_total_count(by, locator, previous_tab_count)




    def wait_and_click(self, by, locator):
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, locator)
            element.click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.wait_and_click(by, locator)

    def normal_click(self, by, locator):
        try:
            self.driver.find_element(by, locator).click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.normal_click(by, locator)

    def click_if_element_found(self, by, locator):
        log = self.getlogger()
        try:
            element = self.Webdriver_Wait_until_element_visible(by, locator)
            element.click()
        except (NoSuchElementException, TimeoutException):
            log.info("Automatic walk through was not initiated. Hence passing this testcase")
            pass

    def Pass_even_element_not_visible(self, by, locator):
        try:
            element = self.Webdriver_Wait_until_element_visible(by, locator)
            if element.is_displayed():
                return True
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return True


    def Apply_Pagination_if_element_not_found(self, by, locator, pagination_path):
        try:
            element = self.Webdriver_Wait_until_element_visible(by, locator)
            self.scroll_to_element_view(element)
        except (NoSuchElementException, TimeoutException):
            self.Webdriver_Wait_until_element_clickable(by, pagination_path).click()
            self.Apply_Pagination_if_element_not_found(by, locator, pagination_path)

    def get_no_of_elements_present(self, by, locator):
        elements = self.driver.find_elements(by, locator)
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

    def mouse_hover_on_element(self, by, locator):
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        hover = ActionChains(self.driver).move_to_element(ele)
        hover.perform()

    def get_app_version_id(self, version):
        return str(version.split(': ')[1])

    def get_count_from_string(self, by, locator):
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        count = ele.text
        return int(float(count.split('(')[1].split(')')[0]))

    def get_no_of_walkthrough_and_pagination_count(self, by, locator):
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        count = element.text.split(' ')[2]
        return int(count)

    def check_file_downloaded_and_get_file_name(self, file_name, file_type):
        time.sleep(10)
        files_list = glob.glob('**/*' + file_name + '*.' + file_type + '', recursive=True)
        downloaded_file_name = str(files_list[0])
        return downloaded_file_name

    def get_file_downloaded_path(self, file_name):
        return os.path.abspath(file_name)

    def delete_downloaded_file(self, downloaded_app_path):
        if os.path.isfile(downloaded_app_path):
            os.remove(downloaded_app_path)
        else:
            raise ValueError("File Not found".format(downloaded_app_path))

    def get_current_page_number(self, by, locator):
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        count = element.text
        return int(count.split(' ')[0])

    def send_keys(self, by, locator, value):
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        element.send_keys(value)

    def send_keys_to_hidden_upload_element(self, by, locator, file_path):
        ele = self.driver.find_element(by, locator)
        ele.send_keys(file_path)

    def clear_field(self, by, locator):
        element = self.driver.find_element(by, locator)
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

    def Webdriver_Wait_until_element_visible(self, by, locator):
        try:
            element = WebDriverWait(self.driver, timeout=20).until(EC.visibility_of_element_located((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not visible with locator" + locator)

    def Webdriver_Wait_until_element_clickable(self, by, locator):
        try:
            element = WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not found/clickable with locator" + locator)

    def check_visibility_of_element(self, by, locator):
        try:
            ele = self.Webdriver_Wait_until_element_visible(by, locator)
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

    def select_from_drop_down(self, by, path, value):
        ddelement = Select(self.driver.find_element(by, path))
        ddelement.select_by_value(value)

    def get_text(self, by, locator):
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        return ele.text

    def read_search_result(self, by, locator, value):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.text_to_be_present_in_element((by, locator), value))
        if ele is True:
            return self.driver.find_element(by, locator).text

    def get_title(self):
        return self.driver.title

    def get_attribute(self, by, locator, attribute_value):
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        return ele.get_attribute(attribute_value)

    def get_current_time(self):
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def get_css_property_value(self, by, locator, css_property):
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        rgb = ele.value_of_css_property(css_property)
        return Color.from_string(rgb).hex

    def get_html_attribute_value(self, by, locator, attribute_name):
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        return element.get_attribute(attribute_name)

    def convert_12to24hrs_time_format(self, time):
        converted_time = datetime.strptime(time, '%b %d, %Y, %I:%M %p')
        return converted_time

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

    def check_status(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele.is_selected()

    def convert_json_to_txt(self, json_data):
        return json.dumps(json_data)
