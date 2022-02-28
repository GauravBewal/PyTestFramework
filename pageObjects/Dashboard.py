from selenium.webdriver.common.by import By
from utilities.Actions import Action

class Dashboard(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    btn_viewall_all = (By.XPATH, "//div[@class='cy-dahsboard-layout__widget']//div[contains(text(),'View all')]")

    def get_all_viewall_elements(self):
        return self.driver.find_elements(*Dashboard.btn_viewall_all)

    widget_elements = (By.XPATH, "//div[contains(@class,'widget-label')]/div")

    def get_all_widget_elements(self):
        return self.driver.find_elements(*Dashboard.widget_elements)

    btn_legend = "//div[contains(text(),'Legends')]"

    def visibility_of_legends_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_legend)

    btn_maximize = "//i[@class='icon icon-maximize']/parent::button"

    def click_maximize_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_maximize)

    btn_minimize = "//i[@class='icon icon-collapse']/parent::button"

    def click_minimize_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_minimize)

    def check_visibility_of_minimize_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_minimize)

    btn_dark_mode = "//i[@class='icon cyicon-moon']/parent::button"

    def click_dark_mode_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_dark_mode)

    def check_dark_mode_btn_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_dark_mode)

    def check_visibility_of_dark_mode_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_dark_mode)

    btn_light_mode = "//i[@class='icon cyicon-sun']/parent::button"

    def click_light_mode_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_light_mode)

    btn_sync = "//i[@class='icon icon-refresh']/parent::button"

    def click_sync_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_sync)

    def check_visibility_of_light_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_light_mode)

    start_date_btn = "//input[@placeholder='Start date']"

    def click_start_date_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.start_date_btn)

    select_end_date = "(//tr[@class='el-date-table__row']/td[@class='available']//span)[7]"

    def select_calendar_end_date(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.select_end_date)

    def get_calendar_end_date_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.select_end_date)

    select_start_date = "(//tr[@class='el-date-table__row']/td[@class='available']//span)[1]"

    def select_calendar_start_date(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.select_start_date)

    def get_calendar_start_date_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.select_start_date)

    cyware_header_section = "//div[contains(@class,'cy-header')]"

    def read_header_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.cyware_header_section)

    def find_element_path_and_get_text(self, path):
        return Action.getText(self, By.XPATH, path)

    def find_element_path_and_click(self, path):
        return Action.waitandclick(self, By.XPATH, path)

    btn_back = "(//section[@class='csol-dashboard__fullscreen-widget']//i)[1]"

    def click_on_back_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_back)
