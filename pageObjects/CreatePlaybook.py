from selenium.webdriver.common.by import By


class CreatePlaybook:

    textbox_playbook_name = (By.XPATH, "//input[@placeholder='Enter Name']")
    textbox_playbook_description = (By.XPATH, "//input[@placeholder='Enter Description']")
    select_labels = (By.XPATH, "//div[@name='labels']/div[contains(@class,'cy-select__menu--label')]")
    select_playbook_tags = (By.XPATH, "//div[@name='tags']/div[contains(@class,'cy-select__menu--label')]")
    textbox_schedule_playbook = (By.XPATH, "//input[@placeholder='Enter Playbook Schedule']")

    def __init__(self, driver):
        self.driver = driver

