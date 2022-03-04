from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Navigation(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    nav_main_menu = "//span[contains(@class,'menu-icon')]/div"

    def click_main_menu(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_main_menu)

    dashboard_menu_synopsis = "//span/div[contains(@class,'menuheader')]"

    def mouse_hover_menu_synopsis(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    def visibility_of_menu_synopsis_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    activate_synopsis_tool_tips = "//div[@class='cy-switch-btn-wrapper__icon']"

    def enable_menu_synopsis(self):
        return Action.javascript_click(self, By.XPATH, Navigation.activate_synopsis_tool_tips)

    deactivate_menu_synopsis = "//div[@class='cy-switch-btn-wrapper__icon']"

    def disable_menu_synopsis(self):
        return Action.javascript_click(self, By.XPATH, Navigation.deactivate_menu_synopsis)

    nav_admin_menu = "//div[contains(@class,'walkthrough-admin-icon')]"

    def click_admin_menu(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_admin_menu)

    nav_search_bar = "//div[@class='cy-sidebar']//input"

    def click_search_bar(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_search_bar)

    def Enter_string_in_searchbar(self, value):
        return Action.send_keys(self, By.XPATH, Navigation.nav_search_bar, value)

    nav_dashboard = "//div[contains(@class,'menu-dashboard')]"

    def navigate_dashboard(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_dashboard)

    nav_playbook_menu_tooltip = "//img[@src='/soar/sidebar/playbook.svg']/following-sibling::div[position()=1]"

    def get_playbook_menu_synopsis_text(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_playbook_menu_tooltip)

    nav_manage_playbook = "//div[contains(@class,'menu-playbook')]"

    def navigate_manage_playbook(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_manage_playbook)

    nav_run_logs = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Run Logs']"

    def navigate_run_logs(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_run_logs)

    nav_trigger_event = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Triggered Events']"

    def navigate_trigger_event(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_trigger_event)

    nav_configure_event = "//div[contains(@class,'walkthrough-menu-event-label')]"

    def navigate_configure_event(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_configure_event)

    nav_data_sync = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                    "[normalize-space()='Data Sync']"

    def navigate_data_sync(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_data_sync)

    nav_apps = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Apps']"

    def navigate_apps(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_apps)

    nav_agent_task = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                     "[normalize-space()='Cyware Agent Tasks']"

    def navigate_agent_task(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_agent_task)

    nav_labels = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Labels']"

    def navigate_labels(self):
        return Action.javascript_click(self, By.XPATH, Navigation.nav_labels)

    profile_settings_icon = "//*[@class='el-dropdown']/div/span"

    def navigate_profile_icon(self):
        return Action.javascript_click(self, By.XPATH, Navigation.profile_settings_icon)

    name_id = "//div[contains(@class,'menu-dashboard')]//div[contains(text(),'Dashboard')]"

    def read_searchbar_result(self):
        return Action.get_text(self, By.XPATH, Navigation.name_id)
