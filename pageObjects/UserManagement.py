from selenium.webdriver.common.by import By

from utilities.Actions import Action


class UserManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_user_management = "//p[contains(text(),'User Management')]/parent::div/parent::div"

    def click_user_management(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_user_management)

    user_count = "//h1[contains(text(),'User Management (')]"

    def get_user_count(self):
        return Action.get_count_from_string(self, By.XPATH, UserManagement.user_count)


    first_active_user = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_user(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_active_user)

    first_inactive_user = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_user(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_inactive_user)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_All)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_All, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.tab_active)

    btn_new_user = "//header//div[3]/button"

    def click_add_user(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_new_user)

    btn_export_user = "//header//div[@class='el-dropdown']/button"

    def click_export(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_export_user)

    drpdwn_export_option = "//li[text()='CSV']"

    def export_option_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, UserManagement.drpdwn_export_option)

    text_slider_title = "//div[text()='User']"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, UserManagement.text_slider_title)

    btn_slider_close = "//div[text()='User']/../following-sibling::div/span[2]"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_slider_close)
