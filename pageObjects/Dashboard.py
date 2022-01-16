from selenium.webdriver.common.by import By

class Dashboard:

    def __init__(self, driver):
        self.driver = driver

    btn_view_all = (By.XPATH, "//div[@class='cy-dahsboard-layout__widget']//div[contains(text(),'View all')]")

    def get_all_elements(self):
        return self.driver.find_elements(*Dashboard.btn_view_all)

    btn_legend = (By.XPATH, "//div[contains(text(),'Legends')]")

    def visibility_of_legends_btn(self):
        return self.driver.find_element(*Dashboard.btn_legend)

    btn_back = (By.XPATH, "(//section[@class='csol-dashboard__fullscreen-widget']//i)[1]")

    def click_on_back_btn(self):
        return self.driver.find_element(*Dashboard.btn_back)


