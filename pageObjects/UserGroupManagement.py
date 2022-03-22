import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class UserGroupManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_user_group_management = "//p[contains(text(),'User Group')]/parent::div/parent::div"

    def click_user_group_management(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.tab_user_group_management)

    tab_active = "//div[contains(@class,'tabs--list')]//li[2]/a"

    def click_on_active_tab(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_active)


    tab_inactive = "//div[@class='px-2 tabs--list my-2']//li[3]/a"

    def click_inactive_tab(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_inactive)

    def get_inactive_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_inactive, 'color')

    tab_all = "//div[contains(@class,'tabs--list')]//li[1]/a"

    def click_all_tab(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_all)

    def get_all_tab_color(self):
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_all, 'color')

    btn_add_user_group = "//header//button"

    def click_add_user_group(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_add_user_group)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_slider_close)

    def click_Update_slider_close(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_update_slider_close)

    btn_update = "//button[@class='cy-button cy-button--primary cy-button--md']"

    def check_update_button(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.btn_update)

    def click_update_button(self):
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_update)

    usergroup_title = "(//div[@class='user-group__list']//div[contains(@class,'app-card-body')])[1]//h3"

    def click_on_header(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.usergroup_title)

    def get_User_Group_Name(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.usergroup_title)

    def check_visibility_of_first_group(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserGroupManagement.usergroup_title)

    def check_visibility_of_first_group_by_name(self, group_name):
        return Action.read_search_result(self, By.XPATH, UserGroupManagement.usergroup_title,group_name)


    user_title = "//input[@aria-placeholder='Title *']"

    def put_usergroup_name(self, value):
        return Action.send_keys(self, By.XPATH, UserGroupManagement.user_title, value)

    def clear_usergroup_name(self):
        return Action.clear_field(self, By.XPATH, UserGroupManagement.user_title)

    create_btn = "//button[@class='cy-button cy-button--primary cy-button--md']"

    def click_create_button(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.create_btn)

    main_searchbar = "//input[@id='main-input']"

    def search_button(self, value):
        return Action.send_keys(self, By.XPATH, UserGroupManagement.main_searchbar, value)

    search_bar_clear_btn = "//div[contains(@class,'clear-button')]"

    def click_on_search_clear_btn(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.search_bar_clear_btn)

    toggle_active = "(//div[@class='el-form-item__content'])[4]//span[@class='cyicon-cross']"

    def click_activate_toggle(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.toggle_active)

    toggle_status = "//p[@class='m-0 subtitle ml-2 font-size-14']"

    def check_toggle_status(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.toggle_status)

    Usergroup_count = "// h1[contains(text(), 'User Group Management (')]"

    def get_usergroup_count(self):
        return Action.get_count_from_string(self, By.XPATH, UserGroupManagement.Usergroup_count)

    description = "//div[contains(@class,'cy-textarea')]/textarea"

    def put_usergroup_description(self, value):
        return Action.send_keys(self, By.XPATH, UserGroupManagement.description, value)

    def clear_usergroup_description(self):
        return Action.clear_field(self, By.XPATH, UserGroupManagement.description)

    add_user_btn = "//div/span[contains(@class,'cyicon-chevron-down')]"

    def click_dropdown_users(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.add_user_btn)

    search_user = "//div[contains(@class,' justify-content-start multiple')]"

    def search_user_in_dropdown(self, value):
        return Action.send_keys(self, By.XPATH, UserGroupManagement.search_user, value)

    toggle_enable = "//div[contains(@class,'justify-content-end')]//span[@class='cyicon-cross']"

    def click_enable_all_permissions(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.toggle_enable)

    status = "//div[contains(@class,'justify-content-end')]//span[contains(@class,'cy-switch-btn-wrapper__label')]"

    def check_permission_status(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.status)

    more_options = "//span[contains(@class,'float-right more-options')]"

    def click_more_option(self):
        return Action.mouse_hover_on_element(self, By.XPATH, UserGroupManagement.more_options)

    edit_option = "(//ul[contains(@class,'menu-dropdown')]/li)[1]"

    def click_edit_option(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.edit_option)

    clone_option = "(//ul[contains(@class,'menu-dropdown')]/li)[2]"

    def click_clone_usergroup(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.clone_option)

    deactive_toggle = "(//span[contains(@class,'cyicon-check')])[1]"

    def click_deactivate_usergroup(self):
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.deactive_toggle)

    close_tooltip_btn = "//div[contains(@class,'notification__closeBtn')]"

    def click_close_tooltip(self):
        return Action.normal_click(self, By.XPATH, UserGroupManagement.close_tooltip_btn)

    toast_msg_txt = "//div[@role='alert']//span[2]/span[1]"

    def get_tooltip_msg(self):
        return Action.get_text(self, By.XPATH, UserGroupManagement.toast_msg_txt)
