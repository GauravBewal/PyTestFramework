from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Admin(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_Configuration = "//p[contains(text(),'Configuration')]/parent::div/parent::div"

    def click_Configuration(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_Configuration)

    tab_Authentication = "//p[contains(text(),'Authentication')]/parent::div/parent::div"

    def click_Authentication(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_Authentication)

    tab_License_Management = "//p[contains(text(),'License Management')]/parent::div/parent::div"

    def click_License_Management(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_License_Management)

    tab_Cyware_Agent = "//p[contains(text(),'Cyware Agent')]/parent::div/parent::div"

    def click_Cyware_Agent(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_Cyware_Agent)

    tab_Console_Status = "//p[contains(text(),'Console Status')]/parent::div/parent::div"

    def click_Console_Status(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_Console_Status)

    tab_Playbook_tags = "//p[contains(text(),'Playbook Tags')]/parent::div/parent::div"

    def click_Playbook_tags(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_Playbook_tags)

    tab_elastic_search = "//div[contains(text(),'Elasticsearch')]"

    def click_elasticsearch(self):
        return Action.waitandclick(self, By.XPATH, Admin.tab_elastic_search)

    btn_back_admin = "//div[@class='d-flex align-items-center mr-3 el-col el-col-4']/div"

    def click_Back_Button(self):
        return Action.waitandclick(self, By.XPATH, Admin.btn_back_admin)

    btn_licence_update_button = "//button/span[contains(text(),'Update')]"

    def click_licence_update_button(self):
        return Action.waitandclick(self, By.XPATH, Admin.btn_licence_update_button)

    text_licence_field = "//div[@class='cs-lincese bg-n10']//input"

    def field_licence_key(self, value):
        return Action.getattribute(self, By.XPATH, Admin.text_licence_field, value)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.clickifelementfound(self, By.XPATH, Admin.close_walkthrough_tooltip)


