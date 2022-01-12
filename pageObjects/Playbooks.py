from selenium.webdriver.common.by import By


class Playbooks:
    tab_custom_playbooks = (By.XPATH, "(//div[@slot='header']//a)[1]")
    tab_cyware_playbooks = (By.XPATH, "(//div[@slot='header']//a)[2]")
    create_new_playbook_btn = (By.XPATH, "//i[@class='icon icon-plus']/..")
    playbook_name_field = (By.XPATH, "//input[@placeholder='Enter Name']")
    playbook_description_field = (By.XPATH, "//input[@placeholder='Enter Description']")
    save_more_options = (By.XPATH, "//div[@class='el-button-group']/button[2]")
    save_and_exit_btn = (By.XPATH, "//i[@class='icon-save-and-exit']")
    table_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip list-button')]")
    grid_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip grid-button')]")
    textbox_search_playbook = (By.CSS_SELECTOR, "input[placeholder='Search Playbook(s)']")
    button_import_playbook = (By.XPATH, "//button[contains(@class,'import-playbook')]")
    button_create_playbook = (By.XPATH, "//button[contains(@class,'create-playbook')]")

    def __init__(self, driver):
        self.driver = driver

    def cyware_app_tab(self):
        return self.driver.find_element(*Playbooks.tab_cyware_playbooks)

    def custom_app_tab(self):
        return self.driver.find_element(*Playbooks.tab_custom_playbooks)

    def click_on_create_playbook_btn(self):
        return self.driver.find_element(*Playbooks.create_new_playbook_btn)

    def enter_playbook_name(self):
        return self.driver.find_element(*Playbooks.playbook_name_field)

    def enter_playbook_description(self):
        return self.driver.find_element(*Playbooks.playbook_description_field)

    def mouse_hover_on_save_btn(self):
        return self.driver.find_element(*Playbooks.save_more_options)

    def click_on_save_exit(self):
        return self.driver.find_element(*Playbooks.save_and_exit_btn)

    def get_table_view_playbook(self):
        return self.driver.find_element(*Playbooks.table_view_playbook)

    def get_grid_view_playbook(self):
        return self.driver.find_element(*Playbooks.grid_view_playbook)
