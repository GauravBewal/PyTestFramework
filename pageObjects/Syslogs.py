from selenium.webdriver.common.by import By


class Syslogs:

    def __init__(self, driver):
        self.driver = driver

    tab_SysLogs = (By.XPATH, "//p[contains(text(),'Syslogs')]/parent::div/parent::div")

    def click_SysLogs(self):
        return self.driver.find_element(*Syslogs.tab_SysLogs)

    btn_new_syslog = (By.XPATH, "//header//button")

    def click_new_Syslog(self):
        return self.driver.find_element(*Syslogs.btn_new_syslog)

    text_slider_heading = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_title(self):
        return self.driver.find_element(*Syslogs.text_slider_heading)

    btn_slider_close = (By.XPATH, "//div[@class='modal--header']//i")

    def click_slider_close(self):
        return self.driver.find_element(*Syslogs.btn_slider_close)

    tab_inactive = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*Syslogs.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'All')]")

    def click_All_tab(self):
        return self.driver.find_element(*Syslogs.tab_All)
