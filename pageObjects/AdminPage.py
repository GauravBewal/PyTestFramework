from selenium.webdriver.common.by import By


class Admin:

    def __init__(self, driver):
        self.driver = driver

    tab_Configuration = (By.XPATH, "//div[@class='admin-components__list']//div[1]")

    def click_Configuration(self):
        return self.driver.find_element(*Admin.tab_Configuration)

    tab_Authentication = (By.XPATH, "//div[@class='admin-components__list']//div[2]")

    def click_Authentication(self):
        return self.driver.find_element(*Admin.tab_Authentication)

    tab_License_Management = (By.XPATH, "//div[@class='admin-components__list']//div[3]")

    def click_License_Management(self):
        return self.driver.find_element(*Admin.tab_License_Management)

    tab_Tenant_Management = (By.XPATH, "//div[@class='admin-components__list']//div[4]")

    def click_Tenant_Management(self):
        return self.driver.find_element(*Admin.tab_Tenant_Management)

    tab_User_Management = (By.XPATH, "//div[@class='admin-components__list']//div[5]")

    def click_User_Management(self):
        return self.driver.find_element(*Admin.tab_User_Management)

    tab_User_Group_Management = (By.XPATH, "//div[@class='admin-components__list']//div[6]")

    def click_User_Group_Management(self):
        return self.driver.find_element(*Admin.tab_User_Group_Management)

    tab_Cyware_Agent = (By.XPATH, "//div[@class='admin-components__list']//div[7]")

    def click_Cyware_Agent(self):
        return self.driver.find_element(*Admin.tab_Cyware_Agent)

    tab_Open_API = (By.XPATH, "//div[@class='admin-components__list']//div[8]")

    def click_Open_API(self):
        return self.driver.find_element(*Admin.tab_Open_API)

    tab_Webhooks = (By.XPATH, "//div[@class='admin-components__list']//div[9]")

    def click_Webhooks(self):
        return self.driver.find_element(*Admin.tab_Webhooks)

    tab_SysLogs = (By.XPATH, "//div[@class='admin-components__list']//div[10]")

    def click_SysLogs(self):
        return self.driver.find_element(*Admin.tab_SysLogs)

    tab_Console_Status = (By.XPATH, "//div[@class='admin-components__list']//div[11]")

    def click_Console_Status(self):
        return self.driver.find_element(*Admin.tab_Console_Status)

    tab_Playbook_tags = (By.XPATH, "//div[@class='admin-components__list']//div[12]")

    def click_Playbook_tags(self):
        return self.driver.find_element(*Admin.tab_Playbook_tags)

    btn_back_admin = (By.XPATH, "//div[@class='d-flex align-items-center mr-3 el-col el-col-4']/div")

    def click_Back_Button(self):
        return self.driver.find_element(*Admin.btn_back_admin)
