import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class FilterandSort(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_filter = "//i[contains(@class,'icon-filter')]/parent::button"

    def click_on_filter_btn(self):
        """
            Click on filter button
        """
        return Action.wait_and_click(self, By.XPATH, FilterandSort.button_filter)

    button_sort = "//span[@class='sort-tab']"

    def click_on_sort(self):
        """
            Click on sort button
        """
        return Action.wait_and_click(self, By.XPATH, FilterandSort.button_filter)

    sort_position = "//span[@class='sort-tab']/div"

    def mouse_hover_on_sort(self):
        """
            Mouse hover on to sort button
        """
        return Action.mouse_hover_on_element(self, By.XPATH, FilterandSort.sort_position)

    def get_name_sorted_filter(self):
        """
            Get the list of the sorted filter name
        """
        return Action.get_text(self, By.XPATH, FilterandSort.sort_position)

    created_sort = "//body/ul/li[2]"

    def click_on_created(self):
        """
            Click on to Created sort option
        """
        return Action.javascript_click(self, By.XPATH, FilterandSort.created_sort)

    sort_order = "//span[@class='sort-tab']//span[@class='el-tooltip sort-button']"

    def changing_sort_to_descending_order(self):
        """
            Click on to descending order button for sort
        """
        return Action.wait_and_click(self, By.XPATH, FilterandSort.sort_order)

    filter_close_btn = "//i[contains(@class,'cyicon-cross')]/parent::span"

    def click_close_filter_btn(self):
        """
            Click on filter close button
        """
        return Action.wait_and_click(self, By.XPATH, FilterandSort.filter_close_btn)

    playbook_filter_title = "//span[@class='filters__header__label']"

    def get_filters_slider_title(self):
        """
            Get the title of filter slider window
        """
        return Action.get_text(self, By.XPATH, FilterandSort.playbook_filter_title)

    last_week = "(//div[contains(@class,'cy-radio__btn--default')]//div)[1]"

    def select_last_week_filter(self):
        """
            Select radio button for last week on filter slider
        """
        return Action.javascript_click(self, By.XPATH, FilterandSort.last_week)

    input_status = "(//div[contains(@class,'cy-radio__btn--default')]//div//input)[1]"

    def check_last_week_radio_status(self):
        """
            Check last week radio button is selected or not
        """
        time.sleep(ReadConfig.Wait_6_Sec())
        return Action.check_status(self, By.XPATH, FilterandSort.input_status)

    last_month = "(//div[contains(@class,'cy-radio__btn--default')]//div)[3]"

    def select_last_month_filter(self):
        """
            Select radio button for last month on filter slider
        """
        return Action.javascript_click(self, By.XPATH, FilterandSort.last_month)

    last_month_input = "(//div[contains(@class,'cy-radio__btn--default')]//div//input)[2]"

    def check_last_month_radio_status(self):
        """
            Check last month radio button is selected or not
        """
        time.sleep(ReadConfig.Wait_6_Sec())
        return Action.check_status(self, By.XPATH, FilterandSort.last_month_input)


class Tooltip(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    close_tooltip_btn = "//div[contains(@class,'notification__closeBtn')]"

    def click_close_tooltip(self):
        """
            Close tooltip pop-up
        """
        return Action.wait_and_click(self, By.XPATH, Tooltip.close_tooltip_btn)

    toast_msg_txt = "//div[@role='alert']//span[2]/span[1]"

    def get_tooltip_msg(self):
        """
            Get the tooltip message otherwise return No message found
        """
        if self.visibility_of_tooltip() is True:
            time.sleep(2)
            return Action.get_text(self, By.XPATH, Tooltip.toast_msg_txt)


    tooltip_div = "//body//div[contains(@class,'cy-notification')]"

    def visibility_of_tooltip(self):
        """
            Check visibility of the tooltip
        """
        return Action.check_visibility_of_element(self, By.XPATH, Tooltip.tooltip_div)

    spinner_on_btn = "//div[contains(@class,'cyicon-spinner')]"

    def invisibility_of_spinner(self):
        return Action.Webdriver_Wait_until_invisibility_of_element(self, By.XPATH, Tooltip.spinner_on_btn)
