from selenium.webdriver.common.by import By


class Playbooks:

    def __init__(self, driver):
        self.driver = driver

    tab_cyware_playbooks = (By.XPATH, "//li[contains(@class,'cyware-playbook')]")

    def cyware_playbook_tab(self):
        return self.driver.find_element(*Playbooks.tab_cyware_playbooks)

    tab_my_playbooks = (By.XPATH, "//li[contains(@class,'my-playbook')]/a")

    def my_playbook_tab(self):
        return self.driver.find_element(*Playbooks.tab_my_playbooks)

    btn_first_playbook = (By.XPATH, "//div[3]//tr[1]/td[2]//a")

    def click_first_playbook(self):
        return self.driver.find_element(*Playbooks.btn_first_playbook)

    playbook_page_heading = (By.XPATH, "//header//h1")

    def get_manage_playbook_heading(self):
        return self.driver.find_element(*Playbooks.playbook_page_heading)

    button_create_playbook = (By.XPATH, "//button[contains(@class,'create-playbook')]")

    def click_on_create_playbook_btn(self):
        return self.driver.find_element(*Playbooks.button_create_playbook)

    button_back = (By.XPATH, "//div[@class='playbook_header__view']//i")

    def click_on_back_button(self):
        return self.driver.find_element(*Playbooks.button_back)

    button_exit_without_save = (By.XPATH, "//button[contains(text(),'Exit without Save')]")

    def click_exit_without_save(self):
        return self.driver.find_element(*Playbooks.button_exit_without_save)

    button_add_node = (By.XPATH, "")

    def click_add_node(self):
        return self.driver.find_element(*Playbooks.button_add_node)


    playbook_name_field = (By.XPATH, "//input[@placeholder='Enter Name']")

    def enter_playbook_name(self):
        return self.driver.find_element(*Playbooks.playbook_name_field)

    playbook_description_field = (By.XPATH, "//input[@placeholder='Enter Description']")

    def enter_playbook_description(self):
        return self.driver.find_element(*Playbooks.playbook_description_field)

    save_more_options = (By.XPATH, "//div[@class='el-button-group']/button[2]")

    def mouse_hover_on_save_btn(self):
        return self.driver.find_element(*Playbooks.save_more_options)

    save_and_exit_btn = (By.XPATH, "//i[@class='icon-save-and-exit']")

    def click_on_save_exit(self):
        return self.driver.find_element(*Playbooks.save_and_exit_btn)

    table_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip list-button')]")

    def get_table_view_playbook(self):
        return self.driver.find_element(*Playbooks.table_view_playbook)

    grid_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip grid-button')]")

    def get_grid_view_playbook(self):
        return self.driver.find_element(*Playbooks.grid_view_playbook)

    textbox_search_playbook = (By.CSS_SELECTOR, "input[placeholder='Search Playbook(s)']")

    def search_playbooks(self):
        return self.driver.find_element(*Playbooks.textbox_search_playbook)

    create_new_playbook_btn = (By.XPATH, "//i[@class='icon icon-plus']/..")

    def click_create_playbook(self):
        return self.driver.find_element(*Playbooks.button_create_playbook)

    button_import_playbook = (By.XPATH, "//button[contains(@class,'import-playbook')]")

    def click_import_playbook(self):
        return self.driver.find_element(*Playbooks.button_import_playbook)

    get_top_first_playbook = (By.XPATH, "//table[@class='el-table__body']/tbody/tr[1]/td[3]")

    def get_first_playbook(self):
        return self.driver.find_element(*Playbooks.get_top_first_playbook)
