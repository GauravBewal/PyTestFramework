import time

from selenium.webdriver.common.by import By
from utilities.Actions import Action
from configuration.readConfiguration import ReadConfig

class Labels(Action):
    click_select_all_columns = (By.XPATH, "//button[contains(text(),'Select All Columns')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    create_New_Label = "//header//button"

    def click_New_Label(self):
        return Action.waitandclick(self, By.XPATH, Labels.create_New_Label)

    click_clear_search = "//div[contains(@class,'clear-button')]/i"

    def clear_search(self):
        return Action.waitandclick(self, By.XPATH, Labels.click_clear_search)

    created_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[2]")

    def select_created_by_customization(self):
        return self.driver.find_element(*Labels.created_by_in_customize_table)

    modified_by_in_customize_table = (By.XPATH, "(//span[@class='el-checkbox__inner'])[4]")

    def select_modified_by_customization(self):
        return self.driver.find_element(*Labels.modified_by_in_customize_table)

    save_customized_table = (By.XPATH, "//div[@class='cy-right-model__footer']//button")

    def save_table_customization(self):
        return self.driver.find_element(*Labels.save_customized_table)

    label_field_error_msg = "//div[@class='el-form-item__error']"

    def get_label_field_error_msg(self):
        return Action.getText(self, By.XPATH, Labels.label_field_error_msg)

    click_customizable_button = (By.XPATH, "//i[@class='cyicon-settings']")

    def click_customize_table(self):
        return self.driver.find_element(*Labels.click_customizable_button)

    click_on_close_label_slider = "//form//i[contains(@class,'el-icon-close')]"

    def close_label_slider(self):
        return Action.waitandclick(self, By.XPATH, Labels.click_on_close_label_slider)

    btn_inactive_toggle = "//form//div[4]//span[text()='On ']"

    def click_inactive_toggle(self):
        return Action.waitandclick(self, By.XPATH, Labels.btn_inactive_toggle)

    text_box_search = "#main-input"

    def put_Search_String(self, value):
        return Action.sendKeys(self, By.CSS_SELECTOR, Labels.text_box_search, value)

    def click_Enter_for_Search(self):
        return Action.clickEnter(self, By.CSS_SELECTOR, Labels.text_box_search)

    top_label_in_listing = "(//tr//a[contains(text(),'Label_')])[1]"

    def top_1_label_name(self):
        return Action.getText(self, By.XPATH, Labels.top_label_in_listing)

    def click_top_first_label(self):
        return Action.waitandclick(self, By.XPATH, Labels.top_label_in_listing)

    label_created_user = "//tbody/tr[1]/td[2]"

    def get_label_created_user(self):
        return Action.getText(self, By.XPATH, Labels.label_created_user)

    label_modified_user = "//tbody/tr[1]/td[4]"

    def get_label_modified_user(self):
        return Action.getText(self, By.XPATH, Labels.label_modified_user)

    tab_inActive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.waitandclick(self, By.XPATH, Labels.tab_inActive)

    def get_inactive_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Labels.tab_inActive)

    tab_All = "//li/a[contains(text(),'All')]"

    def click_All_tab(self):
        return Action.waitandclick(self, By.XPATH, Labels.tab_All)

    def get_all_tab_color(self):
        return Action.getElementColor(self, By.XPATH, Labels.tab_All)

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_Active_tab(self):
        return Action.waitandclick(self, By.XPATH, Labels.tab_active)

    button_sort = (By.XPATH, "//span[contains(text(),'Sort')]")

    def click_Sort(self):
        return self.driver.find_element(*Labels.button_sort)

    text_box_Label_Name = "//input[@aria-placeholder='Label Name']"

    def put_Label_Name(self, value):
        return Action.sendKeys(self, By.XPATH, Labels.text_box_Label_Name, value)

    def clear_label_field(self):
        return Action.clear_field(self, By.XPATH, Labels.text_box_Label_Name)

    button_update = "//button[text()='Update']"

    def click_update_label(self):
        return Action.waitandclick(self, By.XPATH, Labels.button_update)

    text_box_Description = "//textarea[@aria-placeholder='Description']"

    def put_Description(self, value):
        return Action.sendKeys(self, By.XPATH, Labels.text_box_Description, value)

    def clear_Description_field(self):
        return Action.clear_field(self, By.XPATH, Labels.text_box_Description)


    click_close_tooltip_xpath = "//div[contains(@class,'notification__closeBtn')]"

    def click_close_tooltip(self):
        return Action.waitandclick(self, By.XPATH, Labels.click_close_tooltip_xpath)

    get_labels_count = "//h1[contains(text(),'Labels (')]"

    def get_label_count(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.getCountfromString(self, By.XPATH, Labels.get_labels_count)


    button_create = "//button[text()='Create']"

    def create_Label(self):
        return Action.waitandclick(self, By.XPATH, Labels.button_create)
