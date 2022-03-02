from selenium.webdriver.common.by import By
from utilities.Actions import Action

class Syslogs(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_SysLogs = "//p[contains(text(),'Syslogs')]/parent::div/parent::div"

    def click_SysLogs(self):
        return Action.waitandclick(self, By.XPATH, Syslogs.tab_SysLogs)

    btn_new_syslog = "//header//button"

    def click_new_Syslog(self):
        return Action.waitandclick(self, By.XPATH, Syslogs.btn_new_syslog)

    text_slider_heading = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, Syslogs.text_slider_heading)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, Syslogs.btn_slider_close)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, Syslogs.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Syslogs.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, Syslogs.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Syslogs.tab_All, 'color')
