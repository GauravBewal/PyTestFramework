from selenium.webdriver.common.by import By

from utilities.Actions import Action


class Runlogs(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    runlog_filter_btn = "//div[@class='filters-view']//button"

    def click_on_filter_btn(self):
        """
            Click on filter button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Runlogs.runlog_filter_btn)

    filter_slider_title = "//span[@class='filters__header__label']"

    def get_filter_slider_title(self):
        """
            Get Slider title of filter
            :return:
        """
        return Action.get_text(self, By.XPATH, Runlogs.filter_slider_title)

    def verify_playbook_visibility_in_runlog(self, playbook_name):
        """
            Verify playbook visibility in runlogs
            :param playbook_name:
            :return:
        """
        path = "//h3[contains(text(),'" + playbook_name + "')]"
        return Action.check_visibility_of_element(self, By.XPATH, path)
