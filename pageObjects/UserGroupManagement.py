from selenium.webdriver.common.by import By
from utilities.Actions import Action


class UserGroupManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_user_group_management = "//p[contains(text(),'User Group')]/parent::div/parent::div"

    def click_user_group_management(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.tab_user_group_management)

    tab_inactive = "//div[@class='px-2 tabs--list my-2']//li[3]/a"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_inactive, 'color')

    tab_all = "//div[@class='px-2 tabs--list my-2']//li[3]/a"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.tab_all)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_all, 'color')

    btn_add_user_group = "//header//button"

    def click_add_user_group(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_add_user_group)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_slider_close)
