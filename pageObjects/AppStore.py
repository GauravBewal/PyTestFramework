from selenium.webdriver.common.by import By


class AppStore:

    app_status = ('Active', 'Inactive', 'Installed')
    button_create_new_app = (By.XPATH, "(//div[@slot='header']//button)[1]")
    button_import_package = (By.XPATH, "(//div[@slot='header']//button)[2]")
    button_app_walkthrough = (By.XPATH, "(//div[@slot='header']//button)[3]")
    tab_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']")
    tab_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']")
    count_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']/span")
    count_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']/span")

    first_app_tab = (By.XPATH, "//div[contains(@class,'text-dark-primary pt-4 pb-5 mb-4 px-4 el-row')]/div[1]/div[1]")
    first_3_dot_icon = (By.XPATH, "(//i[contains(@class,'icon icon-more-vertical color-primary')])[1]")
    first_app_status = (By.XPATH, "(//span[@class='status'])[1]")
    first_install_button = (By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Install'])[1]")
    first_published_app = (By.XPATH, "(//p[@class='font-size-11 color-n300'][normalize-space()='Published By'])[1]")
    first_created_by = (By.XPATH, "(//p[contains(text(),'Created By')])[1]")

    def __init__(self, driver):
        self.driver = driver

    def App_Store_Tab(self):
        return self.driver.find_element(*AppStore.tab_app_store)

    def My_Apps_Tab(self):
        return self.driver.find_element(*AppStore.tab_my_apps)

    def Import_button(self):
        return self.driver.find_element(*AppStore.button_import_package)

    def Create_App_button(self):
        return self.driver.find_element(*AppStore.button_create_new_app)

    def Walk_through_button(self):
        return self.driver.find_element(*AppStore.button_app_walkthrough)


