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

    global count
    count = 0

    def javascript_click(self, by, locator):
        """
            Click on element by java scrpit Executor
            :param by: Type of locator
            :param locator: locator
            :return:
        """
        global count
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, locator)
            self.driver.execute_script("arguments[0].click();", element)
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException) as e:
            if count < 4:
                count += 1
                self.javascript_click(by, locator)
            else:
                raise e

    def wait_and_click(self, by, locator):
        """
            Click on element by checking element is clickable or not
            :param by:
            :param locator:
            :return:
        """
        global count
        try:
            element = self.Webdriver_Wait_until_element_clickable(by, locator)
            element.click()
        except (StaleElementReferenceException, ElementClickInterceptedException) as e:
            if count < 4:
                count += 1
                self.wait_and_click(by, locator)
            else:
                raise e

    def click_if_element_found(self, by, locator):
        """
            Click on element after checking visibility of element
            :param by: type of locator
            :param locator: locator
            :return:
        """
        log = self.getlogger()
        try:
            element = self.Webdriver_Wait_until_element_visible(by, locator)
            element.click()
        except (NoSuchElementException, TimeoutException):
            log.info("Walkthrough/Element not found. Hence passing this testcase")
            pass

    def Pass_even_element_not_visible(self, by, locator):
        """
            No action when element is displayed
            :param by:
            :param locator:
            :return:
        """
        try:
            element = self.Webdriver_Wait_until_element_visible(by, locator)
            if element.is_displayed():
                return True
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            return True

    def Apply_Pagination_if_element_not_found(self, by, locator, pagination_path):
        try:
            self.Webdriver_Wait_until_element_visible(by, locator)
            self.scroll_to_element_view(by, locator)
        except (NoSuchElementException, TimeoutException):
            self.Webdriver_Wait_until_element_clickable(by, pagination_path).click()
            self.Apply_Pagination_if_element_not_found(by, locator, pagination_path)

    def get_no_of_elements_present(self, by, locator):
        """
            Get the number of the elements present on page
            :param by:
            :param locator:
            :return:
        """
        elements = self.driver.find_elements(by, locator)
        return len(elements)

    def scroll_to_element_view(self, by, locator):
        """
            Scroll on window until element view
            :param by:
            :param locator:
            :return:
        """
        element = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_new_tab(self):
        """
            Switch new opened tab from main tab
            :return:
        """
        # keeping 5 secs sleep to wait until new tab is opened
        time.sleep(5)
        all_windows = self.driver.window_handles
        parent_window = all_windows[0]
        child_window = all_windows[1]
        self.driver.switch_to.window(child_window)
        return parent_window

    def switch_back_parent_window(self, parent_window):
        """
            Switch back to parent window
            :param parent_window:
            :return:
        """
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        time.sleep(5)

    def mouse_hover_on_element(self, by, locator):
        """
            Mouse hover on element
            :param by:
            :param locator:
            :return:
        """
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        hover = ActionChains(self.driver).move_to_element(ele)
        hover.perform()

    def get_app_version_id(self, version):
        """
            Get app Version ID
            :param version:
            :return:
        """
        return str(version.split(': ')[1])

    def get_count_from_string(self, by, locator):
        """
            Get count of character from String
            :param by:
            :param locator:
            :return:
        """
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        count = ele.text
        return int(float(count.split('(')[1].split(')')[0]))

    def get_no_of_walkthrough_and_pagination_count(self, by, locator):
        """
            Get number of walk through and pagination count
            :param by:
            :param locator:
            :return:
        """
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        count = element.text.split(' ')[2]
        return int(count)

    def check_file_downloaded_and_get_file_directory_path(self, file_name, file_type):
        """
            Check file downloaded and get file directory path
            :param file_name:
            :param file_type:
            :return:
        """
        time.sleep(10)
        files_list = glob.glob('**/*' + file_name + '*.' + file_type + '', recursive=True)
        return str(files_list[0])

    def get_file_downloaded_path(self, app_dir_path):
        """
            Get the path of the downloaded path
            :param app_dir_path:
            :return:
        """
        return os.path.abspath(app_dir_path)

    def delete_downloaded_file(self, downloaded_app_path):
        """
            Delete downloaded file from provided path
            :param downloaded_app_path:
            :return:
        """
        if os.path.isfile(downloaded_app_path):
            os.remove(downloaded_app_path)
        else:
            raise ValueError("File Not found".format(downloaded_app_path))

    def get_current_page_number(self, by, locator):
        """
            Get current page number
            :param by:
            :param locator:
            :return:
        """
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        count = element.text
        return int(count.split(' ')[0])

    def send_keys(self, by, locator, value):
        """
            Sendkey method
            :param by:
            :param locator:
            :param value:
            :return:
        """
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        element.send_keys(value)

    def send_keys_to_hidden_upload_element(self, by, locator, file_path):
        """
            Send Keys for upload in hidden elements
            :param by:
            :param locator:
            :param file_path:
            :return:
        """
        ele = self.driver.find_element(by, locator)
        ele.send_keys(file_path)

    def clear_field(self, by, locator):
        """
            Clear text field
            :param by:
            :param locator:
            :return:
        """
        element = self.driver.find_element(by, locator)
        while len(element.get_attribute("value")) > 0:
            element.send_keys(Keys.BACK_SPACE)

    def Press_enter(self):
        """
            Click enter
            :return:
        """
        action1 = ActionChains(self.driver)
        action1.send_keys(Keys.ENTER)
        action1.perform()

    def drag_and_drop_element_by_target(self, by, source_path, target_path):
        """
            Drag and drop element by source to destination
            :param by:
            :param source_path:
            :param target_path:
            :return:
        """
        source = self.Webdriver_Wait_until_element_visible(by, source_path)
        target = self.Webdriver_Wait_until_element_visible(by, target_path)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def drag_and_drop_by_offset(self, by, source_path, width, height):
        """
            Drag and grop by offset
            :param by:
            :param source_path:
            :param width:
            :param height:
            :return:
        """
        source = self.Webdriver_Wait_until_element_visible(by, source_path)
        action = ActionChains(self.driver)
        action.click_and_hold(source).move_by_offset(width, height).release().perform()

    def click_and_hold_and_release_element(self, by, source_path, destination_path):
        """
            Click on element and hold till destination and then release later on.
            :param by:
            :param source_path:
            :param destination_path:
            :return:
        """
        try:
            source = self.Webdriver_Wait_until_element_visible(by, source_path)
            destination = self.Webdriver_Wait_until_element_visible(by, destination_path)
            action = ActionChains(self.driver)
            action.click_and_hold(source).move_to_element(destination).release(source).perform()
        except StaleElementReferenceException:
            self.click_and_hold_and_release_element(by, source_path, destination_path)

    def Webdriver_Wait_until_element_visible(self, by, locator):
        """
            Explicit wait for element until element visibility verified
            :param by:
            :param locator:
            :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=30).until(EC.visibility_of_element_located((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not visible with locator" + locator)

    def Webdriver_Wait_until_invisibility_of_element(self, by, locator):
        """
            Explicit wait for element until invisibility of element
            :param by:
            :param locator:
            :return:
        """
        try:
            return WebDriverWait(self.driver, timeout=30).until(EC.invisibility_of_element_located((by, locator)))
        except (TimeoutException, StaleElementReferenceException) as e:
            raise e

    def page_refresh(self):
        """
            Page refresh
            :return:
        """
        self.driver.get(self.driver.current_url)

    def Webdriver_Wait_until_element_clickable(self, by, locator):
        """
            Explicit wait for element until element is to be clickable
            :param by:
            :param locator:
            :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout=40).until(EC.element_to_be_clickable((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException("Element not found/clickable with locator" + locator)

    def check_visibility_of_element(self, by, locator):
        """
            Check visibility of element
            :param by:
            :param locator:
            :return:
        """
        try:
            ele = self.Webdriver_Wait_until_element_visible(by, locator)
            return ele.is_displayed()
        except StaleElementReferenceException:
            self.check_visibility_of_element(by, locator)
        except (NoSuchElementException, TimeoutException):
            return False

    def check_app_is_installed_or_not(self, by, installed_path, install_btn_path, slider_install_btn_path):
        """
            Check app is installed or not
            :param by:
            :param installed_path:
            :param install_btn_path:
            :param slider_install_btn_path:
            :return:
        """
        try:
            self.Webdriver_Wait_until_element_visible(by, installed_path)
        except(NoSuchElementException, TimeoutException):
            self.Webdriver_Wait_until_element_clickable(by, install_btn_path).click()
            self.Webdriver_Wait_until_element_clickable(by, slider_install_btn_path).click()

    def select_from_drop_down(self, by, path, value):
        """
            Select from drop-down on value
            :param by:
            :param path:
            :param value:
            :return:
        """
        ddelement = Select(self.driver.find_element(by, path))
        ddelement.select_by_value(value)

    def get_text(self, by, locator):
        """
            Get text of the element
            :param by:
            :param locator:
            :return:
        """
        global count
        try:
            ele = self.Webdriver_Wait_until_element_visible(by, locator)
            return ele.text
        except StaleElementReferenceException:
            self.get_text(by, locator)
        except (ElementClickInterceptedException, TimeoutException) as e:
            raise e

    def WaitUntil_textToBePresentInElementLocated(self, by, locator, value):
        ele = WebDriverWait(self.driver, timeout=30).until(EC.text_to_be_present_in_element((by, locator), value))
        if ele is True:
            return self.driver.find_element(by, locator).text

    def get_title(self):
        """
            Get title
            :return:
        """
        return self.driver.title

    def get_attribute(self, by, locator, attribute_value):
        """
            Get attribute
            :param by:
            :param locator:
            :param attribute_value:
            :return:
        """
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        return ele.get_attribute(attribute_value)

    def get_current_time(self):
        """
            Get current time
            :return:
        """
        return datetime.now().strftime("%B %d, %Y %H:%M:%S")

    def get_css_property_value(self, by, locator, css_property):
        """
            Get css property value
            :param by:
            :param locator:
            :param css_property:
            :return:
        """
        ele = self.Webdriver_Wait_until_element_visible(by, locator)
        rgb = ele.value_of_css_property(css_property)
        return Color.from_string(rgb).hex

    def get_html_attribute_value(self, by, locator, attribute_name):
        """
            Get html attribute value
            :param by:
            :param locator:
            :param attribute_name:
            :return:
        """
        element = self.Webdriver_Wait_until_element_visible(by, locator)
        return element.get_attribute(attribute_name)

    def convert_12to24hrs_time_format(self, time):
        """
            Convert 12-hour time format to 24-hour format
            :param time:
            :return:
        """
        converted_time = datetime.strptime(time, '%b %d, %Y, %I:%M %p')
        return converted_time

    def convert_string_to_lower(self, text_string):
        """
            Convert provided string to in lower case character
            :param string:
            :return:
        """
        return text_string.lower()

    def get_random_digit(self, no_of_digits):
        """
            Create random number with number of digits
            :param no_of_digits:
            :return:
        """
        res = ''.join(random.choices(string.digits, k=no_of_digits))
        return res

    def accept_alert(self):
        """
            Accept alert
            :return:
        """
        alert = self.driver.switch_to_alert()
        alert.accept()

    def dismiss_alert(self):
        """
            dismiss alert
            :return:
        """
        alert = self.driver.switch_to_alert()
        alert.dismiss()

    def check_status(self, by, locator):
        """
            Check whether element is selected or not
            :param by:
            :param locator:
            :return:
        """
        ele = self.driver.find_element(by, locator)
        return ele.is_selected()

    def convert_json_to_txt(self, json_data):
        """
            Convert json file to text
            :param json_data:
            :return:
        """
        return json.dumps(json_data)
