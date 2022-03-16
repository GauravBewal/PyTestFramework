import pytest

from pageObjects.FilterandSort import FilterAndSort
from pageObjects.Navigation import Navigation
from pageObjects.Pagination import Pagination
from pageObjects.Playbooks import Playbooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybook(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Manage_Playbook_redirection(self):
        """
            Verify Manage Playbook redirection from Main Menu
            Validation- 1. On the basis of page heading
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on Main Menu")
        nav.click_main_menu()
        log.info("Click on Manage Playbook from Main Menu")
        nav.navigate_manage_playbook()
        log.info("Check if walk through is initiated")
        playbooks.click_on_close_walkthrough()
        read_page_heading = playbooks.get_manage_playbook_heading()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert read_page_heading == 'Manage Playbooks' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Verify_Cyware_Playbooks_Switch_tab(self):
        """
            Verify user is able to switch from My Playbooks to Cyware Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on Cyware Playbooks for switch tab ")
        playbooks.cyware_playbook_tab()
        log.info("Check if walk through is initiated")
        playbooks.click_on_close_walkthrough()
        assert action.get_title() == 'Cyware Playbooks | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_My_Playbooks_Switch_tab(self):
        """
            Verify user is able to switch from Cyware Playbooks to My Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on My Playbooks for switch tab")
        playbooks.my_playbook_tab()
        assert action.get_title() == 'My Playbooks | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Click_Create_New_Playbook_btn(self):
        """
        Verify user is able to click on create new playbook button
        Validation : Based on the window title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on create new playbook cta")
        playbooks.click_on_create_playbook_btn()
        log.info("Read the page title")
        log.info("Check if walk through is initiated")
        playbooks.click_on_close_walkthrough()
        assert action.get_title() == 'Add Playbook | Cyware Orchestrate'

    @pytest.mark.readOnly
    @pytest.mark.regression
    def test_05_Verify_Click_Add_Node_btn(self):
        """
          Verify click on add node button
          Validation : Based on the add node slider title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on add node button")
        playbooks.click_add_node_btn()
        log.info("Read the add node slider title")
        slider_text = playbooks.get_add_node_slider_text()
        assert slider_text == 'ADD NODES'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_06_Verify_All_Node_Type_Titles_Visibility(self):
        """
           Verify user is able to see all the node types
           Validation: Based on the nodes category title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Read all the action nodes")
        elements_list = playbooks.get_list_of_elements(playbooks.get_all_node_type_elements(),
                                                       playbooks.all_node_type_title)
        log.info("Validate all the node type title")
        for element in range(0, len(elements_list)):
            node_type_title = playbooks.get_node_type_title(elements_list[element])
            assert node_type_title == playbooks.node_type_list[element]

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_07_Verify_All_Nodes_Visibility(self):
        """
        Verify user is able to see all the nodes
        Validation 1: Based on the nodes visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Reade the node title")
        elements_list = playbooks.get_list_of_elements(playbooks.get_all_node_elements(), playbooks.all_nodes_names)
        log.info("Validate all the node title")
        for element in range(0, len(elements_list)):
            node_title = playbooks.get_node_type_title(elements_list[element])
            assert node_title == playbooks.node_titles_list[element]
        log.info("Closing the node slider")
        playbooks.click_on_node_close_btn()

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_08_Check_Video_walkthrough(self):
        """
            Verify user is able to see the video walkthough
            Validation: Based on the video walkthrough popup title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on Walkthrough button")
        playbooks.click_walkthrough_bulb_btn()
        log.info("Click on video walkthrough button")
        playbooks.click_on_video_walthrough_btn()
        log.info("Read the video walkthrough popup title")
        popup_title = playbooks.get_video_walkthrough_popup_txt()
        log.info("Click on finish button to close the popup")
        playbooks.click_on_finish_button()
        assert popup_title == 'Creating a New Playbook?'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_09_Check_Tooltip_walkthrough(self):
        """
            Verify user is able to see the tooltip walkthough
            Validation: Based on the tooltip walkthrough title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on Walkthrough button")
        playbooks.click_walkthrough_bulb_btn()
        log.info("Mouse hover on the tooltip walkthrough button")
        playbooks.mouse_hover_on_tooltip_walkthrough_btn()
        log.info("Click on the tooltip walkthrough button")
        playbooks.click_on_tooltip_walkthrough_btn()
        log.info("Reading the no of tooltips available")
        tooltip_count = playbooks.get_tooltip_count()
        log.info("Reading the walkthrough tooltip title")
        for i in range(0, tooltip_count):
            tooltip_text = playbooks.get_tooltip_title()
            assert tooltip_text == playbooks.tooltip_titles[i]
            playbooks.click_on_next_btn()

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_10_Check_Save_Options(self):
        """
            Verify user is able to see the save options
            Validation: Based on the save options visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Mouse hover on the save button")
        playbooks.mouse_hover_on_save_btn()
        text_save_and_run = playbooks.get_save_and_run_txt()
        text_save_and_exit = playbooks.get_save_and_exit_txt()
        assert text_save_and_exit == 'Save & Exit' and text_save_and_run == 'Save & Run'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_11_Check_Playbook_Overview_Slider(self):
        """
            Verify user is able to see the playbook overview slider
            Validation: Based on the slider title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the over view button")
        playbooks.click_on_playbook_overview_btn()
        log.info("Read the playbook overview slider title")
        slider_title = playbooks.get_playbook_overview_slider_title()
        assert slider_title == 'Overview'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_12_Switch_Output_Parameters_Section(self):
        """
            Verify whether user is able to click on output parameter
            Validation: Based on the section title and add parameter button visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the playbook data slider")
        playbooks.click_on_playbook_data()
        log.info("Click on the output parameters section")
        playbooks.click_on_output_parameters()
        log.info("Read the section title")
        section_title = playbooks.get_output_parameter_section_title()
        log.info("Check for visibility of add parameters button")
        visibility = playbooks.visibility_of_add_parameter_btn()
        assert section_title == 'Output Parameters (0)' and visibility is True

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_13_Add_Output_Parameter(self):
        """
            Verify user is able to add the output parameters
            Validation: Based on the params visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on add parameter button")
        playbooks.click_on_add_parameter_btn()
        log.info("Check visibility of key field")
        visibility1 = playbooks.check_visibility_of_key_field()
        log.info("Check visibility of value field")
        visibility2 = playbooks.check_visibility_of_value_field()
        log.info("Deleting the created parameters")
        playbooks.click_on_parameter_delete_btn()
        assert visibility1 and visibility2 is True

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_14_Verify_Switch_to_Associated_Playbooks(self):
        """
            Verify user is able to switch to associated playbooks section
            Validation: Based on the section title and no state text
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the output parameters section")
        playbooks.click_on_output_parameters()
        log.info("Click on associated playbooks section")
        playbooks.click_on_associated_playbook()
        log.info("Read the section title")
        section_title = playbooks.get_associated_playbooks_section_title()
        log.info("Read the no state text")
        text = playbooks.get_no_state_validation_text()
        assert section_title == 'Associated Playbook (0)' and text == 'No Master Playbooks Available'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_15_Verify_Switch_to_Sub_Playbooks_tab(self):
        """
            Verify whether user is able to switch to sub-playbooks section
            Validation: Based on the subplaybooks tab color
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Switch to sub-playbooks tab")
        playbooks.switch_to_sub_playbooks_tab()
        log.info("Read no state text")
        text = playbooks.get_no_state_validation_text()
        assert text == 'No Sub Playbooks Available'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_16_Verify_Switch_App_and_Actions(self):
        """
            Verify whether user is able to switch apps and actions section
            Validation based on section title and no state text
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the associated playbooks section")
        playbooks.click_on_associated_playbook()
        log.info("Click on apps and action section")
        playbooks.click_apps_and_actions()
        log.info("Read the section title")
        section_title = playbooks.get_apps_and_actions_section_title()
        log.info("Read the no state text")
        text = playbooks.get_no_state_validation_text()
        log.info("click on the back button")
        playbooks.click_on_back_button()
        log.info("Click exit without save button")
        playbooks.click_exit_without_save()
        assert section_title == 'Apps (0) / Actions (0)' and text == 'No App/Actions Available'

    @pytest.mark.regression
    def test_17_Click_Customize_Table_btn(self):
        """
            Verify whether user is able to click on customize table
            Validation: Based on the slider title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the customize table button")
        playbooks.click_on_customize_table_btn()
        log.info("Read the slider title")
        slider_txt = playbooks.get_customize_table_txt()
        log.info("close the slider")
        playbooks.click_close_customize_table_btn()
        assert slider_txt == 'Customize Display Fields'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_18_Click_Filter_btn(self):
        """
            Verify whether user is able to click on filter button
            Validation: Based on the slider title
        """
        log = self.getlogger()
        filterandsort = FilterAndSort(self.driver)
        log.info("Click on the filter button")
        filterandsort.click_on_filters()
        log.info("Read the filter slider title")
        slider_txt = filterandsort.get_filters_slider_title()
        log.info("Close filter")
        filterandsort.close_filter_btn()
        assert slider_txt == 'FILTERS'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_19_View_Playbook(self):
        """
            Verify opening playbook in view mode from cyware playbook
            Validation : Based on the window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Switching to cyware playbook tab")
        playbooks.cyware_playbook_tab()
        log.info("Click on the first playbook")
        playbooks.click_first_playbook()
        log.info("Switch to newly opened playbook tab")
        global parent_window
        parent_window = playbooks.switch_new_window(1)
        log.info("Check if walk through is initiated")
        playbooks.click_on_close_walkthrough()
        log.info("Read the window title and validate it")
        assert action.get_title() == 'View Playbook | Cyware Orchestrate'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_20_Check_Export_Options_visibility(self):
        """
            Verify whether user is able to seen the export options
            Validation: Based on the export options visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("mouse hover on the more options")
        playbooks.mouse_hover_on_more_options()
        log.info("Click on the export button")
        playbooks.mouse_hover_export_btn()
        log.info("Check visibility of export options ")
        export_png = playbooks.check_visibility_export_as_png()
        export_json = playbooks.check_visibility_export_as_json()
        assert export_json and export_png is True

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_21_Check_Clone_btn_Visibility(self):
        """
        Verify whether user is able to see the clone button
        Validation: Based on the clone button visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("mouse hover on the more options")
        playbooks.mouse_hover_on_more_options()
        log.info("Check for clone button visibility")
        visibility = playbooks.check_visibility_of_clone_btn()

        assert visibility is True

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_22_Click_on_Test_Instances(self):
        """
        Verify whether user is able to click on the test connectivity
        Validation:- Based on the slider title
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the more options")
        playbooks.mouse_hover_on_more_options()
        log.info("Click on the test instances button")
        playbooks.click_on_test_instances_btn()
        log.info("Read the slider title")
        slider_title = playbooks.get_test_instance_slider_text()
        log.info("Close the test instances slider")
        playbooks.click_test_instance_slider_close_btn()
        log.info("switch back to parent window")
        playbooks.switch_back_parent_window(parent_window)
        assert slider_title == 'Test Instances'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_23_Verify_Grid_view_switching(self):
        """
        Verify whether user is able to switch to Grid view
        Validation 1:- Based on the button color visibility
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on Grid button")
        playbooks.click_on_grid_btn()
        log.info("Check whether grid view button is selected")
        grid_button_selected = playbooks.get_grid_icon_color()
        log.info("Check whether view has been changed to grid")
        assert grid_button_selected == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_24_Sort_options_visibility(self):
        """
        Verify whether user is able to see all the available sort options
        Validation 1: Based on the options visibility
        """
        log = self.getlogger()
        playbook = Playbooks(self.driver)
        log.info("Switching to my playbooks tab")
        playbook.my_playbook_tab()
        log.info("Mouse on the sort options")
        playbook.mouse_hover_sort_options()
        log.info("Reading all the visible sort options")
        elements_list = playbook.get_list_of_elements(playbook.read_available_sort_options(),
                                                      playbook.available_sort_options)
        for element in range(0, len(elements_list)):
            read_sort_option = playbook.get_sort_options_title(elements_list[element])
            assert read_sort_option == playbook.sort_options[element]

    @pytest.mark.regression
    def test_25_Verify_Pagination_increment(self):
        """
        Verify whether user is able to apply pagination
        Validation 1: Based on the page number
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        pagination = Pagination(self.driver)
        log.info("Reding the no of pages available")
        log.info("Change to 2nd page")
        pagination.click_on_increment_pagination_btn()
        page_count_after_change = playbooks.get_current_page_count()
        assert page_count_after_change == 2

    @pytest.mark.regression
    def test_26_Verify_Pagination_decrement(self):
        """
        Verify whether user is able to apply pagination
        Validation 1: Based on the page number
        """
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        pagination = Pagination(self.driver)
        log.info("Click on the previous page button")
        pagination.click_on_decrement_pagination_btn()
        log.info("Reding the current page number")
        current_page_number = playbooks.get_current_page_count()
        assert current_page_number == 1

    # @pytest.mark.regression
    # def test_27_Verify_playbook_execution_flow_with_ctix_action_node(self):
    #     """
    #     Install the ctix app to use it for playbook execution
    #     Validation 1: Based on the ctix app visibility
    #     """
    #     log = self.getlogger()
    #     action = Action(self.driver)
    #     nav = Navigation(self.driver)
    #     my_apps = MyApps(self.driver)
    #     playbooks = Playbooks(self.driver)
    #     log.info("Click on Main Menu")
    #     nav.click_main_menu()
    #     log.info("Click on Apps from Menu")
    #     nav.navigate_apps()
    #     log.info("Switch to my app tab")
    #     my_apps.app_store_tab()
    #     global app_name
    #     app_name = "CTIX"
    #     log.info("Search for ctix app")
    #     my_apps.search_for_app(app_name)
    #     search_result = my_apps.top_first_search(app_name)
    #     assert app_name in search_result
    #     log.info("Check whether app is installed or not")
    #     my_apps.Verify_app_installed_or_not()
    #     my_apps.click_first_search_result()
    #     log.info("Read the app version")
    #     app_version = my_apps.get_app_version()
    #     log.info("Navigate to instance tab")
    #     my_apps.click_app_instance_tab()
    #     log.info("create new instance")
    #     my_apps.click_on_new_instance_btn()
    #     log.info("Enter Instance name")
    #     global instance_name
    #     instance_name = "ui_automation" + action.get_current_time()
    #     my_apps.enter_instance_name(instance_name)
    #     log.info("Enter base url")
    #     my_apps.enter_base_url(ReadConfig.ctix_baseurl())
    #     log.info("Enter Access key")
    #     my_apps.enter_access_key(ReadConfig.ctix_access_key())
    #     log.info("Enter Secret key")
    #     my_apps.enter_secret_key(ReadConfig.ctix_secret_key())
    #     log.info("Click on create instance button")
    #     my_apps.click_slider_instance_create_btn()
    #     my_apps.close_tooltip()
    #     nav.click_main_menu()
    #     nav.navigate_manage_playbook()
    #     playbooks.my_playbook_tab()
    #     playbooks.click_on_create_playbook_btn()
    #     playbooks.click_add_node_btn()
    #     playbooks.drag_and_drop_action_app_node_by_position(500, 60)
    #     playbooks.put_app_name_to_search(app_name)
    #     playbooks.click_app_search_result()
    #     playbooks.select_action_version_based(app_version)
    #     selected_app_name = playbooks.get_selected_app_name("text")
    #     assert app_name in selected_app_name and playbooks.get_playbook_node_title() == '#1 - Action Node (App)'
    #     playbooks.mouse_hover_on_instance_tab()
    #     playbooks.click_on_clear_instance_btn()
    #     playbooks.click_on_instance_dropdown()
    #     playbooks.put_instance_name(instance_name)
    #     playbooks.click_on_searched_instance()
    #     log.info("Close the instance drop down")
    #     playbooks.click_on_instance_dropdown()
    #     playbooks.click_on_node_test_instance_btn()
    #     visibility = playbooks.visibility_of_test_again_btn()
    #     connectivity_result = playbooks.get_test_connectivity_result()
    #     assert connectivity_result == 'SUCCESS' and visibility is True
    #     playbooks.click_on_instance_connectivity_close_btn(instance_name)
    #     playbooks.click_on_input_data_tab()
    #     playbooks.put_input_data("cyware.com")
    #     playbooks.click_on_slider_close_btn()
    #     playbooks.mouse_hover_on_start_node()
    #     playbooks.connect_start_node_and_app_node()
    #     time.sleep(10)
