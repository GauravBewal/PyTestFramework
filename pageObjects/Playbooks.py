import time
from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Playbooks(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    node_type_list = ['Action Nodes', 'Condition Nodes', 'Input Node', 'Memory Node']
    node_titles_list = ['App', 'Custom', 'Playbook', 'Regular', 'Custom', 'Regular', 'Regular']
    tooltip_titles = ['Playbook Overview', 'Add Node', 'Connect Nodes', 'Zoom and Auto-arrange Nodes',
                      'Save and Run']
    sort_options = ['Name', 'Modified', 'Created', 'ID', 'Last Run', 'Total Run']

    tab_cyware_playbooks = "//li[contains(@class,'cyware-playbook')]"

    def cyware_playbook_tab(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.tab_cyware_playbooks)

    tab_my_playbooks = "//li[contains(@class,'my-playbook')]/a"

    def my_playbook_tab(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.tab_my_playbooks)

    more_options_btn = "//div[@class='el-dropdown']/span"

    def mouse_hover_on_more_options(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.more_options_btn)

    playbook_clone_btn = "//i[@class='cyicon-copy']/parent::li"

    def check_visibility_of_clone_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.playbook_clone_btn)

    playbook_test_instances = "//i[@class='icon-connect']/parent::li"

    def click_on_test_instances_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_test_instances)

    playbook_test_instance_slider_text = "//span[@data-testaction='slider-close']/parent::div/" \
                                         "preceding-sibling::div/div"

    def get_test_instance_slider_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_test_instance_slider_text)

    instance_connection_result_tabs = (By.XPATH, "//div[@class='px-2 tabs--list']//li")

    def get_all_connection_result_tabs(self):
        return self.driver.find_elements(*Playbooks.instance_connection_result_tabs)

    test_instance_no_state_text = "//div[@class='h-100']//p"

    def get_test_instance_no_state_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.test_instance_no_state_text)

    test_instance_slider_close_btn = "//span[@data-testaction='slider-close']/parent::div"

    def click_test_instance_slider_close_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.test_instance_slider_close_btn)

    playbook_sort_options = "//span[@class='sort-tab']/div"

    def mouse_hover_sort_options(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.playbook_sort_options)

    available_sort_options = "//ul[contains(@class,'sort')]/li"

    def read_available_sort_options(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Playbooks.available_sort_options)

    def get_sort_options_title(self, path):
        return Action.get_text(self, By.XPATH, path)

    playbook_export_btn = "//i[@class='icon-export-boxed']/parent::li"

    def mouse_hover_export_btn(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.playbook_export_btn)

    playbook_export_as_png = "//li[contains(text(),'PNG')]"

    def check_visibility_export_as_png(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.playbook_export_as_png)

    playbook_export_as_json = "//li[contains(text(),'JSON')]"

    def check_visibility_export_as_json(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.playbook_export_as_json)

    btn_first_cyware_playbook = "//div[3]//tr[1]/td[2]//a"

    def click_first_playbook(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.btn_first_cyware_playbook)

    btn_first_my_playbook = "//div[3]//tr[1]/td[3]//a"

    def visibility_of_first_playbook(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.btn_first_my_playbook)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, Playbooks.close_walkthrough_tooltip)

    playbook_page_heading = "//header//h1"

    def get_manage_playbook_heading(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_page_heading)

    playbook_customize_table_btn = "//i[@class='cyicon-settings']/parent::div"

    def click_on_customize_table_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_customize_table_btn)

    customize_table_slider_title = "//span[@data-testaction='slider-close']/parent::div/preceding-sibling::div"

    def get_customize_table_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.customize_table_slider_title)

    close_customize_table = "//span[@data-testaction='slider-close']/parent::div"

    def click_close_customize_table_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.close_customize_table)

    playbook_create_btn = "//button[contains(@class,'create-playbook')]"

    def click_on_create_playbook_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_create_btn)

    playbook_back_btn = "//div[@class='playbook_header__view']//i[contains(@class,'icon-arrow-back')]"

    def click_on_back_button(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_back_btn)

    playbook_exit_without_save_btn = "//button[contains(text(),'Exit without Save')]"

    def click_exit_without_save(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_exit_without_save_btn)

    playbook_add_node_btn = "//div[@class='stencil-container walkthrough-stencil']"

    def click_add_node_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_add_node_btn)

    action_app_node_btn = "(//*[@data-type='cy.STENCILSHAPE'])[1]"

    playbook_background = "//div[@class='paper-scroller-background']/div"

    def drag_and_drop_action_app_node_by_position(self, width, height):
        return Action.drag_and_drop_by_offset(self, By.XPATH, Playbooks.action_app_node_btn, width, height)

    playbook_node_slider_text = "//div[@class='stencil-header']"

    def get_add_node_slider_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_node_slider_text)

    input_action_search = "//form/div[1]//input[@placeholder='Search and Select']"

    def put_app_name_to_search(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.input_action_search, value)

    def click_on_app_name_search(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.input_action_search)

    playbook_app_search_result = "//div[@class='app-action-picker__apps']/div[1]/div[1]//div[@role='button']//span"

    def click_app_search_result(self):
        time.sleep(5)
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_app_search_result)

    def select_action_version_based(self, version):
        version_id = Action.get_app_version_id(self, version)
        path = "//span[contains(text(),'" + version_id + "')]/parent::div/parent::li//div[contains(text()," \
                                                         "'Domain Search')]"
        return Action.wait_and_click(self, By.XPATH, path)

    txt_selected_node_name = "(//*[@model-id='1']/*[@joint-selector='label'])[1]"

    def get_selected_app_name(self, attribute):
        return Action.get_html_attribute_value(self, By.XPATH, Playbooks.txt_selected_node_name, attribute)

    playbook_node_title = "//div[contains(@class,'playbook-left-modal')]//div[contains(@class,'header__label')]/div"

    def get_playbook_node_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_node_title)

    all_node_type_title = "//div[@class='content']//h3"

    def get_all_node_type_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Playbooks.all_node_type_title)

    all_nodes_names = "//div[@class='content']//*[@class='v-line']"

    def get_all_node_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Playbooks.all_nodes_names)

    def get_list_of_elements(self, elements_count, elements):
        elements_list = []
        # indexing xpath and storing it in list
        for value in range(1, elements_count + 1):
            path = "(" + elements + ")[" + str(value) + "]"
            elements_list.append(path)
        return elements_list

    app_instance_field = "//span[contains(text(),'App Instance(s) *')]/following-sibling::div" \
                         "//div[contains(@class,'menu--label__container')]"

    def mouse_hover_on_instance_tab(self):
        time.sleep(8)
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.app_instance_field)

    instance_dropdown_icon = "//div[@class='playbook-left-modal__content']//div[contains(@class,'menu--chevron')]"

    def click_on_instance_dropdown(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.instance_dropdown_icon)

    clear_instance_field_btn = "//div[contains(@class,'menu--close-icon')]"

    def click_on_clear_instance_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.clear_instance_field_btn)

    app_instance_search_field = "//div[contains(@class,'search multiple')]/input"

    def put_instance_name(self, instance_name):
        return Action.send_keys(self, By.XPATH, Playbooks.app_instance_search_field, instance_name)

    instance_search_result = "//div//li[1]/span[contains(@class,'instance-list')]"

    def click_on_searched_instance(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.instance_search_result)

    test_instance_btn = "//span[contains(@class,'test-connectivity')]"

    def click_on_node_test_instance_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.test_instance_btn)

    instance_test_Again_btn = "//button[contains(text(),'Test Again')]"

    def visibility_of_test_again_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.instance_test_Again_btn)

    def click_on_instance_connectivity_close_btn(self, instance_name):
        path = "//span[contains(text(),'" + instance_name + "')]/following-sibling::button"
        return Action.wait_and_click(self, By.XPATH, path)

    test_connectivity_result = "//div[@class='instance__dialog-label']/span"

    def get_test_connectivity_result(self):
        return Action.get_text(self, By.XPATH, Playbooks.test_connectivity_result)

    action_input_data_tab = "//div[contains(text(),'Setup Input Data')]"

    def click_on_input_data_tab(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.action_input_data_tab)

    start_node = "//div[@id='playbook']//*[contains(text(),'Start')]"

    def mouse_hover_on_start_node(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.start_node)

    start_node_joint_port = "//div[@id='playbook']//*[@model-id='start']/*[@class='joint-port']"

    app_node_joint_port = "(//div[@id='playbook']//*[@model-id='1']//*[@class='joint-port'])[1]"

    def connect_start_node_and_app_node(self):
        return Action.click_and_hold_and_release_element(self, By.XPATH, Playbooks.start_node_joint_port,
                                                         Playbooks.app_node_joint_port)

    action_input_field = "//div[contains(@class,'action-input-params')]//textarea"

    def put_input_data(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.action_input_field, value)

    action_node_slider_close_btn = "//span[@data-testaction='slider-close']/parent::div"

    def click_on_slider_close_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.action_node_slider_close_btn)

    def get_node_type_title(self, path):
        return Action.get_text(self, By.XPATH, path)

    node_slider_close_btn = "//div[@class='stencil-close']"

    def click_on_node_close_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.node_slider_close_btn)

    playbook_name_field = "//input[@placeholder='Enter Name']"

    def enter_playbook_name(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.playbook_name_field, value)

    def remove_default_playbook_name(self):
        return Action.clear_field(self, By.XPATH, Playbooks.playbook_name_field)

    playbook_description_field = "//input[@placeholder='Enter Description']"

    def enter_playbook_description(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.playbook_description_field, value)

    save_more_options = "(//div[@class='el-button-group']/button)[2]"

    def mouse_hover_on_save_btn(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.save_more_options)

    save_and_run_btn = "//i[@class='icon-save-and-run']/parent::li"

    def get_save_and_run_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.save_and_run_btn)

    save_and_exit_btn = "//i[@class='icon-save-and-exit']/parent::li"

    def get_save_and_exit_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.save_and_exit_btn)

    def click_save_and_exit_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.save_and_exit_btn)

    playbook_walkthrough_bulb_btn = "//div[@class=' el-dropdown-selfdefine']/button"

    def click_walkthrough_bulb_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_walkthrough_bulb_btn)

    playbook_tooltip_walkthrough = "//i[contains(@class,'icon-refresh')]/ancestor::li"

    def click_on_tooltip_walkthrough_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_tooltip_walkthrough)

    def mouse_hover_on_tooltip_walkthrough_btn(self):
        return Action.mouse_hover_on_element(self, By.XPATH, Playbooks.playbook_tooltip_walkthrough)

    walkthrough_tooltip_count = "//div[@class='introjs-helperNumberLayer']"

    def get_tooltip_count(self):
        return Action.get_no_of_walkthrough_and_pagination_count(self, By.XPATH, Playbooks.walkthrough_tooltip_count)

    page_count = "//div[contains(@class,'footer-box')]//span[contains(text(),'of')]"

    def get_current_page_count(self):
        return Action.get_current_page_number(self, By.XPATH, Playbooks.page_count)

    grid_view_btn = "//span[contains(@class,'grid-button')]"

    def click_on_grid_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.grid_view_btn)

    def get_grid_icon_color(self):
        return Action.get_css_property_value(self, By.XPATH, Playbooks.grid_view_btn, 'color')

    walkthrough_tooltip_title = "//h1[@class='introjs-tooltip-title']"

    def get_tooltip_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.walkthrough_tooltip_title)

    walkthrough_tooltip_next_btn = "//a[contains(@class,'introjs-nextbutton')]"

    def click_on_next_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.walkthrough_tooltip_next_btn)

    playbook_video_walkthrough_btn = "//i[contains(@class,'icon-video')]/ancestor::li"

    def click_on_video_walthrough_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_video_walkthrough_btn)

    video_walkthrough_popup_title = "//h1[@class='introjs-tooltip-title']"

    def get_video_walkthrough_popup_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.video_walkthrough_popup_title)

    video_walkthrough_finish_btn = "//div[@class='introjs-tooltipbuttons']/a"

    def click_on_finish_button(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.video_walkthrough_finish_btn)

    textbox_search_playbook = "//header//div[contains(@class,'search-input')]/input"

    def search_playbooks(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.textbox_search_playbook, value)

    playbook_overview_btn = "//button[contains(@class,'playbook-overview-btn')]"

    def click_on_playbook_overview_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_overview_btn)

    playbook_overview_slider_title = "//div[text()='Overview']"

    def get_playbook_overview_slider_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_overview_slider_title)

    overview_output_parameters = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[1]"

    def click_on_output_parameters(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.overview_output_parameters)

    def get_output_parameter_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.overview_output_parameters)

    add_parameters_btn = "//div[@class='el-collapse-item is-active']//button"

    def click_on_add_parameter_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.add_parameters_btn)

    def visibility_of_add_parameter_btn(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.add_parameters_btn)

    parameter_key_field = "//textarea[@placeholder='Key']"

    def check_visibility_of_key_field(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.parameter_key_field)

    parameter_value_field = "//textarea[@placeholder='Value']"

    def check_visibility_of_value_field(self):
        return Action.check_visibility_of_element(self, By.XPATH, Playbooks.parameter_value_field)

    parameter_delete_btn = "//i[@class='cyicon-trash']/parent::button"

    def click_on_parameter_delete_btn(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.parameter_delete_btn)

    overview_playbook_data = "//div[contains(@class,'playbook-data')]/div[1]/div"

    def click_on_playbook_data(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.overview_playbook_data)

    associated_playbooks = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[2]"

    def click_on_associated_playbook(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.associated_playbooks)

    def get_associated_playbooks_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.associated_playbooks)

    no_state_validation_txt = "//div[@class='el-collapse-item is-active']//h1"

    def get_no_state_validation_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.no_state_validation_txt)

    associated_sub_playbooks = "//div[@class='el-collapse-item is-active']//label[2]"

    def switch_to_sub_playbooks_tab(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.associated_sub_playbooks)

    playbook_app_and_actions = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[3]"

    def click_apps_and_actions(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.playbook_app_and_actions)

    def get_apps_and_actions_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_app_and_actions)

    button_import_playbook = "//button[contains(@class,'import-playbook')]"

    def click_import_playbook(self):
        return Action.javascript_click(self, By.XPATH, Playbooks.button_import_playbook)

    label_field = "//div[@name='labels']//span[contains(@class,'cyicon-chevron-down')]"

    def click_on_label_field(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.label_field)

    label_input_field = "//div[@name='labels']//input[@type='text']"

    def put_label_name(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.label_input_field, value)

    def visibility_of_label(self, label_name):
        path = "//div[@name='labels']//li[1]//div[contains(text(),'" + label_name + "')]"
        return Action.check_visibility_of_element(self, By.XPATH, path)

    top_first_searched_label = "//div[@name='labels']//li[1]/div[2]"

    def click_on_top_searched_label(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.top_first_searched_label)

    playbook_created_successful_txt = "//div[@class='el-notification__content']//span[contains(text(),'Playbook')]"

    def get_playbook_created_successful_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_created_successful_txt)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.normal_click(self, By.XPATH, Playbooks.tooltip_close)
