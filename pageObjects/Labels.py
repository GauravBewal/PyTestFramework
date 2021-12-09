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

    def click_New_Label(self):
        return self.driver.find_element(*Labels.create_New_Label)

    def put_Search_String(self):
        return self.driver.find_element(*Labels.text_box_search)

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

    def put_Description(self):
        return self.driver.find_element(*Labels.text_box_Description)

    def create_Label(self):
        return self.driver.find_element(*Labels.button_create)
