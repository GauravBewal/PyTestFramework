from selenium.webdriver.common.by import By
from utilities.Actions import Action

class Dashboard(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    widget_titles = ['PLAYBOOK EXECUTION TIMELINE', 'FREQUENTLY USED PLAYBOOKS',
                     'PLAYBOOK EXECUTION TIME (ON AVERAGE)'
        , 'FREQUENTLY USED INSTANCES', 'FREQUENTLY USED APPS', 'FREQUENTLY USED ACTIONS',
                     'FREQUENTLY EXECUTED ACTIONS'
        , 'FREQUENTLY UTILIZED APPS', 'FREQUENTLY UTILIZED INSTANCES', 'TOTAL EVENT COUNT'
        , 'INCOMING SOURCE EVENTS', 'PERCENTAGE OF UNUTILIZED EVENTS',
                     'PERCENTAGE OF EVENTS THAT CAUSE PLAYBOOK EXECUTION ERROR']

    btn_viewall_all = "//div[@class='cy-dahsboard-layout__widget']//div[contains(text(),'View all')]"

    def get_all_viewall_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Dashboard.btn_viewall_all)

    def get_list_of_elements(self, elements_count, elements):
        elements_list = []
        #indexing xpath and storing it in list
        for value in range(1, elements_count+1):
            path = "("+elements+")["+str(value)+"]"
            elements_list.append(path)
        return elements_list

    def click_on_view_all_btn(self, element):
        return Action.waitandclick(self, By.XPATH, element)

    widget_elements = "//div[contains(@class,'widget-label')]/div"

    def get_all_widget_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Dashboard.widget_elements)

    btn_legend = "//div[contains(text(),'Legends')]"

    def visibility_of_legends_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_legend)

    btn_maximize = "//i[@class='icon icon-maximize']/parent::button"

    def click_maximize_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_maximize)

    btn_minimize = "//i[@class='icon icon-collapse']/parent::button"

    def click_minimize_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_minimize)

    def check_visibility_of_minimize_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_minimize)

    btn_dark_mode = "//i[@class='icon cyicon-moon']/parent::button"

    def click_dark_mode_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_dark_mode)

    def check_dark_mode_btn_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_dark_mode)

    def check_visibility_of_dark_mode_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_dark_mode)

    btn_light_mode = "//i[@class='icon cyicon-sun']/parent::button"

    def click_light_mode_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_light_mode)

    btn_sync = "//i[@class='icon icon-refresh']/parent::button"

    def click_sync_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_sync)

    def check_visibility_of_light_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Dashboard.btn_light_mode)

    start_date_btn = "//input[@placeholder='Start date']"

    def click_start_date_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.start_date_btn)

    select_end_date = "(//tr[@class='el-date-table__row']/td[contains(@class,'available')]//span)[3]"

    def select_calendar_end_date(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.select_end_date)

    def get_calendar_end_date_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.select_end_date, 'background-color')

    select_start_date = "(//tr[@class='el-date-table__row']/td[contains(@class,'available')]//span)[1]"

    def select_calendar_start_date(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.select_start_date)

    def get_calendar_start_date_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.select_start_date, 'background-color')

    cyware_header_section = "//div[contains(@class,'cy-header')]"

    def read_header_color(self):
        return Action.getElementColor(self, By.XPATH, Dashboard.cyware_header_section, 'color')

    def find_element_path_and_get_text(self, path):
        return Action.getText(self, By.XPATH, path)

    def find_element_path_and_click(self, path):
        return Action.waitandclick(self, By.XPATH, path)

    btn_back = "(//section[@class='csol-dashboard__fullscreen-widget']//i)[1]"

    def click_on_back_btn(self):
        return Action.waitandclick(self, By.XPATH, Dashboard.btn_back)
