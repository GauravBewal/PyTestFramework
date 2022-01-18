from selenium.webdriver.common.by import By


class Labels:
    click_select_all_columns = (By.XPATH, "//button[contains(text(),'Select All Columns')]")

    def __init__(self, driver):
        self.driver = driver

    create_New_Label = (By.XPATH, "//header//button")

    def click_New_Label(self):
        return self.driver.find_element(*Labels.create_New_Label)

    click_clear_search = (By.XPATH, "//div[contains(@class,'clear-button')]/i")

    def clear_search(self):
        return self.driver.find_element(*Labels.click_clear_search)

    created_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[2]")

    def select_created_by_customization(self):
        return self.driver.find_element(*Labels.created_by_in_customize_table)

    modified_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[4]")

    def select_modified_by_customization(self):
        return self.driver.find_element(*Labels.modified_by_in_customize_table)

    save_customized_table = (By.XPATH, "//div[@class='cy-right-model__footer']//button")

    def save_table_customization(self):
        return self.driver.find_element(*Labels.save_customized_table)

    label_field_error_msg = (By.XPATH, "//div[@class='el-form-item__error']")

    def get_label_field_error_msg(self):
        return self.driver.find_element(*Labels.label_field_error_msg)

    click_customizable_button = (By.XPATH, "//i[@class='cyicon-settings']")

    def click_customize_table(self):
        return self.driver.find_element(*Labels.click_customizable_button)

    click_on_close_label_slider = (By.XPATH, "//form//i[contains(@class,'el-icon-close')]")

    def close_label_slider(self):
        return self.driver.find_element(*Labels.click_on_close_label_slider)

    click_active_toggle = (By.XPATH, "//form//div[4]//span[text()='On ']")

    def click_toggle(self):
        return self.driver.find_element(*Labels.click_active_toggle)

    text_box_search = (By.CSS_SELECTOR, "#main-input")

    def put_Search_String(self):
        return self.driver.find_element(*Labels.text_box_search)

    top_label_in_listing = (By.XPATH, "(//tr//a[contains(text(),'Label_')])[1]")

    def top_1_label_name(self):
        return self.driver.find_element(*Labels.top_label_in_listing)

    label_created_user = (By.XPATH, "//tbody/tr[1]/td[2]")

    def get_label_created_user(self):
        return self.driver.find_element(*Labels.label_created_user)

    label_modified_user = (By.XPATH, "//tbody/tr[1]/td[4]")

    def get_label_modified_user(self):
        return self.driver.find_element(*Labels.label_modified_user)

    tab_Active = (By.XPATH, "//a[normalize-space()='Active']")

    def click_Active(self):
        return self.driver.find_element(*Labels.tab_Active)

    tab_inActive = (By.XPATH, "//a[normalize-space()='Inactive']")

    def click_InActive(self):
        return self.driver.find_element(*Labels.tab_inActive)

    tab_All = (By.XPATH, "//a[normalize-space()='All']")

    def click_All(self):
        return self.driver.find_element(*Labels.tab_All)

    button_sort = (By.XPATH, "//span[contains(text(),'Sort')]")

    def click_Sort(self):
        return self.driver.find_element(*Labels.button_sort)

    text_box_Label_Name = (By.XPATH, "//input[@aria-placeholder='Label Name']")

    def put_Label_Name(self):
        return self.driver.find_element(*Labels.text_box_Label_Name)

    button_update = (By.XPATH, "//button[text()='Update']")

    def click_update_label(self):
        return self.driver.find_element(*Labels.button_update)

    text_box_Description = (By.XPATH, "//textarea[@aria-placeholder='Description']")

    def put_Description(self):
        return self.driver.find_element(*Labels.text_box_Description)

    click_close_tooltip_xpath = (By.XPATH, "//div[@class='modal--header']//div[2]/i")

    def click_close_tooltip(self):
        return self.driver.find_element(*Labels.click_close_tooltip_xpath)

    get_labels_count = (By.XPATH, "//h1[contains(text(),'Labels (')]")

    def get_label_count(self):
        return self.driver.find_element(*Labels.get_labels_count)

    button_create = (By.XPATH, "//button[text()='Create']")

    def create_Label(self):
        return self.driver.find_element(*Labels.button_create)
