from selenium.webdriver.common.by import By


class AppStore:

    def __init__(self, driver):
        self.driver = driver

    tab_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']")

    def App_Store_Tab(self):
        return self.driver.find_element(*AppStore.tab_app_store)

    tab_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']")

    def My_Apps_Tab(self):
        return self.driver.find_element(*AppStore.tab_my_apps)

    button_import_package = (By.XPATH, "(//div[@slot='header']//button)[2]")

    def Import_button(self):
        return self.driver.find_element(*AppStore.button_import_package)

    button_create_new_app = (By.XPATH, "(//div[@slot='header']//button)[1]")

    def Create_App_button(self):
        return self.driver.find_element(*AppStore.button_create_new_app)

    button_app_walkthrough = (By.XPATH, "(//div[@slot='header']//button)[3]")

    def Walk_through_button(self):
        return self.driver.find_element(*AppStore.button_app_walkthrough)
