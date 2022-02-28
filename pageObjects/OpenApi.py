from selenium.webdriver.common.by import By
from utilities.Actions import Action

class OpenApi(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_Open_API = "//p[contains(text(),'Open API')]/parent::div/parent::div"

    def click_Open_API_tab(self):
        return Action.waitandclick(self, By.XPATH, OpenApi.tab_Open_API)


    btn_new_open_api = "//button[contains(@aria-describedby,'el-tooltip')]"

    def click_new_open_api(self):
        return Action.waitandclick(self, By.XPATH, OpenApi.btn_new_open_api)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, OpenApi.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, OpenApi.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, OpenApi.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, OpenApi.tab_inactive)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, OpenApi.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, OpenApi.tab_All)
