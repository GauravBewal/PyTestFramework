from selenium.webdriver.common.by import By
from utilities.Actions import Action

class DataSync(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_run_history = "//span[@class='tab__count']/parent::a[@href='/soar/data-sync/list/logs']"

    def click_run_history(self):
        return Action.waitandclick(self, By.XPATH, DataSync.tab_run_history)

    btn_create_data_sync = "//header//button/i"

    def click_create_data_sync(self):
        return Action.waitandclick(self, By.XPATH, DataSync.btn_create_data_sync)

    page_heading_text = "//header//h1"

    def get_page_heading_text(self):
        return Action.getText(self, By.XPATH, DataSync.page_heading_text)

    tab_job_details = "//span[@class='tab__count']/parent::a[@href='/soar/data-sync/list/jobs']"

    def click_job_details(self):
        return Action.waitandclick(self, By.XPATH, DataSync.tab_job_details)

    button_back_to_home = "//div[contains(@class,'back-button')]/i"

    def click_back_button(self):
        return Action.waitandclick(self, By.XPATH, DataSync.button_back_to_home)

    button_confirm_close = "//button[contains(text(),'Close without Saving')]"

    def click_confirm_close(self):
        return Action.waitandclick(self, By.XPATH, DataSync.button_confirm_close)

    datasync_filter_btn = "//div[@class='filters-view']//button"

    def click_on_filter_btn(self):
        return Action.waitandclick(self, By.XPATH, DataSync.datasync_filter_btn)

    filter_slider_title = "//span[@class='filters__header__label']"

    def get_filter_slider_title(self):
        return Action.getText(self, By.XPATH, DataSync.filter_slider_title)
