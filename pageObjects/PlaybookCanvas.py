from selenium.webdriver.common.by import By


class PlaybookCanvas:

    def __init__(self, driver):
        self.driver = driver

    tab_cyware_playbooks = (By.XPATH, "(//div[@slot='header']//a)[2]")

    def cyware_playbook_tab(self):
        return self.driver.find_element(*PlaybookCanvas.tab_cyware_playbooks)
