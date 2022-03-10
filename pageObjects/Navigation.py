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

    nav_admin_menu = "//a[@href='/soar/admin']"

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

    search_result_txt = "//div[contains(@class,'menu-dashboard')]//div[contains(text(),'Dashboard')]"

    def read_searchbar_result(self):
        return Action.get_text(self, By.XPATH, Navigation.search_result_txt)

    btn_clear_search_result = "//i[contains(@class,'search-input__close')]/parent::span"

    def click_clear_search_result_btn(self):
        return Action.wait_and_click(self, By.XPATH, Navigation.btn_clear_search_result)

    def get_list_of_elements(self, elements_count, elements):
        elements_list = []
        # indexing xpath and storing it in list
        for value in range(1, elements_count + 1):
            path = "(" + elements + ")[" + str(value) + "]"
            elements_list.append(path)

        return elements_list

    get_started_btn="//button[contains(text(),'Get Started')]"

    def click_get_started_button(self):
        return Action.wait_and_click(self, By.XPATH, Navigation.get_started_btn)

    walkthrough_options="//ul/a//span"
    def get_walkthrough_option_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Navigation.walkthrough_options)

    def visibility_of_walkthrough_option(self, element):
        return Action.check_visibility_of_element(self, By.XPATH, element)

    walkthrough_overview_btn = "//span[contains(text(),'Overview')]/parent::div"

    def click_on_overview_btn(self):
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_overview_btn)

    walkthrough_playbook_btn = "//span[contains(text(),'Manage Playbooks')]/parent::div"

    def click_playbook_walkthrough_btn(self):
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_playbook_btn)

    walkthrough_apps_btn = "//span[contains(text(),'Apps')]/parent::div"

    def click_apps_walkthrough_btn(self):
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_apps_btn)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def visibility_of_walkthrough_close_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.close_walkthrough_tooltip)


    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, Navigation.close_walkthrough_tooltip)

