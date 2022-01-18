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

    tab_Cyware_Agent = (By.XPATH, "//div[@class='admin-components__list']//div[7]")

    def click_Cyware_Agent(self):
        return self.driver.find_element(*Admin.tab_Cyware_Agent)

    tab_Console_Status = (By.XPATH, "//div[@class='admin-components__list']//div[11]")

    def click_Console_Status(self):
        return self.driver.find_element(*Admin.tab_Console_Status)

    tab_Playbook_tags = (By.XPATH, "//div[@class='admin-components__list']//div[12]")

    def click_Playbook_tags(self):
        return self.driver.find_element(*Admin.tab_Playbook_tags)

    tab_elastic_search = (By.XPATH, "//div[contains(text(),'Elasticsearch')]")

    def click_elasticsearch(self):
        return self.driver.find_element(*Admin.tab_elastic_search)

    btn_back_admin = (By.XPATH, "//div[@class='d-flex align-items-center mr-3 el-col el-col-4']/div")

    def click_Back_Button(self):
        return self.driver.find_element(*Admin.btn_back_admin)

    btn_licence_update_button = (By.XPATH, "//button/span[contains(text(),'Update')]")

    def click_licence_update_button(self):
        return self.driver.find_element(*Admin.btn_licence_update_button)

    text_licence_field = (By.XPATH, "//div[@class='cs-lincese bg-n10']//input")

    def field_licence_key(self):
        return self.driver.find_element(*Admin.text_licence_field)
