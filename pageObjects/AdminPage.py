from selenium.webdriver.common.by import By

from utilities.Actions import Action


class Admin(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    tab_Configuration = "//p[contains(text(),'Configuration')]/parent::div/parent::div"

    def click_configuration(self):
        """
            Click on Configuration under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_Configuration)

    tab_Authentication = "//p[contains(text(),'Authentication')]/parent::div/parent::div"

    def click_authentication(self):
        """
            Click on Authentication under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_Authentication)

    tab_License_Management = "//p[contains(text(),'License Management')]/parent::div/parent::div"

    def click_license_management(self):
        """
            Click on License Management under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_License_Management)

    tab_Cyware_Agent = "//p[contains(text(),'Cyware Agent')]/parent::div/parent::div"

    def click_cyware_agent(self):
        """
            Click on Cyware Agent under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_Cyware_Agent)

    tab_Console_Status = "//p[contains(text(),'Console Status')]/parent::div/parent::div"

    def click_console_status(self):
        """
            Click on Console Status under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_Console_Status)

    tab_Playbook_tags = "//p[contains(text(),'Playbook Tags')]/parent::div/parent::div"

    def click_playbook_tags(self):
        """
            Click on Playbook Tags under Admin Panel
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.tab_Playbook_tags)

    btn_back_admin = "//div[@class='d-flex align-items-center mr-3 el-col el-col-4']/div"

    def click_back_button(self):
        """
             Click on back button under Admin Panel for return back on admin section.
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Admin.btn_back_admin)
