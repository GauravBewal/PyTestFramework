from selenium.webdriver.common.by import By


class Navigation:

    def __init__(self, driver):
        self.driver = driver

    nav_main_menu = (By.CSS_SELECTOR, "i.cyicon-menu")
    nav_admin_menu = (By.CSS_SELECTOR, "i.icon.icon-settings-gear")
    nav_profile = (By.XPATH, "//span[@aria-describedby='el-tooltip-2789']")
    nav_dashboard = (By.XPATH, "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Dashboard']")
    nav_manage_playbook = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Manage Playbooks']")
    nav_run_logs = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Run Logs']")
    nav_trigger_event = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Triggered Events']")
    nav_configure_event = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Configure Triggers']")
    nav_labels = (By.XPATH, "//div[@class='cs-menu-item--title color-n500 font-size-14'][normalize-space()='Labels']")
    nav_apps = (By.XPATH, "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Apps']")
    nav_agent_task = (By.XPATH, "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Cyware Agent Tasks']")
    nav_data_sync = (By.XPATH, "//div[@class='cs-menu-item--title font-weight-500 color-n800 font-size-15'][normalize-space()='Data Sync']")

    def Click_Main_Menu(self):
        return self.driver.find_element(*Navigation.nav_main_menu)

    def Navigate_Dashboard(self):
        return self.driver.find_element(*Navigation.nav_dashboard)

    def Navigate_Manage_Playbook(self):
        return self.driver.find_element(*Navigation.nav_manage_playbook)

    def Navigate_Run_Logs(self):
        return self.driver.find_element(*Navigation.nav_run_logs)

    def Navigate_Trigger_Event(self):
        return self.driver.find_element(*Navigation.nav_trigger_event)

    def Navigate_Configure_Event(self):
        return self.driver.find_element(*Navigation.nav_configure_event)

    def Navigate_Data_Sync(self):
        return self.driver.find_element(*Navigation.nav_data_sync)

    def Navigate_Apps(self):
        return self.driver.find_element(*Navigation.nav_apps)

    def Click_Admin_Menu(self):
        return self.driver.find_element(*Navigation.nav_admin_menu)

    def Navigate_Agent_task(self):
        return self.driver.find_element(*Navigation.nav_agent_task)

    def Navigate_Labels(self):
        return self.driver.find_element(*Navigation.nav_labels)

    def Navigate_Profile(self):
        return self.driver.find_element(*Navigation.nav_profile)
