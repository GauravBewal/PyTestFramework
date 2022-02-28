from selenium.webdriver.common.by import By
from utilities.Actions import Action


class MyApps(Action):
    count_my_apps = (By.XPATH, "//a[@href='/soar/app/list/my-apps']/span")
    count_app_store = (By.XPATH, "//a[@href='/soar/app/list/app-store']/span")
    first_3_dot_icon = (By.XPATH, "(//i[contains(@class,'icon icon-more-vertical color-primary')])[1]")
    first_app_status = (By.XPATH, "(//span[@class='status'])[1]")
    first_install_button = (By.XPATH, "(//button[contains(@type,'button')][normalize-space()='Install'])[1]")
    first_published_app = (By.XPATH, "(//p[@class='font-size-11 color-n300'][normalize-space()='Published By'])[1]")
    first_created_by = (By.XPATH, "(//p[contains(text(),'Created By')])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_app_store = "//a[@href='/soar/app/list/app-store']"

    def App_Store_Tab(self):
        return Action.waitandclick(self, By.XPATH, MyApps.tab_app_store)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return  Action.getText(self, By.XPATH, MyApps.text_page_heading)

    total_app_count = "//a[@href='/soar/app/list/my-apps']/span"

    def get_app_count(self):
        return Action.getCountfromString(self, By.XPATH, MyApps.total_app_count)

    read_search_result_after_uninstall = "//div[@class='apps-container']//h1"

    def get_search_result_after_uninstall(self):
        return Action.getText(self, By.XPATH, MyApps.read_search_result_after_uninstall)

    app_uninstalled_success_message = "//span[text()='App deleted successfully.']"

    def read_app_uninstall_success_message(self):
        return Action.getText(self, By.XPATH, MyApps.app_uninstalled_success_message)

    confirm_uninstall_app = "(//div[@class='footer float-left']/button)[1]"

    def click_confirm_uninstall_app(self):
        return Action.waitandclick(self, By.XPATH, MyApps.confirm_uninstall_app)

    more_options_dropdown = "//div[@class='el-dropdown']/span"

    def mouse_hover_on_more_Actions(self):
        return Action.mouse_hover_on_element(self, By.XPATH, MyApps.more_options_dropdown)

    uninstall_app_button = "//li[text()='Uninstall App']"

    def click_on_uninstall_app(self):
        return Action.waitandclick(self, By.XPATH, MyApps.uninstall_app_button)

    default_instance = "//div[contains(text(),'Default Instance')]/preceding-sibling::div"

    def read_default_instance(self):
        return Action.getText(self, By.XPATH, MyApps.default_instance)

    instance_name_textbox = "//input[@placeholder='Enter Instance Name']"

    def enter_instance_name(self, instance_name):
        return Action.sendKeys(self, By.XPATH, MyApps.instance_name_textbox,instance_name)

    instance_description_textbox = "//textarea[@placeholder='Enter Instance Description']"

    def enter_instance_description(self, description):
        return Action.sendKeys(self, By.XPATH, MyApps.instance_description_textbox, description)

    instance_creation_button = "//button[text()='Create']"

    def click_instance_creation(self):
        return Action.waitandclick(self, By.XPATH, MyApps.instance_creation_button)

    app_actions_tab = "//a[contains(@href,'/action/list')]"

    def click_app_actions_tab(self):
        return Action.waitandclick(self, By.XPATH, MyApps.app_actions_tab)

    button_new_instance = "//div[@class='app-summary__actions-header--wrapper']//button"

    def click_on_new_instance(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_new_instance)

    app_instance_tab = "//a[contains(@href,'/instance/list')]"

    def click_app_instance_tab(self):
        return Action.waitandclick(self, By.XPATH, MyApps.app_instance_tab)

    app_playbooks_tab = "//a[contains(@href,'/playbook/list')]"

    def click_app_playbooks_tab(self):
        return Action.waitandclick(self, By.XPATH, MyApps.app_playbooks_tab)

    app_title = "//div[@class='app-card-v2__header']//h3"

    def read_app_title(self):
        return Action.getText(self, By.XPATH, MyApps.app_title)

    active_app = "//div[@class='app-edit__view']//span//button"

    def click_active_app(self):
        return Action.waitandclick(self, By.XPATH, MyApps.active_app)

    top_1_search_result = "(//div[@class='apps-container']//h3)[1]"

    def top_first_search(self, app_name):
        return Action.ReadSearchResult(self, By.XPATH, MyApps.top_1_search_result, app_name)

    def click_first_search_result(self):
        return Action.waitandclick(self, By.XPATH, MyApps.top_1_search_result)

    search_app = "//input[@placeholder='Search App(s)']"

    def click_on_app_search(self, app_name):
        return Action.sendKeys(self, By.XPATH, MyApps.search_app, app_name)

    app_name_textbox = "//input[@placeholder='Enter App Name']"

    def enter_app_name(self, app_name):
        return Action.sendKeys(self, By.XPATH, MyApps.app_name_textbox, app_name)

    supported_api_version_textbox = "//input[@placeholder='Enter Supported API Versions']"

    def enter_supported_api_version(self, version):
        return Action.sendKeys(self, By.XPATH, MyApps.supported_api_version_textbox, version)

    button_app_refresh = "//div[@class='tabs']//div[1]/i"

    def click_app_refresh_button(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_app_refresh)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.click(self, By.XPATH, MyApps.tooltip_close)

    button_app_save = "//div[@class='app-edit__view']//div[3]/button"

    def click_save_app_button(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_app_save)

    tab_my_apps = "//a[@href='/soar/app/list/my-apps']"

    def My_Apps_Tab(self):
        return Action.waitandclick(self, By.XPATH, MyApps.tab_my_apps)

    button_import_package = "(//div[@slot='header']//button)[2]"

    def Import_button(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_import_package)

    button_create_new_app = "(//div[@slot='header']//button)[1]"

    def Create_App_button(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_create_new_app)

    button_app_walkthrough = "(//div[@slot='header']//button)[3]"

    def Click_walkthrough_button(self):
        return Action.waitandclick(self, By.XPATH, MyApps.button_app_walkthrough)

    walkthrough_tooltip_count = "//div[@class='introjs-helperNumberLayer']"

    def get_tooltip_count(self):
       return Action.waitandclick(self, By.XPATH, MyApps.walkthrough_tooltip_count)

    walkthrough_tooltip_next_btn = "//a[contains(@class,'introjs-nextbutton')]"

    def click_on_next_btn(self):
        return Action.waitandclick(self, By.XPATH, MyApps.walkthrough_tooltip_next_btn)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.clickifelementfound(self, By.XPATH, MyApps.close_walkthrough_tooltip)