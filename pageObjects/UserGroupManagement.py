from selenium.webdriver.common.by import By
from utilities.Actions import Action

class UserGroupManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_User_Group_Management = "//p[contains(text(),'User Group')]/parent::div/parent::div"

    def click_User_Group_Management(self):
        return Action.waitandclick(self, By.XPATH, UserGroupManagement.tab_User_Group_Management)

    tab_inactive = "//div[@class='px-2 tabs--list my-2']//li[3]/a"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, UserGroupManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, UserGroupManagement.tab_inactive)

    tab_All = "//div[@class='px-2 tabs--list my-2']//li[3]/a"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, UserGroupManagement.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, UserGroupManagement.tab_All)

    btn_add_user_group = "//header//button"

    def click_add_user_group(self):
        return Action.waitandclick(self, By.XPATH, UserGroupManagement.btn_add_user_group)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.getText(self, By.XPATH, UserGroupManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.waitandclick(self, By.XPATH, UserGroupManagement.btn_slider_close)
