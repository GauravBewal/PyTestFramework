from selenium.webdriver.common.by import By
from utilities.Actions import Action


class Playbooks(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    nodes_list = ['Action Nodes', 'Condition Nodes', 'Input Node', 'Memory Node']
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
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_test_instances)

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
        return Action.wait_and_click(self, By.XPATH, Playbooks.test_instance_slider_close_btn)

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

    btn_first_playbook = "//div[3]//tr[1]/td[2]//a"

    def click_first_playbook(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.btn_first_playbook)

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, Playbooks.close_walkthrough_tooltip)

    playbook_page_heading = "//header//h1"

    def get_manage_playbook_heading(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_page_heading)

    playbook_customize_table_btn = "//i[@class='cyicon-settings']/parent::div"

    def click_on_customize_table_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_customize_table_btn)

    customize_table_slider_title = "//span[@data-testaction='slider-close']/parent::div/preceding-sibling::div"

    def get_customize_table_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.customize_table_slider_title)

    close_customize_table = "//span[@data-testaction='slider-close']/parent::div"

    def click_close_customize_table_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.close_customize_table)

    playbook_filter_btn = "//i[@class='icon icon-filter']/parent::button"

    def click_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_filter_btn)

    filter_close_btn = "//i[contains(@class,'cyicon-cross')]/parent::span"

    def close_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.filter_close_btn)

    playbook_filter_title = "//span[@class='filters__header__label']"

    def get_filter_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_filter_title)

    playbook_create_btn = "//button[contains(@class,'create-playbook')]"

    def click_on_create_playbook_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_create_btn)

    playbook_back_btn = "//div[@class='playbook_header__view']//i"

    def click_on_back_button(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_back_btn)

    playbook_exit_without_save_btn = "//button[contains(text(),'Exit without Save')]"

    def click_exit_without_save(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_exit_without_save_btn)

    playbook_add_node_btn = "//div[@class='stencil-container walkthrough-stencil']"

    def click_add_node_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_add_node_btn)

    playbook_node_slider_text = "//div[@class='stencil-header']"

    def get_add_node_slider_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_node_slider_text)

    all_Action_nodes_text = "//div[@class='content']//h3"

    def get_all_viewall_elements(self):
        return Action.get_no_of_elements_present(self, By.XPATH, Playbooks.all_Action_nodes_text)

    def get_list_of_elements(self, elements_count, elements):
        elements_list = []
        # indexing xpath and storing it in list
        for value in range(1, elements_count + 1):
            path = "(" + elements + ")[" + str(value) + "]"
            elements_list.append(path)
        return elements_list

    def get_node_title(self, path):
        return Action.get_text(self, By.XPATH, path)

    node_slider_close_btn = "//div[@class='stencil-close']"

    def click_on_node_close_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.node_slider_close_btn)

    playbook_name_field = "//input[@placeholder='Enter Name']"

    def enter_playbook_name(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.playbook_name_field, value)

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

    playbook_walkthrough_bulb_btn = "//div[@class=' el-dropdown-selfdefine']/button"

    def click_walkthrough_bulb_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_walkthrough_bulb_btn)

    playbook_tooltip_walkthrough = "//i[contains(@class,'icon-refresh')]/ancestor::li"

    def click_on_tooltip_walkthrough_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_tooltip_walkthrough)

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
        return Action.wait_and_click(self, By.XPATH, Playbooks.grid_view_btn)

    def get_grid_icon_color(self):
        return Action.get_css_property_value(self, By.XPATH, Playbooks.grid_view_btn, 'color')

    increment_pagination_btn = "//div[contains(@class,'footer-box')]//button[@class='btn-next']"

    def click_on_increment_pagination_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.increment_pagination_btn)

    decrement_pagination_btn = "//div[contains(@class,'footer-box')]//button[@class='btn-prev']"

    def click_on_decrement_pagination_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.decrement_pagination_btn)

    walkthrough_tooltip_title = "//h1[@class='introjs-tooltip-title']"

    def get_tooltip_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.walkthrough_tooltip_title)

    walkthrough_tooltip_next_btn = "//a[contains(@class,'introjs-nextbutton')]"

    def click_on_next_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.walkthrough_tooltip_next_btn)

    playbook_video_walkthrough_btn = "//i[contains(@class,'icon-video')]/ancestor::li"

    def click_on_video_walthrough_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_video_walkthrough_btn)

    video_walkthrough_popup_title = "//h1[@class='introjs-tooltip-title']"

    def get_video_walkthrough_popup_txt(self):
        return Action.get_text(self, By.XPATH, Playbooks.video_walkthrough_popup_title)

    video_walkthrough_finish_btn = "//div[@class='introjs-tooltipbuttons']/a"

    def click_on_finish_button(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.video_walkthrough_finish_btn)

    textbox_search_playbook = "//header//div[contains(@class,'search-input')]/input"

    def search_playbooks(self, value):
        return Action.send_keys(self, By.XPATH, Playbooks.textbox_search_playbook, value)

    playbook_overview_btn = "//button[contains(@class,'playbook-overview-btn')]"

    def click_on_playbook_overview_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_overview_btn)

    playbook_overview_slider_title = "//div[text()='Overview']"

    def get_playbook_overview_slider_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_overview_slider_title)

    overview_output_parameters = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[1]"

    def click_on_output_parameters(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.overview_output_parameters)

    def get_output_parameter_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.overview_output_parameters)

    add_parameters_btn = "//div[@class='el-collapse-item is-active']//button"

    def click_on_add_parameter_btn(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.add_parameters_btn)

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
        return Action.wait_and_click(self, By.XPATH, Playbooks.parameter_delete_btn)

    overview_playbook_data = "//div[contains(@class,'playbook-data')]/div[1]/div"

    def click_on_playbook_data(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.overview_playbook_data)

    associated_playbooks = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[2]"

    def click_on_associated_playbook(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.associated_playbooks)

    def get_associated_playbooks_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.associated_playbooks)

    no_state_validation_txt = "//div[@class='el-collapse-item is-active']//h1"

    def get_no_state_validation_text(self):
        return Action.get_text(self, By.XPATH, Playbooks.no_state_validation_txt)

    associated_sub_playbooks = "//div[@class='el-collapse-item is-active']//label[2]"

    def switch_to_sub_playbooks_tab(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.associated_sub_playbooks)

    playbook_app_and_actions = "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[3]"

    def click_apps_and_actions(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.playbook_app_and_actions)

    def get_apps_and_actions_section_title(self):
        return Action.get_text(self, By.XPATH, Playbooks.playbook_app_and_actions)

    button_import_playbook = "//button[contains(@class,'import-playbook')]"

    def click_import_playbook(self):
        return Action.wait_and_click(self, By.XPATH, Playbooks.button_import_playbook)
