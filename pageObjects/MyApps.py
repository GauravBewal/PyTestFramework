import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class MyApps(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    tab_app_store = "//span[@class='tab__count']/parent::a[@href='/soar/app/list/app-store']"

    def app_store_tab(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.tab_app_store)

    text_page_heading = "//header//h1"

    def get_page_heading(self):
        return Action.get_text(self, By.XPATH, MyApps.text_page_heading)

    total_app_count = "//a[@href='/soar/app/list/my-apps']/span"

    def get_app_count(self):
        return Action.get_count_from_string(self, By.XPATH, MyApps.total_app_count)

    items_per_page_arrow_btn = "//i[contains(@class,'icon-arrow-up')]/parent::span/parent::span"

    def click_on_items_per_page_arrow(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.items_per_page_arrow_btn)

    dd_100_items_per_page_option = "//span[text()='100/page']/parent::li"

    def click_on_100_items_per_page_option(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.dd_100_items_per_page_option)

    app_install_btn = "(//button[contains(text(),'Install')])[1]"

    app_store_pagination = "//button[@class='btn-next']"

    def click_on_install_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.app_install_btn)

    def scroll_to_install_btn_view(self):
        return Action.Apply_Pagination_if_element_not_found(self, By.XPATH, MyApps.app_install_btn,
                                                            MyApps.app_store_pagination)

    txt_app_name = "(//button[contains(text(),'Install')])[1]/ancestor::div[4]" \
                   "//div[contains(@class,'title--header')]/h3"

    def get_installing_app_name(self):
        return Action.get_text(self, By.XPATH, MyApps.txt_app_name)

    def scroll_to_install_app_heading(self):
        return Action.scroll_to_element_view(self, self.driver.find_element(By.XPATH, MyApps.txt_app_name))

    install_app_slider_title = "//div[contains(@class,'app-update')]//div[@class='ellipsis']"

    def get_install_app_slider_title(self):
        return Action.get_text(self, By.XPATH, MyApps.install_app_slider_title)

    slider_install_btn = "//div[contains(@class,'app-update')]//button"

    def click_slider_install_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.slider_install_btn)

    toast_msg_txt = "//div[@role='alert']//span[2]/span[1]"

    def get_tooltip_msg(self):
        return Action.get_text(self, By.XPATH, MyApps.toast_msg_txt)

    def get_first_3_letter_of_downloaded_app(self, downloaded_app_name):
        first_3_letters = downloaded_app_name.lower()
        return first_3_letters[0:3]

    def verify_error_msg_visibility(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.toast_msg_txt)

    read_search_result_after_uninstall = "//div[@class='apps-container']//h1"

    def get_search_result_after_uninstall(self):
        return Action.get_text(self, By.XPATH, MyApps.read_search_result_after_uninstall)

    confirm_uninstall_app = "(//div[@class='footer float-left']/button)[1]"

    def click_confirm_uninstall_app(self):
        return Action.javascript_click(self, By.XPATH, MyApps.confirm_uninstall_app)

    more_options_dropdown = "//div[@class='el-dropdown']/span/i"

    def mouse_hover_on_more_Actions(self):
        time.sleep(3)
        return Action.mouse_hover_on_element(self, By.XPATH, MyApps.more_options_dropdown)

    uninstall_app_button = "//li[text()='Uninstall App']"

    def click_on_uninstall_app(self):
        return Action.javascript_click(self, By.XPATH, MyApps.uninstall_app_button)

    def visibility_of_uninstall_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.uninstall_app_button)

    default_instance = "//div[contains(text(),'Default Instance')]/preceding-sibling::div"

    def read_default_instance(self):
        return Action.get_text(self, By.XPATH, MyApps.default_instance)

    instance_name_textbox = "//input[@placeholder='Enter Instance Name']"

    def enter_instance_name(self, instance_name):
        return Action.send_keys(self, By.XPATH, MyApps.instance_name_textbox, instance_name)

    cftr_base_url_field = "//input[@placeholder='Enter Base URL']"

    def enter_cftr_base_url(self, base_url):
        return Action.send_keys(self, By.XPATH, MyApps.cftr_base_url_field, base_url)

    cftr_access_id_field = "//input[@placeholder='Enter Access ID']"

    def enter_cftr_access_key(self, access_key):
        return Action.send_keys(self, By.XPATH, MyApps.cftr_access_id_field, access_key)

    cftr_secret_key_field = "//input[@placeholder='Enter Secret Key']"

    def enter_cftr_secret_key(self, secret_key):
        return Action.send_keys(self, By.XPATH, MyApps.cftr_secret_key_field, secret_key)

    instance_connectivity_slider_close = "//span[@data-testaction='slider-close']"

    def click_instance_connectivity_slider_close(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.instance_connectivity_slider_close)

    filter_btn = "//button[contains(@class,'filter')]"

    def click_on_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.filter_btn)

    collapse_expand_btn = "//span[contains(@class,'expand-collapse-button')]"

    def click_collapse_and_expand_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.collapse_expand_btn)

    published_tab = "//div[contains(text(),'Published')]"

    def click_on_published_tab(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.published_tab)

    cyware_published_filter_radio_btn = "//span[contains(text(),'Cyware') and @class='item__title']" \
                                        "/preceding-sibling::div"

    def click_on_cyware_published_filter(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.cyware_published_filter_radio_btn)

    applied_filter_title = "//div[contains(@class,'applied-filters')]/span"

    def get_applied_filter_title(self):
        return Action.get_text(self, By.XPATH, MyApps.applied_filter_title)

    instance_description_textbox = "//textarea[@placeholder='Enter Instance Description']"

    def enter_instance_description(self, description):
        return Action.send_keys(self, By.XPATH, MyApps.instance_description_textbox, description)

    slider_instance_creation_button = "//button[text()='Create']"

    def click_slider_instance_create_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.slider_instance_creation_button)

    app_actions_tab = "//a[contains(@href,'/action/list')]"

    def click_app_actions_tab(self):
        return Action.javascript_click(self, By.XPATH, MyApps.app_actions_tab)

    button_new_instance = "//div[@class='app-summary__actions-header--wrapper']//button"

    def click_on_new_instance_btn(self):
        return Action.javascript_click(self, By.XPATH, MyApps.button_new_instance)

    txt_app_version = "//span[contains(@class,'version-selector__active')]"

    def get_app_version(self):
        return Action.get_text(self, By.XPATH, MyApps.txt_app_version)

    input_instance_name_field = "//input[@placeholder='Enter Instance Name']"

    def Enter_new_instance(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.input_instance_name_field, value)

    input_base_url_field = "//input[@placeholder='Enter Base URL']"

    def enter_base_url(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.input_base_url_field, value)

    input_access_key = "//input[@placeholder='Enter Access Key']"

    def enter_access_key(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.input_access_key, value)

    input_secret_key = "//input[@placeholder='Enter Secret Key']"

    def enter_secret_key(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.input_secret_key, value)

    app_instance_tab = "//a[contains(@href,'/instance/list')]"

    def click_app_instance_tab(self):
        return Action.javascript_click(self, By.XPATH, MyApps.app_instance_tab)

    def mouse_hover_on_created_instance(self, instance_name):
        path = "//div[contains(text(),'" + instance_name + "')]"
        return Action.mouse_hover_on_element(self, By.XPATH, path)

    test_instance_btn = "//button[contains(text(),' Test Instance')]"

    def click_on_test_instance_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.test_instance_btn)

    test_connectivity_msg = "//img[@src='/soar/test-connection-success.svg']"

    def visibility_of_successful_test_connectivity(self):
        time.sleep(10)
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.test_connectivity_msg)

    app_playbooks_tab = "//a[contains(@href,'/playbook/list')]"

    def click_app_playbooks_tab(self):
        return Action.javascript_click(self, By.XPATH, MyApps.app_playbooks_tab)

    app_title = "//div[@class='app-card-v2__header']//h3"

    def read_app_title(self):
        return Action.get_text(self, By.XPATH, MyApps.app_title)

    listing_back_btn = "//div[contains(@class,'back-button')]"

    def click_back_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.listing_back_btn)

    app_listing_more_options = "(//div[@class='el-dropdown']//div[contains(@class,'more-options')])[1]"

    def mouse_hover_list_more_options(self):
        return Action.mouse_hover_on_element(self, By.XPATH, MyApps.app_listing_more_options)

    clone_app_btn = "//ul[@x-placement='bottom-end']//li[contains(text(),'Clone App')]"

    def click_clone_app_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.clone_app_btn)

    def visibility_of_clone_app_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.clone_app_btn)

    clone_slider_button = "//div[contains(@class,'app-export')]//button[contains(text(),'Clone App')]"

    def click_clone_btn_on_slider(self):
        return Action.click_if_element_found(self, By.XPATH, MyApps.clone_slider_button)

    clone_page_heading_txt = "//h1[contains(text(),'Clone App')]"

    def get_clone_page_heading(self):
        return Action.get_text(self, By.XPATH, MyApps.clone_page_heading_txt)

    cloned_app_name = "//span[contains(@class,'app-edit__view--title')]"

    def get_cloned_app_name(self):
        return Action.get_text(self, By.XPATH, MyApps.cloned_app_name)

    active_app = "//div[@class='app-edit__view']//span//button"

    def click_active_app(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.active_app)

    top_1_search_result = "(//div[@class='apps-container']//h3)[1]"

    def top_first_search(self, app_name):
        return Action.read_search_result(self, By.XPATH, MyApps.top_1_search_result, app_name)

    def click_first_search_result(self):
        return Action.javascript_click(self, By.XPATH, MyApps.top_1_search_result)

    def visibility_of_first_app(self):
        return Action.Pass_even_element_not_visible(self, By.XPATH, MyApps.top_1_search_result)

    search_app = "//input[@placeholder='Search App(s)']"

    def search_for_app(self, app_name):
        return Action.send_keys(self, By.XPATH, MyApps.search_app, app_name)

    app_status = "(//span[@class='status__text' and text()='Installed'])[1]"

    def Verify_app_installed_or_not(self):
        return Action.check_app_is_installed_or_not(self, By.XPATH, MyApps.app_status, MyApps.app_install_btn,
                                                    MyApps.slider_install_btn)

    app_name_textbox = "//input[@placeholder='Enter App Name']"

    def enter_app_name(self, app_name):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.send_keys(self, By.XPATH, MyApps.app_name_textbox, app_name)

    supported_api_version_textbox = "//input[@placeholder='Enter Supported API Versions']"

    def enter_supported_api_version(self, version):
        return Action.send_keys(self, By.XPATH, MyApps.supported_api_version_textbox, version)

    button_app_refresh = "//i[contains(@class,'icon-map-gear')]/parent::div"

    def click_app_refresh_button(self):
        return Action.javascript_click(self, By.XPATH, MyApps.button_app_refresh)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.normal_click(self, By.XPATH, MyApps.tooltip_close)

    list_view_btn = "//span[contains(@class,'list-button')]"

    def click_on_list_view_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.list_view_btn)

    first_app_in_list_view = "(//div[contains(@class,'list-layout')]//h3)[1]"

    def visibility_of_app_in_list_view(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.first_app_in_list_view)

    clear_search_btn = "//i[contains(@class,'search-input__close')]/parent::span"

    def click_clear_search_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.clear_search_btn)

    button_app_save = "//div[@class='app-edit__view']//div[3]/button"

    def click_save_app_button(self):
        return Action.javascript_click(self, By.XPATH, MyApps.button_app_save)

    dd_edit_btn = "//ul[@x-placement='bottom-end']//li[contains(text(),'Edit App')]"

    def click_on_edit_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.dd_edit_btn)

    def visibility_of_edit_button(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.dd_edit_btn)

    dd_export_btn = "//ul[@x-placement='bottom-end']//li[contains(text(),'Export App')]"

    def visibility_of_export_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, MyApps.dd_export_btn)

    def click_on_export_btn(self):
        return Action.javascript_click(self, By.XPATH, MyApps.dd_export_btn)

    run_btn = "//i[contains(@class,'cyicon-play')]/parent::div"

    def click_on_run_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.run_btn)

    dd_instance_field = "(//span[contains(@class,'cyicon-chevron-down')]/parent::div)[1]"

    def click_on_instance_field(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.dd_instance_field)

    dd_action_field = "(//span[contains(@class,'cyicon-chevron-down')]/parent::div)[2]"

    def click_on_action_field(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.dd_action_field)

    input_field = "//input[contains(@placeholder,'Search')]"

    def put_instance_name(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.input_field, value)

    def put_action_name(self, value):
        time.sleep(3)
        return Action.send_keys(self, By.XPATH, MyApps.input_field, value)

    debug_app_first_option_in_list = "(//form//ul/li)[1]"

    def select_first_instance(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.debug_app_first_option_in_list)

    def get_first_instance_name_after_search(self, value):
        return Action.read_search_result(self, By.XPATH, MyApps.debug_app_first_option_in_list, value)

    def get_first_action_name_after_search(self, action_name):
        return Action.read_search_result(self, By.XPATH, MyApps.debug_app_first_option_in_list, action_name)

    def select_first_action(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.debug_app_first_option_in_list)

    debug_incident_title_input_field = "//div[contains(@class,'action-input')]" \
                                       "//textarea[contains(@placeholder,'title')]"

    def put_incident_title_field_value(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.debug_incident_title_input_field, value)

    debug_incident_description_field_value = "//div[contains(@class,'action-input')]" \
                                             "//textarea[contains(@placeholder,'escription')]"

    def put_incident_description(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.debug_incident_description_field_value, value)

    debug_incident_status_field = "//div[contains(@class,'action-input')]//textarea[contains(@placeholder,'status')]"

    def put_incident_status(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.debug_incident_status_field, value)

    debug_incident_severity_level_field = "//div[contains(@class,'action-input')]" \
                                          "//textarea[contains(@placeholder,'level')]"

    def put_incident_severity_level(self, value):
        return Action.send_keys(self, By.XPATH, MyApps.debug_incident_severity_level_field, value)

    debug_button_test = "//button[contains(text(),'Test')]"

    def click_on_debug_test_btn(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.debug_button_test)

    debug_console_status = "//div[contains(@class,'debug-console')]//div"

    def get_debug_console_status(self):
        time.sleep(20)
        return Action.get_text(self, By.XPATH, MyApps.debug_console_status)

    debug_result_data = "//div[contains(@class,'debug-console')]//pre"

    def get_debug_result_data(self):
        return Action.get_text(self, By.XPATH, MyApps.debug_result_data)

    tab_my_apps = "//span[@class='tab__count']/parent::a[@href='/soar/app/list/my-apps']"

    def My_Apps_Tab(self):
        return Action.javascript_click(self, By.XPATH, MyApps.tab_my_apps)

    button_import_package = "//i[contains(@class,'icon-import')]/parent::button"

    def click_on_import_button(self):
        return Action.wait_and_click(self, By.XPATH, MyApps.button_import_package)

    app_input_field = "//input[@type='file']"

    def send_file_path_to_upload_input_field(self, file_path):
        return Action.send_keys_to_hidden_upload_element(self, By.XPATH, MyApps.app_input_field, file_path)

    button_create_new_app = "//i[contains(@class,'icon-plus')]/parent::button"

    def Create_App_button(self):
        return Action.javascript_click(self, By.XPATH, MyApps.button_create_new_app)

    button_app_walkthrough = "(//div[@slot='header']//button)[3]"

    def Click_walkthrough_button(self):
        return Action.javascript_click(self, By.XPATH, MyApps.button_app_walkthrough)

    walkthrough_tooltip_count = "//div[@class='introjs-helperNumberLayer']"

    def get_tooltip_count(self):
        return Action.javascript_click(self, By.XPATH, MyApps.walkthrough_tooltip_count)

    walkthrough_tooltip_next_btn = "//a[contains(@class,'introjs-nextbutton')]"

    def click_on_next_btn(self):
        return Action.javascript_click(self, By.XPATH, MyApps.walkthrough_tooltip_next_btn)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, MyApps.close_walkthrough_tooltip)
