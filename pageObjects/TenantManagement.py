from selenium.webdriver.common.by import By

from utilities.Actions import Action


class TenantManagement(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_tenant_management = "//p[contains(text(),'Tenant Management')]/parent::div/parent::div"

    def click_tenant_management(self):
        """
            Click on tenant Management
            :return:
        """
        return Action.javascript_click(self, By.XPATH, TenantManagement.tab_tenant_management)

    tab_inactive = "//li/a[contains(text(),'Inactive')]"

    def click_inactive_tab(self):
        """
            Click on inactive tab
            :return:
        """
        return Action.javascript_click(self, By.XPATH, TenantManagement.tab_inactive)

    tab_active = "//li/a[contains(text(),'Active')]"

    def click_active_tab(self):
        """
            Click on active tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, TenantManagement.tab_active)

    def get_inactive_tab_color(self):
        """
            Get Inactive tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, TenantManagement.tab_inactive, 'color')

    tab_all = "//li/a[contains(text(),'All')]"

    def click_all_tab(self):
        """
            Click on all tab
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, TenantManagement.tab_all)

    def get_all_tab_color(self):
        """
            Get all tab color
            :return:
        """
        return Action.get_css_property_value(self, By.XPATH, TenantManagement.tab_all, 'color')

    tenant_count = "//h1[contains(text(),'Tenant Management (')]"

    def get_tenant_count(self):
        """
            Get tenant count
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, TenantManagement.tenant_count)

    first_active_tenant = "(//span[text()='Active' and @class='status__text'])[1]"

    def Pass_even_first_active_Tenant_is_not_visible(self):
        """
            Visibility of first active tenant
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, TenantManagement.first_active_tenant)

    first_inactive_tenant = "(//span[text()='Inactive' and @class='status__text'])[1]"

    def Pass_even_first_inactive_Tenant_is_not_visible(self):
        """
            Visibility of first inactive tenant
            :return:
        """
        return Action.Pass_even_element_not_visible(self, By.XPATH, TenantManagement.first_inactive_tenant)

    btn_new_tenant = "//header//button"

    def click_new_tenant(self):
        """
            Click on new tenant
            :return:
        """
        return Action.javascript_click(self, By.XPATH, TenantManagement.btn_new_tenant)

    text_slider_title = "//div[@class='modal--header']//span"

    def get_slider_title(self):
        """
            Get Slider title
            :return:
        """
        return Action.get_text(self, By.XPATH, TenantManagement.text_slider_title)

    btn_slider_close = "//div[@class='modal--header']//i"

    def click_slider_close(self):
        """
            Click on slider close button
            :return:
        """
        return Action.javascript_click(self, By.XPATH, TenantManagement.btn_slider_close)

    tenant_count = "//h1[contains(text(),'Tenant Management (')]"

    def get_count_of_tenants(self):
        """
            Get count of tenants
            :return:
        """
        return Action.get_count_from_string(self, By.XPATH, TenantManagement.tenant_count)

    tenant_name = "(//div[contains(@class,'cy-input ')]/input)[1]"

    def put_tenant_name(self, value):
        """
            Put tenant name
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, TenantManagement.tenant_name, value)

    domain_name = "(//div[contains(@class,'cy-input ')]/input)[2]"

    def put_domain_name(self, value):
        """
            Put domain name
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, TenantManagement.domain_name, value)

    Save_btn = "//div[contains(@class,'add-tenant')]//button[text()='Save']"

    def click_save_btn(self):
        """
            Click on save button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, TenantManagement.Save_btn)

    continue_using_co_btn = "//div[contains(@class,'configuring')]//button"

    def click_continue_using_co_btn(self):
        """
            Click on continue using co button
            :return:
        """
        return Action.wait_and_click(self, By.XPATH, TenantManagement.continue_using_co_btn)

    main_input = "//input[@id='main-input']"

    def search_input_string(self, value):
        """
            Search input string
            :param value:
            :return:
        """
        return Action.send_keys(self, By.XPATH, TenantManagement.main_input, value)

    def click_enter_for_search(self):
        """
            Click on enter for search
            :return:
        """
        return Action.click_enter(self)

    first_tenant_name = "(//tr[@class='el-table__row']//a)[1]"

    def get_name_first_tenant(self):
        """
            Get name of first tenant
            :return:
        """
        return Action.get_text(self, By.XPATH, TenantManagement.first_tenant_name)

    def visibility_of_created_Tenant(self):
        return Action.check_visibility_of_element(self, By.XPATH, TenantManagement.first_tenant_name)

