from selenium.webdriver.common.by import By


class OpenApi:

    def __init__(self, driver):
        self.driver = driver

    tab_Open_API = (By.XPATH, "//div[@class='admin-components__list']//div[8]")

    def click_Open_API_tab(self):
        return self.driver.find_element(*OpenApi.tab_Open_API)

    btn_new_open_api = (By.XPATH, "//button[contains(@aria-describedby,'el-tooltip')]")

    def click_new_open_api(self):
        return self.driver.find_element(*OpenApi.btn_new_open_api)

    text_slider_title = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_title(self):
        return self.driver.find_element(*OpenApi.text_slider_title)

    btn_slider_close = (By.XPATH, "//div[@class='modal--header']//i")

    def click_slider_close(self):
        return self.driver.find_element(*OpenApi.btn_slider_close)

    tab_inactive = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*OpenApi.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'All')]")

    def click_All_tab(self):
        return self.driver.find_element(*OpenApi.tab_All)
