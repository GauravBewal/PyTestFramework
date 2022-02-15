from selenium.webdriver.common.by import By


class Playbooks:

    def __init__(self, driver):
        self.driver = driver

    tab_cyware_playbooks = (By.XPATH, "//li[contains(@class,'cyware-playbook')]")

    def cyware_playbook_tab(self):
        return self.driver.find_element(*Playbooks.tab_cyware_playbooks)

    tab_my_playbooks = (By.XPATH, "//li[contains(@class,'my-playbook')]/a")

    def my_playbook_tab(self):
        return self.driver.find_element(*Playbooks.tab_my_playbooks)

    more_options_btn = (By.XPATH, "//div[@class='el-dropdown']/span")

    def click_playbook_more_options(self):
        return self.driver.find_element(*Playbooks.more_options_btn)

    playbook_clone_btn = (By.XPATH, "//i[@class='cyicon-copy']/parent::li")

    def check_visibility_of_clone_btn(self):
        return self.driver.find_element(*Playbooks.playbook_clone_btn)

    playbook_test_instances = (By.XPATH, "//i[@class='icon-connect']/parent::li")

    def click_on_test_instances_btn(self):
        return self.driver.find_element(*Playbooks.playbook_test_instances)

    playbook_test_instance_slider_text = (By.XPATH, "//span[@data-testaction='slider-close']/parent::div/preceding-sibling::div/div")

    def get_test_instance_slider_text(self):
        return self.driver.find_element(*Playbooks.playbook_test_instance_slider_text)

    instance_connection_result_tabs = (By.XPATH, "//div[@class='px-2 tabs--list']//li")

    def get_all_connection_result_tabs(self):
        return self.driver.find_elements(*Playbooks.instance_connection_result_tabs)

    test_instance_no_state_text = (By.XPATH, "//div[@class='h-100']//p")

    def get_test_intance_no_state_text(self):
        return self.driver.find_element(*Playbooks.test_instance_no_state_text)

    test_instance_slider_close_btn = (By.XPATH, "//span[@data-testaction='slider-close']/parent::div")

    def click_test_instance_slider_close_btn(self):
        return self.driver.find_element(*Playbooks.test_instance_slider_close_btn)

    playbook_export_btn = (By.XPATH, "//i[@class='icon-export-boxed']/parent::li")

    def mouse_hover_export_btn(self):
        return self.driver.find_element(*Playbooks.playbook_export_btn)

    playbook_export_as_png = (By.XPATH, "//li[contains(text(),'PNG')]")

    def check_visibility_export_as_png(self):
        return self.driver.find_element(*Playbooks.playbook_export_as_png)

    playbook_export_as_json = (By.XPATH, "//li[contains(text(),'JSON')]")

    def check_visibility_export_as_json(self):
        return self.driver.find_element(*Playbooks.playbook_export_as_json)



    btn_first_playbook = (By.XPATH, "//div[3]//tr[1]/td[2]//a")

    def click_first_playbook(self):
        return self.driver.find_element(*Playbooks.btn_first_playbook)

    close_walkthrough_tooltip = (By.XPATH, "//a[@class='introjs-skipbutton']")

    def click_on_close_walkthrough(self):
        return self.driver.find_element(*Playbooks.close_walkthrough_tooltip)

    playbook_page_heading = (By.XPATH, "//header//h1")

    def get_manage_playbook_heading(self):
        return self.driver.find_element(*Playbooks.playbook_page_heading)

    playbook_customize_table_btn = (By.XPATH, "//i[@class='cyicon-settings']/parent::div")

    def click_on_customize_table_btn(self):
        return self.driver.find_element(*Playbooks.playbook_customize_table_btn)

    customize_table_slider_title = (By.XPATH, "//span[@data-testaction='slider-close']/parent::div/preceding-sibling::div")

    def get_customize_table_txt(self):
        return self.driver.find_element(*Playbooks.customize_table_slider_title)

    close_customize_table = (By.XPATH, "//span[@data-testaction='slider-close']/parent::div")

    def click_close_customize_table_btn(self):
        return self.driver.find_element(*Playbooks.close_customize_table)

    playbook_filter_btn = (By.XPATH, "//i[@class='icon icon-filter']/parent::button")

    def click_filter_btn(self):
        return self.driver.find_element(*Playbooks.playbook_filter_btn)

    playbook_filter_title = (By.XPATH, "//span[@class='filters__header__label']")

    def get_filter_title(self):
        return self.driver.find_element(*Playbooks.playbook_filter_title)


    playbook_create_btn = (By.XPATH, "//button[contains(@class,'create-playbook')]")

    def click_on_create_playbook_btn(self):
        return self.driver.find_element(*Playbooks.playbook_create_btn)

    playbook_back_btn = (By.XPATH, "//div[@class='playbook_header__view']//i")

    def click_on_back_button(self):
        return self.driver.find_element(*Playbooks.playbook_back_btn)

    playbook_exit_without_save_btn = (By.XPATH, "//button[contains(text(),'Exit without Save')]")

    def click_exit_without_save(self):
        return self.driver.find_element(*Playbooks.playbook_exit_without_save_btn)

    playbook_add_node_btn = (By.XPATH, "//div[@class='stencil-container walkthrough-stencil']")

    def click_add_node_btn(self):
        return self.driver.find_element(*Playbooks.playbook_add_node_btn)

    playbook_node_slider_text = (By.XPATH, "//div[@class='stencil-header']")

    def get_add_node_slider_text(self):
        return self.driver.find_element(*Playbooks.playbook_node_slider_text)

    all_Action_nodes_text = (By.XPATH, "//div[@class='content']//h3")

    def get_all_elements(self):
        return self.driver.find_elements(*Playbooks.all_Action_nodes_text)

    node_slider_close_btn = (By.XPATH, "//div[@class='stencil-close']")

    def click_on_node_close_btn(self):
        return self.driver.find_element(*Playbooks.node_slider_close_btn)

    playbook_name_field = (By.XPATH, "//input[@placeholder='Enter Name']")

    def enter_playbook_name(self):
        return self.driver.find_element(*Playbooks.playbook_name_field)

    playbook_description_field = (By.XPATH, "//input[@placeholder='Enter Description']")

    def enter_playbook_description(self):
        return self.driver.find_element(*Playbooks.playbook_description_field)

    save_more_options = (By.XPATH, "(//div[@class='el-button-group']/button)[2]")

    def mouse_hover_on_save_btn(self):
        return self.driver.find_element(*Playbooks.save_more_options)

    save_and_run_btn = (By.XPATH, "//i[@class='icon-save-and-run']/parent::li")

    def get_save_and_run_txt(self):
        return self.driver.find_element(*Playbooks.save_and_run_btn)

    save_and_exit_btn = (By.XPATH, "//i[@class='icon-save-and-exit']/parent::li")

    def get_save_and_exit_txt(self):
        return self.driver.find_element(*Playbooks.save_and_exit_btn)


    playbook_walkthrough_bulb_btn = (By.XPATH, "//div[@class=' el-dropdown-selfdefine']/button")

    def click_walkthrough_bulb_btn(self):
        return self.driver.find_element(*Playbooks.playbook_walkthrough_bulb_btn)

    playbook_tooltip_walkthrough = (By.XPATH, "//i[contains(@class,'icon-refresh')]/ancestor::li")

    def click_on_tooltip_walkthrough_btn(self):
        return self.driver.find_element(*Playbooks.playbook_tooltip_walkthrough)

    walkthrough_tooltip_count = (By.XPATH, "//div[@class='introjs-helperNumberLayer']")

    def get_tooltip_count(self):
        return self.driver.find_element(*Playbooks.walkthrough_tooltip_count)

    walkthrough_tooltip_title = (By.XPATH, "//h1[@class='introjs-tooltip-title']")

    def get_tooltip_title(self):
        return self.driver.find_element(*Playbooks.walkthrough_tooltip_title)



    walkthrough_tooltip_next_btn = (By.XPATH, "//a[contains(@class,'introjs-nextbutton')]")

    def click_on_next_btn(self):
        return self.driver.find_element(*Playbooks.walkthrough_tooltip_next_btn)


    walkthrough_finish_btn = (By.XPATH, "//a[contains(@class,'introjs-donebutton')]")

    def click_on_walkthrough_finish_btn(self):
        return self.driver.find_element(*Playbooks.walkthrough_finish_btn)

    playbook_video_walkthrough_btn = (By.XPATH, "//i[contains(@class,'icon-video')]/ancestor::li")

    def click_on_video_walthrough_btn(self):
        return self.driver.find_element(*Playbooks.playbook_video_walkthrough_btn)

    video_walkthrough_popup_title = (By.XPATH, "//h1[@class='introjs-tooltip-title']")

    def get_video_walkthrough_popup_txt(self):
        return self.driver.find_element(*Playbooks.video_walkthrough_popup_title)

    video_walkthrough_finish_btn = (By.XPATH, "//div[@class='introjs-tooltipbuttons']/a")

    def click_on_finish_button(self):
        return self.driver.find_element(*Playbooks.video_walkthrough_finish_btn)

    table_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip list-button')]")

    def get_table_view_playbook(self):
        return self.driver.find_element(*Playbooks.table_view_playbook)

    grid_view_playbook = (By.XPATH, "//*[contains(@class,'el-tooltip grid-button')]")

    def get_grid_view_playbook(self):
        return self.driver.find_element(*Playbooks.grid_view_playbook)

    textbox_search_playbook = (By.CSS_SELECTOR, "input[placeholder='Search Playbook(s)']")

    def search_playbooks(self):
        return self.driver.find_element(*Playbooks.textbox_search_playbook)

    playbook_overview_btn = (By.XPATH, "//button[contains(@class,'playbook-overview-btn')]")

    def click_on_playbook_overview_btn(self):
        return self.driver.find_element(*Playbooks.playbook_overview_btn)

    playbook_overview_slider_title = (By.XPATH, "//div[text()='Overview']")

    def get_playbook_overview_slider_title(self):
        return self.driver.find_element(*Playbooks.playbook_overview_slider_title)

    overview_output_parameters = (By.XPATH,"(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[1]")

    def click_on_output_parameters(self):
        return self.driver.find_element(*Playbooks.overview_output_parameters)

    add_parameters_btn = (By.XPATH, "//div[@class='el-collapse-item is-active']//button")

    def click_on_add_parameter_btn(self):
        return self.driver.find_element(*Playbooks.add_parameters_btn)

    parameter_key_field = (By.XPATH,"//textarea[@placeholder='Key']")

    def check_visibility_of_key_field(self):
        return self.driver.find_element(*Playbooks.parameter_key_field)

    parameter_value_field = (By.XPATH, "//textarea[@placeholder='Value']")

    def check_visibility_of_value_field(self):
        return self.driver.find_element(*Playbooks.parameter_value_field)

    parameter_delete_btn = (By.XPATH, "//i[@class='cyicon-trash']/parent::button")

    def click_on_parameter_delete_btn(self):
        return self.driver.find_element(*Playbooks.parameter_delete_btn)

    overview_playbook_data = (By.XPATH, "//div[contains(@class,'playbook-data')]/div[1]/div")

    def click_on_playbook_data(self):
        return self.driver.find_element(*Playbooks.overview_playbook_data)

    associated_playbooks = (By.XPATH, "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[2]")

    def click_on_associated_playbook(self):
        return self.driver.find_element(*Playbooks.associated_playbooks)

    no_state_validation_txt = (By.XPATH, "//div[@class='el-collapse-item is-active']//h1")

    def get_no_state_validation_text(self):
        return self.driver.find_element(*Playbooks.no_state_validation_txt)

    associated_sub_playbooks = (By.XPATH, "//div[@class='el-collapse-item is-active']//label[2]")

    def switch_to_sub_playbooks_tab(self):
        return self.driver.find_element(*Playbooks.associated_sub_playbooks)

    playbook_app_and_actions = (By.XPATH, "(//div[contains(@class,'playbook-data')]/following-sibling::div/div[1]/div)[3]")

    def click_apps_and_actions(self):
        return self.driver.find_element(*Playbooks.playbook_app_and_actions)


    button_import_playbook = (By.XPATH, "//button[contains(@class,'import-playbook')]")

    def click_import_playbook(self):
        return self.driver.find_element(*Playbooks.button_import_playbook)
