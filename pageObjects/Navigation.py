from selenium.webdriver.common.by import By


class Navigation:

    def __init__(self, driver):
        self.driver = driver

    nav_main_menu = (By.CSS_SELECTOR, "i.cyicon-menu")

    def click_Main_Menu(self):
        return self.driver.find_element(*Navigation.nav_main_menu)

    nav_admin_menu = (By.CSS_SELECTOR, "i.icon.icon-settings-gear")

    def click_Admin_Menu(self):
        return self.driver.find_element(*Navigation.nav_admin_menu)

    nav_dashboard = (By.XPATH, "//div[contains(@class,'cs-menu-item--title') or (text()='Dashboard')]")

    def Navigate_Dashboard(self):
        return self.driver.find_element(*Navigation.nav_dashboard)

    nav_manage_playbook = (
        By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Manage Playbooks']")

    def Navigate_Manage_Playbook(self):
        return self.driver.find_element(*Navigation.nav_manage_playbook)

    nav_run_logs = (
        By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Run Logs']")

    def Navigate_Run_Logs(self):
        return self.driver.find_element(*Navigation.nav_run_logs)

    nav_trigger_event = (
        By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Triggered Events']")

    def Navigate_Trigger_Event(self):
        return self.driver.find_element(*Navigation.nav_trigger_event)

    nav_configure_event = (
        By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Configure Triggers']")

    def Navigate_Configure_Event(self):
        return self.driver.find_element(*Navigation.nav_configure_event)

    nav_data_sync = (By.XPATH,
                     "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']"
                     "[normalize-space()='Data Sync']")

    def Navigate_Data_Sync(self):
        return self.driver.find_element(*Navigation.nav_data_sync)

    nav_apps = (
        By.XPATH,
        "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Apps']")

    def Navigate_Apps(self):
        return self.driver.find_element(*Navigation.nav_apps)

    nav_agent_task = (By.XPATH,
                      "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15']"
                      "[normalize-space()='Cyware Agent Tasks']")

    def Navigate_Agent_task(self):
        return self.driver.find_element(*Navigation.nav_agent_task)

    nav_labels = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Labels']")

    def Navigate_Labels(self):
        return self.driver.find_element(*Navigation.nav_labels)

    nav_profile = (By.XPATH, "//span[@aria-describedby='el-tooltip-2789']")

    def Navigate_Profile(self):
        return self.driver.find_element(*Navigation.nav_profile)
