from selenium.webdriver.common.by import By


class Labels:

    def __init__(self, driver):
        self.driver = driver

    create_New_Label = (By.XPATH, "//button[normalize-space()='New']")
    text_box_Label_Name = (By.XPATH, "//input[@aria-placeholder='Label Name']")
    text_box_Description = (By.XPATH, "//textarea[@aria-placeholder='Description']")
    text_box_search = (By.CSS_SELECTOR, "#main-input")
    tab_inActive = (By.XPATH, "//a[normalize-space()='Inactive']")
    tab_Active = (By.XPATH, "//a[normalize-space()='Active']")
    tab_All = (By.XPATH, "//a[normalize-space()='All']")
    button_sort = (By.XPATH, "//span[contains(text(),'Sort')]")
    button_create = (By.XPATH, "//button[normalize-space()='Create']")
    button_update = (By.XPATH, "//button[normalize-space()='Update']")
    get_labels_count = (By.XPATH, "//h1[contains(text(),'Labels (')]")
    top_label_in_listing = (By.XPATH, "(//tr//a[contains(text(),'Label_')])[1]")
    click_close_tooltip_xpath = (By.XPATH, "//div[@role='alert']//div[2]")
    click_active_toggle = (By.XPATH, "//form//div[4]//button")
    label_field_error_msg = (By.XPATH, "//div[@class='el-form-item__error']")

    def click_New_Label(self):
        return self.driver.find_element(*Labels.create_New_Label)

    def get_label_field_error_msg(self):
        return self.driver.find_element(*Labels.label_field_error_msg)

    def click_toggle(self):
        return self.driver.find_element(*Labels.click_active_toggle)

    def put_Search_String(self):
        return self.driver.find_element(*Labels.text_box_search)

    def top_1_label_name(self):
        return self.driver.find_element(*Labels.top_label_in_listing)

    def click_Active(self):
        return self.driver.find_element(*Labels.tab_Active)

    def click_InActive(self):
        return self.driver.find_element(*Labels.tab_inActive)

    def click_All(self):
        return self.driver.find_element(*Labels.tab_All)

    def click_Sort(self):
        return self.driver.find_element(*Labels.button_sort)

    def put_Label_Name(self):
        return self.driver.find_element(*Labels.text_box_Label_Name)

    def click_update_label(self):
        return self.driver.find_element(*Labels.button_update)

    def put_Description(self):
        return self.driver.find_element(*Labels.text_box_Description)

    def click_close_tooltip(self):
        return self.driver.find_element(*Labels.click_close_tooltip_xpath)

    def get_label_count(self):
        return self.driver.find_element(*Labels.get_labels_count)

    def create_Label(self):
        return self.driver.find_element(*Labels.button_create)
