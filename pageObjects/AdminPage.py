from selenium.webdriver.common.by import By

from utilities.Actions import Action


class Admin(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_Configuration = "//p[contains(text(),'Configuration')]/parent::div/parent::div"

    def click_configuration(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_Configuration)

    tab_Authentication = "//p[contains(text(),'Authentication')]/parent::div/parent::div"

    def click_authentication(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_Authentication)

    tab_License_Management = "//p[contains(text(),'License Management')]/parent::div/parent::div"

    def click_license_management(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_License_Management)

    tab_Cyware_Agent = "//p[contains(text(),'Cyware Agent')]/parent::div/parent::div"

    def click_cyware_agent(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_Cyware_Agent)

    tab_Console_Status = "//p[contains(text(),'Console Status')]/parent::div/parent::div"

    def click_console_status(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_Console_Status)

    tab_Playbook_tags = "//p[contains(text(),'Playbook Tags')]/parent::div/parent::div"

    def click_playbook_tags(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_Playbook_tags)

    tab_elastic_search = "//div[contains(text(),'Elasticsearch')]"

    def click_elastic_search(self):
        return Action.javascript_click(self, By.XPATH, Admin.tab_elastic_search)

    btn_back_admin = "//div[@class='d-flex align-items-center mr-3 el-col el-col-4']/div"

    def click_back_button(self):
        return Action.javascript_click(self, By.XPATH, Admin.btn_back_admin)

    btn_licence_update_button = "//button/span[contains(text(),'Update')]"

    def click_licence_update_button(self):
        return Action.javascript_click(self, By.XPATH, Admin.btn_licence_update_button)

    text_licence_field = "//div[@class='cs-lincese bg-n10']//input"

    def licence_key_field(self, value):
        return Action.get_attribute(self, By.XPATH, Admin.text_licence_field, value)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, Admin.close_walkthrough_tooltip)
