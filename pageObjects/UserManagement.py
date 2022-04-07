from selenium.webdriver.common.by import By

from utilities.Actions import Action


class UserManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_user_management = "//p[contains(text(),'User Management')]/parent::div/parent::div"

    def click_user_management(self):
        """
            Click on user management
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_user_management)

    user_count = "//h1[contains(text(),'User Management (')]"

    def get_user_count(self):
        """
            Get total user count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, UserManagement.user_count)

    first_active_user = "(//span[text()='Active' and @class='status__text'])[1]"

    def Pass_even_first_active_User_is_not_visible(self):
        """
            Visibility of first active user
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_active_user)

    first_inactive_user = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def Pass_even_first_inactive_User_is_not_visible(self):
        """
            Visibility of first inactive user
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, UserManagement.first_inactive_user)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on Inactive tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_inactive)

    def get_inactive_tab_color(self):
        """
            Get inactive tab color
            :return: 
        """
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_inactive, 'color')

    tab_All = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.tab_All)

    def get_all_tab_color(self):
        """
            Get all tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, UserManagement.tab_All, 'color')

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.tab_active)

    btn_new_user = "//header//div[3]/button"

    def click_add_user(self):
        """
            Click on add user
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_new_user)

    btn_export_user = "//header//div[@class='el-dropdown']/button"

    def click_export(self):
        """
            Click on export
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_export_user)

    drpdwn_export_option = "//li[text()='CSV']"

    def export_option_visibility(self):
        """
            Export option visibility
            :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, UserManagement.drpdwn_export_option)

    text_slider_title = "//div[text()='User']"

    def get_slider_title(self):
        """
            Get slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, UserManagement.text_slider_title)

    btn_slider_close = "//span[@data-testaction='slider-close']"

    def click_slider_close(self):
        """
            Click slider close button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, UserManagement.btn_slider_close)

    First_name = "//label[@for='first_name']/parent::div//input"

    def put_first_name(self, value):
        """
            Put first name on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserManagement.First_name, value)

    def clear_first_name(self):
        """
            Clear first name text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, UserManagement.First_name)

    Last_name = "//label[@for='last_name']/parent::div//input"

    def put_last_name(self, value):
        """
            put last name on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserManagement.Last_name, value)

    def clear_last_name(self):
        """
            clear last name on text field
            :return:
        """
        return Action.clear_field(self, By.XPATH, UserManagement.Last_name)

    drop_down_btn = "//div[@name='groups']//span[contains(@class,'chevron-down')]"

    def click_dropdown(self):
        """
            Click dropdown
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.drop_down_btn)

    top_first_usergroup = "(//div[@name='groups']//ul//li)[1]"

    def click_top_user_group(self):
        """
            Click top user group
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.top_first_usergroup)

    user_name = "//label[@for='username']/parent::div//input"

    def put_user_name(self, value):
        """
            Put username on text field
            :param value:
            :return:
        """
        user_name = Action.convert_string_to_lower(self, value)
        return Action.send_keys(self, By.XPATH, UserManagement.user_name, user_name)

    user_email = "//label[@for='email']/parent::div//input"

    def put_user_email(self, value):
        """
            Put user email on text field
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserManagement.user_email, value)

    create_user_btn = "//button[contains(text(),'Create')]"

    def click_create_user_btn(self):
        """
            Click on create user button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.create_user_btn)

    main_searchbar = "//input[@id='main-input']"

    def Put_string_in_search_bar(self, value):
        """
            Search bar input field used to search
            :param- value
            :return:
        """
        return Action.send_keys(self, By.XPATH, UserManagement.main_searchbar, value)

    list_first_name = "(//tr//td[1]//a)[1]"

    def get_first_user_name_in_list(self):
        """
            Get first list name
            :return:
        """
        return Action.get_text(self, By.XPATH, UserManagement.list_first_name)

    def visibility_of_created_user(self):
        """
        Wait until Visibility of created user
        :return:
        """
        return Action.check_visibility_of_element(self, By.XPATH, UserManagement.list_first_name)

    def click_first_user_in_listing(self):
        """
            Click first list username
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.list_first_name)

    deactivate_btn = "//div[contains(@class,'cy-switch-btn__ball')]//span[contains(@class,'cyicon-check')]"

    def click_deactivate_user(self):
        """
            Click deactivate user
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.deactivate_btn)

    update_btn = "//button[contains(text(),'Update')]"

    def click_update_btn(self):
        """
            Click update button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.update_btn)

    search_bar_clear_btn = "//div[contains(@class,'clear-button')]"

    def click_on_search_clear_btn(self):
        """
            Click on search clear button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.search_bar_clear_btn)

    export_users = "//ul[contains(@class,'el-dropdown-menu--small')]/li"

    def click_on_csv_btn(self):
        """
            Click on csv button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.export_users)

    def visibility_of_user_in_usergroup(self, user_name):
        """
            Visibility of user in usergroup
            :param user_name:
            :return:
        """
        path = "//ul/li//div[contains(@class,'cy-select-menu-option--multiple')]//div[contains(text(),'" + user_name + "')]"
        return Action.check_visibility_of_element(self, By.XPATH, path)

    def visibility_of_user(self, user_name):
        """
            Visibility of users
            :param user_name:
            :return:
        """
        path = "//ul/li//div[contains(@class,'cy-width-inherit')]//div[contains(text(),'" + user_name + "')]"
        return Action.check_visibility_of_element(self, By.XPATH, path)

    bot_user = "//span[contains(text(),'Bot User')]/parent::div"

    def check_bot_user(self):
        """
            Check bot user
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, UserManagement.bot_user)
