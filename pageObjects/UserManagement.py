from selenium.webdriver.common.by import By


class UserManagement:

    def __init__(self, driver):
        self.driver = driver

    tab_User_Management = (By.XPATH, "//div[@class='admin-components__list']//div[5]")

    def click_User_Management(self):
        return self.driver.find_element(*UserManagement.tab_User_Management)

    tab_inactive = (By.XPATH, "//li/a[contains(text(),'Inactive')]")

    def click_inactive_tab(self):
        return self.driver.find_element(*UserManagement.tab_inactive)

    tab_All = (By.XPATH, "//li/a[contains(text(),'All')]")

    def click_All_tab(self):
        return self.driver.find_element(*UserManagement.tab_All)

    btn_new_user = (By.XPATH, "//header//div[3]/button")

    def click_add_user(self):
        return self.driver.find_element(*UserManagement.btn_new_user)

    btn_export_user = (By.XPATH, "//header//div[@class='el-dropdown']/button")

    def click_export(self):
        return self.driver.find_element(*UserManagement.btn_export_user)

    drpdwn_export_option = (By.XPATH, "//li[text()='CSV']")

    def export_option_visibility(self):
        return self.driver.find_element(*UserManagement.drpdwn_export_option)

    text_slider_title = (By.XPATH, "//div[text()='User']")

    def get_slider_title(self):
        return self.driver.find_element(*UserManagement.text_slider_title)

    btn_slider_close = (By.XPATH, "//div[text()='User']/../following-sibling::div/span[2]")

    def click_slider_close(self):
        return self.driver.find_element(*UserManagement.btn_slider_close)
