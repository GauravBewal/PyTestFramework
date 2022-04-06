import time

from selenium.webdriver.common.by import By
from utilities.Base import Base
from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class UserGroupManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    tab_user_group_management = "//p[contains(text(),'User Group')]/parent::div/parent::div"

    def click_user_group_management(self):
        """
            Click on user group management
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.tab_user_group_management)

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_on_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_active)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"


    def click_inactive_tab(self):
        """
            Click on inactive tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_inactive)

    def get_inactive_tab_color(self):
        """
            Get inactive tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_inactive, 'color')

    tab_all = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.tab_all)

    def get_all_tab_color(self):
        """
            Get all tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, UserGroupManagement.tab_all, 'color')

    btn_add_user_group = "//header//button"

    def click_add_user_group(self):
        """
            Click on add user group
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_add_user_group)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        """
            Get slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, UserGroupManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        """
            Click on slider close button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_slider_close)

    def click_Update_slider_close(self):
        """
            Click on update slider close button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_update_slider_close)

    btn_update = "//button[@class='cy-button cy-button--primary cy-button--md']"

    def check_update_button(self):
        """
            Check update button
            :return:
        """
        return Action.get_text(self, By.XPATH, UserGroupManagement.btn_update)

    def click_update_button(self):
        """
            Click on update button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserGroupManagement.btn_update)

    usergroup_title = "(//div[@class='user-group__list']//div[contains(@class,'app-card-body')])[1]//h3"

    def get_User_Group_Name(self):
        """
            Get user group name
            :return:
        """
        return Action.get_text(self, By.XPATH, UserGroupManagement.usergroup_title)

    def visibility_of_created_usergroup(self):
        return Action.check_visibility_of_element(self, By.XPATH, UserGroupManagement.usergroup_title)

    first_active_usergroup = "(//div[contains(@class,'app-card')]//span[text()='ACTIVE'])[1]"

    def Pass_even_first_Active_usergroup_is_not_visible(self):
        """
            Visibility of first active usergroup
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserGroupManagement.first_active_usergroup)

    first_inactive_usergroup = "(//div[contains(@class,'app-card')]//span[text()='INACTIVE'])[1]"

    def Pass_even_first_inactive_usergroup_is_not_visible(self):
        """
            Visibility of first inactive usergroup
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserGroupManagement.first_inactive_usergroup)

    user_title = "//input[@aria-placeholder='Title *']"

    def put_usergroup_name(self, value):
        """
            Put usergroup name on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserGroupManagement.user_title, value)

    def clear_usergroup_name(self):
        """
            Clear usergroup name text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, UserGroupManagement.user_title)

    create_btn = "//button[@class='cy-button cy-button--primary cy-button--md']"

    def click_create_button(self):
        """
            Click on create button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.create_btn)

    main_searchbar = "//input[@id='main-input']"

    def Put_String_to_Search(self, value):
        """
            Enter string to search
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserGroupManagement.main_searchbar, value)

    def click_enter_to_search(self):
        """
            Click on enter to search
            :return:
        """
        return Action.Press_enter(self)

    search_bar_clear_btn = "//div[contains(@class,'clear-button')]"

    def click_on_search_clear_btn(self):
        """
            Click on search clear button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.search_bar_clear_btn)

    toggle_active = "(//div[@class='el-form-item__content'])[4]//span[@class='cyicon-cross']"

    def click_activate_toggle(self):
        """
            Click on activate toggle button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.toggle_active)

    enable_all_permissions = "//span[text()='Enable All']/parent::div//span[@class='cyicon-cross']"

    def click_on_enable_all_permissions_btn(self):
        """
            Click on enable all permission button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.enable_all_permissions)

    toggle_status = "//p[@class='m-0 subtitle ml-2 font-size-14']"

    def check_toggle_status(self):
        """
            Check toggle status
            :return:
        """
        return Action.get_text(self, By.XPATH, UserGroupManagement.toggle_status)

    Usergroup_count = "// h1[contains(text(), 'User Group Management (')]"

    def get_usergroup_count(self):
        """
            Get total usergroups count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, UserGroupManagement.Usergroup_count)

    description = "//div[contains(@class,'cy-textarea')]/textarea"

    def put_usergroup_description(self, value):
        """
            Put usergroup description on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserGroupManagement.description, value)

    def clear_usergroup_description(self):
        """
            Clear usergroup description text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, UserGroupManagement.description)

    add_user_btn = "//div/span[contains(@class,'cyicon-chevron-down')]"

    def click_dropdown_users(self):
        """
            Click dropdown users list
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.add_user_btn)

    search_user = "//div[contains(@class,' justify-content-start multiple')]"

    def search_user_in_dropdown(self, value):
        """
            Search user in dropdown
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserGroupManagement.search_user, value)

    toggle_enable = "//div[contains(@class,'justify-content-end')]//span[@class='cyicon-cross']"

    def click_enable_all_permissions(self):
        """
            Click on enable all permissions
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.toggle_enable)

    status = "//div[contains(@class,'justify-content-end')]//span[contains(@class,'cy-switch-btn-wrapper__label')]"

    def check_permission_status(self):
        """
            Check permission status
            :return:
        """
        return Action.get_text(self, By.XPATH, UserGroupManagement.status)

    more_options = "//span[contains(@class,'float-right more-options')]"

    def click_more_option(self):
        """
            Click more options
            :return:
        """
        return Action.mouse_hover_on_element(self, By.XPATH, UserGroupManagement.more_options)

    edit_option = "(//ul[contains(@class,'menu-dropdown')]/li)[1]"

    def click_edit_option(self):
        """
            Click edit option
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.edit_option)

    clone_option = "(//ul[contains(@class,'menu-dropdown')]/li)[2]"

    def click_clone_usergroup(self):
        """
            Click clone usergroup
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.clone_option)

    deactive_toggle = "(//span[contains(@class,'cyicon-check')])[1]"

    def click_deactivate_usergroup(self):
        """
            Click on deactivate usergroup
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserGroupManagement.deactive_toggle)
