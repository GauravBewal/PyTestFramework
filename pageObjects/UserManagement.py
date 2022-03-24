from selenium.webdriver.common.by import By

from utilities.Actions import Action


class UserManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_user_management = "//p[contains(text(),'User Management')]/parent::div/parent::div"

    def click_user_management(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_user_management)

    user_count = "//h1[contains(text(),'User Management (')]"

    def get_user_count(self):
        return Action.get_count_from_string(self, By.XPATH, UserManagement.user_count)


    first_active_user = "(//span[text()='Active' and @class='status__text'])[1]"

    def visibility_of_first_active_user(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_active_user)

    first_inactive_user = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def visibility_of_first_inactive_user(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_inactive_user)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_All)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_All, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.tab_active)

    btn_new_user = "//header//div[3]/button"

    def click_add_user(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_new_user)

    btn_export_user = "//header//div[@class='el-dropdown']/button"

    def click_export(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_export_user)

    drpdwn_export_option = "//li[text()='CSV']"

    def export_option_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, UserManagement.drpdwn_export_option)

    text_slider_title = "//div[text()='User']"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, UserManagement.text_slider_title)

    btn_slider_close = "//div[text()='User']/../following-sibling::div/span[2]"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_slider_close)

    First_name = "(//div[contains(@class,'cy-input ')]/input)[1]"

    def put_first_name(self, value):
        return Action.send_keys(self, By.XPATH, UserManagement.First_name, value)

    Last_name = "(//div[contains(@class,'cy-input ')]/input)[2]"

    def put_last_name(self, value):
        return Action.send_keys(self, By.XPATH, UserManagement.Last_name, value)

    drop_down_btn = "//div[contains(@class,'cy-select__menu--icon')]//span[contains(@class,'cyicon-chevron-down')]"

    def click_dropdown(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.drop_down_btn)

    top_first_usergroup = "(//div[contains(@class,'cy-select__menu---expanded')]//ul//li)[1]"

    def click_top_user_group(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.top_first_usergroup)

    user_name = "(//div[contains(@class,'cy-input ')]/input)[3]"

    def put_user_name(self, value):
        return Action.send_keys(self, By.XPATH, UserManagement.user_name, value)

    user_email = "(//div[contains(@class,'cy-input ')]/input)[4]"

    def put_user_email(self, value):
        return Action.send_keys(self, By.XPATH, UserManagement.user_email, value)

    create_user_btn = "//div[contains(@class,'cy-right-model__footer')]//button[contains(text(),'Create')]"

    def click_create_user_btn(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.create_user_btn)

    close_tooltip_btn = "//div[contains(@class,'notification__closeBtn')]"

    def click_close_tooltip(self):
        return Action.normal_click(self, By.XPATH, UserManagement.close_tooltip_btn)

    toast_msg_txt = "//div[@role='alert']//span[2]/span[1]"

    def get_tooltip_msg(self):
        return Action.get_text(self, By.XPATH, UserManagement.toast_msg_txt)

    main_searchbar = "//input[@id='main-input']"

    def search_button(self, value):
        return Action.send_keys(self, By.XPATH, UserManagement.main_searchbar, value)

    list_first_name = "(//div/span[contains(@class,'align-items-center')]/a)[1]"

    def get_first_list_name(self):
        return Action.get_text(self, By.XPATH, UserManagement.list_first_name)

    def click_first_list_user(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.list_first_name)

    deactivate_btn ="//div[contains(@class,'cy-switch-btn__ball')]//span[contains(@class,'cyicon-check')]"

    def click_deactivate_user(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.deactivate_btn)

    update_btn = "//div[contains(@class,'cy-right-model__footer')]//button[contains(text(),'Update')]"

    def click_update_btn(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.update_btn)

    search_bar_clear_btn = "//div[contains(@class,'clear-button')]"

    def click_on_search_clear_btn(self):
        return Action.wait_and_click(self, By.XPATH, UserManagement.search_bar_clear_btn)








