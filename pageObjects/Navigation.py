from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.Actions import Action

class Navigation(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    nav_main_menu = "i.cyicon-menu"

    def click_Main_Menu(self):
        return Action.waitandclick(self, By.CSS_SELECTOR, Navigation.nav_main_menu)

    dashboard_menu_synopsis = "//span/div[contains(@class,'menuheader')]"

    def mouse_hover_menu_synopsis(self):

        return Action.mouse_hover_on_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    def visibility_of_menu_synopsis_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    activate_synopsis_tool_tips = "//div[@class='cy-switch-btn-wrapper__icon']"

    def enable_menu_synopsis(self):
        return Action.waitandclick(self, By.XPATH, Navigation.activate_synopsis_tool_tips)

    deactivate_menu_synopsis = "//div[@class='cy-switch-btn-wrapper__icon']"

    def disable_menu_synopsis(self):
        return Action.waitandclick(self, By.XPATH, Navigation.deactivate_menu_synopsis)

    nav_admin_menu = "i.icon.icon-settings-gear"

    def click_Admin_Menu(self):
        return Action.waitandclick(self, By.CSS_SELECTOR, Navigation.nav_admin_menu)


    nav_search_bar = "//div[@class='cy-sidebar']//input"

    def click_search_bar(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_search_bar)

    nav_dashboard = "//div[contains(@class,'menu-dashboard')]"

    def Navigate_Dashboard(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_dashboard)

    nav_playbook_menu_tooltip = "//img[@src='/soar/sidebar/playbook.svg']/following-sibling::div[position()=1]"

    def get_playbook_menu_synopsis_text(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_playbook_menu_tooltip)

    nav_manage_playbook = "//div[contains(@class,'menu-playbook')]"

    def Navigate_Manage_Playbook(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_manage_playbook)

    nav_run_logs = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Run Logs']"

    def Navigate_Run_Logs(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_run_logs)

    nav_trigger_event = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Triggered Events']"

    def Navigate_Trigger_Event(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_trigger_event)

    nav_configure_event = "//div[contains(@class,'walkthrough-menu-event-label')]"

    def Navigate_Configure_Event(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_configure_event)

    nav_data_sync = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                    "[normalize-space()='Data Sync']"

    def Navigate_Data_Sync(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_data_sync)

    nav_apps = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Apps']"

    def Navigate_Apps(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_apps)

    nav_agent_task = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                     "[normalize-space()='Cyware Agent Tasks']"

    def Navigate_Agent_task(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_agent_task)

    nav_labels = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Labels']"

    def Navigate_Labels(self):
        return Action.waitandclick(self, By.XPATH, Navigation.nav_labels)

    profile_settings_icon = "//*[@class='el-dropdown']/div/span"

    def Navigate_Profile_icon(self):
        return Action.waitandclick(self, By.XPATH, Navigation.profile_settings_icon)
