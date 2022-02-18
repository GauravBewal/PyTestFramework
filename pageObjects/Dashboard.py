from selenium.webdriver.common.by import By


class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    btn_viewall_all = (By.XPATH, "//div[@class='cy-dahsboard-layout__widget']//div[contains(text(),'View all')]")

    def get_all_viewall_elements(self):
        return self.driver.find_elements(*Dashboard.btn_viewall_all)

    widget_elements = (By.XPATH, "//div[contains(@class,'widget-label')]/div")

    def get_all_widget_elements(self):
        return self.driver.find_elements(*Dashboard.widget_elements)

    btn_legend = (By.XPATH, "//div[contains(text(),'Legends')]")

    def visibility_of_legends_btn(self):
        return self.driver.find_element(*Dashboard.btn_legend)

    btn_maximize = (By.XPATH, "//i[@class='icon icon-maximize']/parent::button")

    def click_maximize_btn(self):
        return self.driver.find_element(*Dashboard.btn_maximize)

    btn_minimize = (By.XPATH, "//i[@class='icon icon-collapse']/parent::button")

    def click_minimize_btn(self):
        return self.driver.find_element(*Dashboard.btn_minimize)

    btn_dark_mode = (By.XPATH, "//i[@class='icon cyicon-moon']/parent::button")

    def click_dark_mode_btn(self):
        return self.driver.find_element(*Dashboard.btn_dark_mode)

    btn_light_mode = (By.XPATH, "//i[@class='icon cyicon-sun']/parent::button")

    def click_light_mode(self):
        return self.driver.find_element(*Dashboard.btn_light_mode)

    start_date_btn = (By.XPATH, "//input[@placeholder='Start date']")

    def click_start_date_btn(self):
        return self.driver.find_element(*Dashboard.start_date_btn)


    select_end_date = (By.XPATH, "(//tr[@class='el-date-table__row']/td[@class='available']//span)[7]")

    def select_calendar_end_date(self):
        return self.driver.find_element(*Dashboard.select_end_date)

    select_start_date = (By.XPATH, "(//tr[@class='el-date-table__row']/td[@class='available']//span)[1]")

    def select_calendar_start_date(self):
        return self.driver.find_element(*Dashboard.select_start_date)

    cyware_header_section = (By.XPATH, "//div[@class='cy-header dark-mode']")

    def read_header_color(self):
        return self.driver.find_element(*Dashboard.cyware_header_section)


    def click_on_path(self, path):
        return self.driver.find_element(By.XPATH, path)

    btn_back = (By.XPATH, "(//section[@class='csol-dashboard__fullscreen-widget']//i)[1]")

    def click_on_back_btn(self):
        return self.driver.find_element(*Dashboard.btn_back)


