from selenium.webdriver.common.by import By


class CreatePlaybook:
    textbox_playbook_name = (By.XPATH, "//input[@placeholder='Enter Name']")
    textbox_playbook_description = (By.XPATH, "//input[@placeholder='Enter Description']")
    select_labels = (By.XPATH, "//div[@name='labels']/div[contains(@class,'cy-select__menu--label')]")
    select_playbook_tags = (By.XPATH, "//div[@name='tags']/div[contains(@class,'cy-select__menu--label')]")
    textbox_schedule_playbook = (By.XPATH, "//input[@placeholder='Enter Playbook Schedule']")
    status_switch_button = (By.XPATH, "//div[contains(@class,'cy-switch-btn__ball')]")
    enable_execution_time = (By.XPATH, "//div[contains(@class,'cy-switch-btn-wrapper')]/div[2]")

    def __init__(self, driver):
        self.driver = driver
