from selenium.webdriver.common.by import By


class UserGroupManagement:

    def __init__(self, driver):
        self.driver = driver

    tab_User_Group_Management = (By.XPATH, "//div[@class='admin-components__list']//div[6]")

    def click_User_Group_Management(self):
        return self.driver.find_element(*UserGroupManagement.tab_User_Group_Management)

    tab_inactive_tenant = (By.XPATH, "//div[@class='px-2 tabs--list my-2']//li[3]/a")

    def click_inactive_tenant_tab(self):
        return self.driver.find_element(*UserGroupManagement.tab_inactive_tenant)

    btn_add_user_group = (By.XPATH, "//header//button")

    def click_add_user_group(self):
        return self.driver.find_element(*UserGroupManagement.btn_add_user_group)

    text_slider_title = (By.XPATH, "//div[@class='modal--header']//span")

    def get_slider_title(self):
        return self.driver.find_element(*UserGroupManagement.text_slider_title)

    btn_slider_close = (By.XPATH, "//div[@class='modal--header']//i")

    def click_slider_close(self):
        return self.driver.find_element(*UserGroupManagement.btn_slider_close)
