from selenium.webdriver.common.by import By


class Playbooks:
    tab_custom_playbooks = (By.XPATH, "//a[@href='/soar/playbook/list/custom' and @class='active']")
    tab_cyware_playbooks = (By.XPATH, "//a[@href='/soar/playbook/list/system']")

    def __init__(self, driver):
        self.driver = driver

    def cyware_app_tab(self):
        return self.driver.find_element(*Playbooks.tab_cyware_playbooks)

    def custom_app_tab(self):
        return self.driver.find_element(*Playbooks.tab_custom_playbooks)
