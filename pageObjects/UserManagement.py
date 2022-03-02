from selenium.webdriver.common.by import By
from utilities.Actions import Action


class UserManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_User_Management = "//p[contains(text(),'User Management')]/parent::div/parent::div"

    def click_User_Management(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.tab_User_Management)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, UserManagement.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, UserManagement.tab_All, 'color')

    btn_new_user = "//header//div[3]/button"

    def click_add_user(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.btn_new_user)

    btn_export_user = "//header//div[@class='el-dropdown']/button"

    def click_export(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.btn_export_user)

    drpdwn_export_option = "//li[text()='CSV']"

    def export_option_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, UserManagement.drpdwn_export_option)

    text_slider_title = "//div[text()='User']"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, UserManagement.text_slider_title)

    btn_slider_close = "//div[text()='User']/../following-sibling::div/span[2]"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, UserManagement.btn_slider_close)
