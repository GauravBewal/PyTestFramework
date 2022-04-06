from selenium.webdriver.common.by import By

from utilities.Actions import Action

class Pagination(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    increment_pagination_btn = "//div[contains(@class,'footer-box')]//button[@class='btn-next']"

    def click_on_increment_pagination_btn(self):
        """
            Click on increment pagination button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Pagination.increment_pagination_btn)

    decrement_pagination_btn = "//div[contains(@class,'footer-box')]//button[@class='btn-prev']"

    def click_on_decrement_pagination_btn(self):
        """
            Click on decrement pagination button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Pagination.decrement_pagination_btn)
