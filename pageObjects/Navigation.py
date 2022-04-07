import time

from selenium.webdriver.common.by import By

from utilities.Actions import Action


class Navigation(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    nav_main_menu = "//span[contains(@class,'menu-icon')]/div"

    def click_main_menu(self):
        """
            Click on Main menu
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_main_menu)

    dashboard_menu_synopsis = "//span/div[contains(@class,'menuheader')]"

    def mouse_hover_menu_synopsis(self):
        """
            Mouse hover menu Synopsis
            :return:
        """
        return Action.mouse_hover_on_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    def visibility_of_menu_synopsis_btn(self):
        """
            Visibility of menu Synopsis button
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.dashboard_menu_synopsis)

    activate_synopsis_tool_tips = "//div[@class='cy-switch-btn-wrapper__icon']"

    def enable_menu_synopsis(self):
        """
            Enable menu Synopsis Toggle
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.activate_synopsis_tool_tips)

    deactivate_menu_synopsis = "//div[@class='cy-switch-btn-wrapper__icon']"

    def disable_menu_synopsis(self):
        """
            Disable Menu Synopsis toggle
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.deactivate_menu_synopsis)

    nav_admin_menu = "//a[@href='/soar/admin']"

    def click_admin_menu(self):
        """
            Click on Admin menu
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_admin_menu)

    nav_search_bar = "//div[@class='cy-sidebar']//input"

    def click_search_bar(self):
        """
            Click on search bar
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_search_bar)

    def Enter_string_in_searchbar(self, value):
        """
            Put String in Search bar
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, Navigation.nav_search_bar, value)

    nav_dashboard = "//div[contains(@class,'menu-dashboard')]"

    def navigate_dashboard(self):
        """
            Navigate to Dashboard
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_dashboard)

    nav_playbook_menu_tooltip = "//img[@src='/soar/sidebar/playbook.svg']/following-sibling::div[position()=1]"

    def get_playbook_menu_synopsis_text(self):
        """
            Get playbook menu Synopsis Text
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_playbook_menu_tooltip)

    nav_manage_playbook = "//div[contains(@class,'menu-playbook')]"

    def navigate_manage_playbook(self):
        """
            Navigate to Manage Playbooks
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_manage_playbook)

    nav_run_logs = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Run Logs']"

    def navigate_run_logs(self):
        """
            Navigate to Run logs
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_run_logs)

    nav_trigger_event = "//div[@class='cs-menu-item--title color-n500 font-size-14']" \
                        "[normalize-space()='Triggered Events']"

    def navigate_trigger_event(self):
        """
            Navigate to trigger event
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.nav_trigger_event)

    nav_configure_event = "//div[contains(@class,'walkthrough-menu-event-label')]"

    def navigate_configure_event(self):
        """
            Navigate to Configure Event
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_configure_event)

    nav_data_sync = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                    "[normalize-space()='Data Sync']"

    def navigate_data_sync(self):
        """
            Navigate to Data Sync Module
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_data_sync)

    nav_apps = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Apps']"

    def navigate_apps(self):
        """
            Navigate to Apps module
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_apps)

    nav_agent_task = "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']" \
                     "[normalize-space()='Cyware Agent Tasks']"

    def navigate_agent_task(self):
        """
            Navigate to agent task
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_agent_task)

    page_heading = "//header//h1"

    def get_page_heading(self):
        """
            Get page heading
            :return:
        """
        return Action.get_text(self, By.XPATH, Navigation.page_heading)

    nav_labels = "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Labels']"

    def navigate_labels(self):
        """
            Navigate to labels
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.nav_labels)

    profile_settings_icon = "//*[@class='el-dropdown']/div/span"

    def navigate_profile_icon(self):
        """
            Navigate to profile icon
            :return:
        """
        return Action.javascript_click(self, By.XPATH, Navigation.profile_settings_icon)

    search_result_txt = "//div[contains(@class,'menu-dashboard')]//div[contains(text(),'Dashboard')]"

    def read_searchbar_result(self):
        """
            Read Search bar results
            :return:
        """
        return Action.get_text(self, By.XPATH, Navigation.search_result_txt)

    btn_clear_search_result = "//i[contains(@class,'search-input__close')]/parent::span"

    def click_clear_search_result_btn(self):
        """
            Click and clear search result button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.btn_clear_search_result)

    def get_list_of_elements(self, elements_count, elements):
        """
            Get list of Elements
            :param elements_count:
            :param elements:
            :return:
        """
        elements_list = []
        # indexing xpath and storing it in list
        for value in range(1, elements_count + 1):
            path = "(" + elements + ")[" + str(value) + "]"
            elements_list.append(path)

        return elements_list

    get_started_btn = "//button[contains(text(),'Get Started')]"

    def click_get_started_button(self):
        """
            Click on get started button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.get_started_btn)

    first_bar_graph = "(//*[contains(@class,'highcharts-axis')])[1]"

    def visibility_of_first_bar_graph(self):
        """
            Visibility of first bar graph
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.first_bar_graph)

    def scroll_to_get_started_view(self):
        """
            Scroll to get started view
            :return:
        """
        return Action.scroll_to_element_view(self, By.XPATH, Navigation.get_started_btn)

    walkthrough_options = "//ul/a//span"

    def get_walkthrough_option_elements(self):
        """
            Get Walkthrough option elements
            :return:
        """
        return Action.get_no_of_elements_present(self, By.XPATH, Navigation.walkthrough_options)

    def visibility_of_walkthrough_option(self, element):
        """
            Visibility of walkthrough option
            :param element:
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, element)

    walkthrough_overview_btn = "//span[contains(text(),'Overview')]"

    def click_on_overview_btn(self):
        """
            Click on overview button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_overview_btn)

    walkthrough_playbook_btn = "//ul//a[@href='/soar/playbook']"

    def click_playbook_walkthrough_btn(self):
        """
            Click on playbook walkthrough button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_playbook_btn)

    walkthrough_apps_btn = "//span[contains(text(),'Apps')]"

    def click_apps_walkthrough_btn(self):
        """
            Click on apps walkthrough button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, Navigation.walkthrough_apps_btn)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def visibility_of_walkthrough_close_btn(self):
        """
            Visibility of walk through close button
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.close_walkthrough_tooltip)

    def click_on_close_walkthrough(self):
        """
            Click on close walk through
            :return:
        """
        return Action.click_if_element_found(self, By.XPATH, Navigation.close_walkthrough_tooltip)

    navigation_error_msg = "(//div[@role='alert']//span[contains(text(),'Error')])[1]"

    def verify_error_msg_after_navigation(self):
        """
            Verify error message after navigation
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, Navigation.navigation_error_msg)
