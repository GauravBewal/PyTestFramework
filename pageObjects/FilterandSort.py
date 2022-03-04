from selenium.webdriver.common.by import By

from utilities.Actions import Action


class FilterAndSort(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_filter = "//div[@class='header__top--left d-flex flex-fill']/button"

    def click_on_filters(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.button_filter)

    button_sort = "//span[@class='sort-tab']"

    def click_on_sort(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.button_filter)
