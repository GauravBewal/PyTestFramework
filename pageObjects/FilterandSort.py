import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class FilterAndSort(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_filter = "//i[@class='icon icon-filter']/parent::button"

    def click_on_filters(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.button_filter)

    button_sort = "//span[@class='sort-tab']"

    def click_on_sort(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.button_filter)

    sort_position = "//span[@class='sort-tab']/div[@class='el-dropdown']"

    def mouse_hover_on_sort(self):
        return Action.mouse_hover_on_element(self, By.XPATH, FilterAndSort.sort_position)

    def get_name_sorted_filter(self):
        return Action.get_text(self, By.XPATH, FilterAndSort.sort_position)

    created_sort = "//li[contains(text(),'Created')]"

    def click_on_created(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.created_sort)


    sort_order = "//span[@class='sort-tab']//span[@class='el-tooltip sort-button']"

    def changing_sort_to_descending_order(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.sort_order)

    filter_close_btn = "//i[contains(@class,'cyicon-cross')]/parent::span"

    def close_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.filter_close_btn)

    playbook_filter_title = "//span[@class='filters__header__label']"

    def get_filters_slider_title(self):
        return Action.get_text(self, By.XPATH, FilterAndSort.playbook_filter_title)

    last_week = "(//div[contains(@class,'cy-radio__btn--default')]//div)[1]"

    def select_last_week_filter(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.last_week)

    input_status = "(//div[contains(@class,'cy-radio__btn--default')]//div//input)[1]"

    def check_last_week_radio_status(self):
        time.sleep(ReadConfig.Wait_6_Sec())
        return Action.check_status(self, By.XPATH, FilterAndSort.input_status)

    last_month = "(//div[contains(@class,'cy-radio__btn--default')]//div)[3]"

    def select_last_month_filter(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.last_month)

    last_month_input = "(//div[contains(@class,'cy-radio__btn--default')]//div//input)[2]"

    def check_last_month_radio_status(self):
        time.sleep(ReadConfig.Wait_6_Sec())
        return Action.check_status(self, By.XPATH, FilterAndSort.last_month_input)
