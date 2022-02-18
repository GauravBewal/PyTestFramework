from selenium.webdriver.common.by import By


class MyApps:
    count_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']/span")
    count_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']/span")
    first_3_dot_icon = (By.XPATH, "(//i[contains(@class,'icon icon-more-vertical color-primary')])[1]")
    first_app_status = (By.XPATH, "(//span[@class='status'])[1]")
    first_install_button = (By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Install'])[1]")
    first_published_app = (By.XPATH, "(//p[@class='font-size-11 color-n300'][normalize-space()='Published By'])[1]")
    first_created_by = (By.XPATH, "(//p[contains(text(),'Created By')])[1]")

    def __init__(self, driver):
        self.driver = driver

    tab_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']")

    def App_Store_Tab(self):
        return self.driver.find_element(*MyApps.tab_app_store)

    total_app_count = (By.XPATH, "//a[@href='/soar/app/list/my-apps']/span")

    def get_app_count(self):
        return self.driver.find_element(*MyApps.total_app_count)

    read_search_result_after_uninstall = (By.XPATH, "//div[@class='apps-container']//h1")

    def get_search_result_after_uninstall(self):
        return self.driver.find_element(*MyApps.read_search_result_after_uninstall)

    app_uninstalled_success_message = (By.XPATH, "//span[text()='App deleted successfully.']")

    def read_app_uninstall_success_message(self):
        return self.driver.find_element(*MyApps.app_uninstalled_success_message)

    confirm_uninstall_app = (By.XPATH, "(//div[@class='footer float-left']/button)[1]")

    def click_confirm_uninstall_app(self):
        return self.driver.find_element(*MyApps.confirm_uninstall_app)

    more_options_dropdown = (By.XPATH, "//div[@class='el-dropdown']/span")

    def mouse_hover_on_more_Actions(self):
        return self.driver.find_element(*MyApps.more_options_dropdown)

    uninstall_app_button = (By.XPATH, "//li[text()='Uninstall App']")

    def click_on_uninstall_app(self):
        return self.driver.find_element(*MyApps.uninstall_app_button)

    default_instance = (By.XPATH, "//div[contains(text(),'Default Instance')]/preceding-sibling::div")

    def read_default_instance(self):
        return self.driver.find_element(*MyApps.default_instance)

    instance_name_textbox = (By.XPATH, "//input[@placeholder='Enter Instance Name']")

    def enter_instance_name(self):
        return self.driver.find_element(*MyApps.instance_name_textbox)

    instance_description_textbox = (By.XPATH, "//textarea[@placeholder='Enter Instance Description']")

    def enter_instance_description(self):
        return self.driver.find_element(*MyApps.instance_description_textbox)

    instance_creation_button = (By.XPATH, "//button[text()='Create']")

    def click_instance_creation(self):
        return self.driver.find_element(*MyApps.instance_creation_button)

    app_actions_tab = (By.XPATH, "//a[contains(@href,'/action/list')]")

    def click_app_actions_tab(self):
        return self.driver.find_element(*MyApps.app_actions_tab)

    button_new_instance = (By.XPATH, "//div[@class='app-summary__actions-header--wrapper']//button")

    def click_on_new_instance(self):
        return self.driver.find_element(*MyApps.button_new_instance)

    app_instance_tab = (By.XPATH, "//a[contains(@href,'/instance/list')]")

    def click_app_instance_tab(self):
        return self.driver.find_element(*MyApps.app_instance_tab)

    app_playbooks_tab = (By.XPATH, "//a[contains(@href,'/playbook/list')]")

    def click_app_playbooks_tab(self):
        return self.driver.find_element(*MyApps.app_playbooks_tab)

    app_title = (By.XPATH, "//div[@class='app-card-v2__header']//h3")

    def read_app_title(self):
        return self.driver.find_element(*MyApps.app_title)

    active_app = (By.XPATH, "//div[@class='app-edit__view']//span//button")

    def click_active_app(self):
        return self.driver.find_element(*MyApps.active_app)

    top_1_search_result = (By.XPATH, "(//div[@class='apps-container']//h3)[1]")

    def top_first_search(self):
        return self.driver.find_element(*MyApps.top_1_search_result)

    search_app = (By.XPATH, "//input[@placeholder='Search App(s)']")

    def click_on_app_search(self):
        return self.driver.find_element(*MyApps.search_app)

    app_name_textbox = (By.XPATH, "//input[@placeholder='Enter App Name']")

    def enter_app_name(self):
        return self.driver.find_element(*MyApps.app_name_textbox)

    supported_api_version_textbox = (By.XPATH, "//input[@placeholder='Enter Supported API Versions']")

    def enter_supported_api_version(self):
        return self.driver.find_element(*MyApps.supported_api_version_textbox)

    button_app_refresh = (By.XPATH, "//div[@class='tabs']//div[1]/i")

    def click_app_refresh_button(self):
        return self.driver.find_element(*MyApps.button_app_refresh)

    tooltip_close = (By.XPATH, "//div[@role='alert']//div[2]")

    def close_tooltip(self):
        return self.driver.find_element(*MyApps.tooltip_close)

    button_app_save = (By.XPATH, "//div[@class='app-edit__view']//div[3]/button")

    def click_save_app_button(self):
        return self.driver.find_element(*MyApps.button_app_save)

    tab_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']")

    def My_Apps_Tab(self):
        return self.driver.find_element(*MyApps.tab_my_apps)

    button_import_package = (By.XPATH, "(//div[@slot='header']//button)[2]")

    def Import_button(self):
        return self.driver.find_element(*MyApps.button_import_package)

    button_create_new_app = (By.XPATH, "(//div[@slot='header']//button)[1]")

    def Create_App_button(self):
        return self.driver.find_element(*MyApps.button_create_new_app)

    button_app_walkthrough = (By.XPATH, "(//div[@slot='header']//button)[3]")

    def Walk_through_button(self):
        return self.driver.find_element(*MyApps.button_app_walkthrough)

    walkthrough_tooltip_count = (By.XPATH, "//div[@class='introjs-helperNumberLayer']")

    def get_tooltip_count(self):
        return self.driver.find_element(*MyApps.walkthrough_tooltip_count)

    walkthrough_tooltip_next_btn = (By.XPATH, "//a[contains(@class,'introjs-nextbutton')]")

    def click_on_next_btn(self):
        return self.driver.find_element(*MyApps.walkthrough_tooltip_next_btn)
