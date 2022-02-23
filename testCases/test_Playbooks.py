import time

import pytest
from selenium.common.exceptions import NoSuchElementException

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from pageObjects.Playbooks import Playbooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybook(Base):
    global parent
    parent = ''

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_Manage_Playbook_redirection(self):
        """
            Verify Manage Playbook redirection from Main Menu
            Validation- 1. On the basis of page heading
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        playbooks = Playbooks(self.driver)
        action = Action(self.driver)
        log.info("Click on Main Menu")
        action.click(nav.click_Main_Menu())
        log.info("Click on Manage Playbook from Main Menu")
        action.click(nav.Navigate_Manage_Playbook())
        read_page_heading = action.getText(playbooks.get_manage_playbook_heading())
        assert read_page_heading == 'Manage Playbooks'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_02_My_Playbooks_close_automatic_walkthrough(self):
        """
            close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        try:
            log.info("click on the next button")
            tooltip_count = action.get_walkthrough_slider_count(playbooks.get_tooltip_count())
            for i in range(0, tooltip_count):
                action.click(playbooks.click_on_next_btn())
        except NoSuchElementException:
            log.info("Automatic walkthrough was not initiated. Hence passing this testcase")
            pass

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Cyware_Playbooks_Switch_tab(self):
        """
            Verify user is able to switch from My Playbooks to Cyware Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on Cyware Playbooks for switch tab ")
        action.click(playbooks.cyware_playbook_tab())
        time.sleep(ReadConfig.Wait_3_Sec())
        assert action.getTitle() == 'Cyware Playbooks | Cyware Orchestrate'

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_04_Cyware_Playbooks_close_automatic_walkthrough(self):
        """
            close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        try:
            log.info("click on the next button")
            tooltip_count = action.get_walkthrough_slider_count(playbooks.get_tooltip_count())
            for i in range(0, tooltip_count):
                action.click(playbooks.click_on_next_btn())
        except NoSuchElementException:
            log.info("Automatic walkthrough was not initiated. Hence passing this testcase")
            pass

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_05_Verify_My_Playbooks_Switch_tab(self):
        """
            Verify user is able to switch from Cyware Playbooks to My Playbooks
            Validation - 1. On the basis of Windows title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on My Playbooks for switch tab")
        action.click(playbooks.my_playbook_tab())
        time.sleep(ReadConfig.Wait_3_Sec())
        assert action.getTitle() == 'My Playbooks | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_06_Verify_Click_Create_New_Playbook_btn(self):
        """
        Verify user is able to click on create new playbook button
        Validation : Based on the window title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on create new playbook cta")
        action.click(playbooks.click_on_create_playbook_btn())
        log.info("Read the page title")
        page_title = action.getTitle()
        assert page_title == 'Add Playbook | Cyware Orchestrate'
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_07_Edit_Mode_close_automatic_walkthrough(self):
        """
            close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        try:
            log.info("click on the next button")
            tooltip_count = action.get_walkthrough_slider_count(playbooks.get_tooltip_count())
            for i in range(0, tooltip_count):
                action.click(playbooks.click_on_next_btn())
        except NoSuchElementException:
            log.info("Automatic walkthrough was not initiated. Hence passing this testcase")
            pass

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_08_Verify_Click_Add_Node_btn(self):
        """
          Verify click on add node button
          Validation : Based on the add node slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Click on add node button")
        action.click(playbooks.click_add_node_btn())
        log.info("Read the add node slider title")
        slider_text = action.getText(playbooks.get_add_node_slider_text())
        assert slider_text == 'ADD NODES'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_09_Verify_All_Nodes_Visibility(self):
        """
           Verify user is able to see all the nodes
           Validation: Based on the nodes category title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Read all the action nodes")
        all_elements = playbooks.get_all_elements()
        nodes_list = ['Action Nodes', 'Condition Nodes', 'Input Node', 'Memory Node']
        log.info("Validate all the node title")
        for i in range(0, len(all_elements)):
            node_title = action.getText(all_elements[i])
            assert node_title == nodes_list[i]
        log.info("Closing the node slider")
        action.click(playbooks.click_on_node_close_btn())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_10_Check_Video_walkthrough(self):
        """
            Verify user is able to see the video walkthough
            Validation: Based on the video walkthrough popup title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on Walkthrough button")
        action.click(playbooks.click_walkthrough_bulb_btn())
        log.info("Click on video walkthrough button")
        time.sleep(ReadConfig.Wait_3_Sec())
        action.javascript_click_element(playbooks.click_on_video_walthrough_btn())
        log.info("Read the video walkthrough popup title")
        popup_title = action.getText(playbooks.get_video_walkthrough_popup_txt())
        log.info("Click on finish button to close the popup")
        action.click(playbooks.click_on_finish_button())
        assert popup_title == 'Creating a New Playbook?'
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_11_Check_Tooltip_walkthrough(self):
        """
            Verify user is able to see the tooltip walkthough
            Validation: Based on the tooltip walkthrough title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on Walkthrough button")
        action.click(playbooks.click_walkthrough_bulb_btn())
        log.info("Click on the tooltip walkthrough button")
        action.javascript_click_element(playbooks.click_on_tooltip_walkthrough_btn())
        log.info("Reading the no of tooltips available")
        tooltip_count = action.get_walkthrough_slider_count(playbooks.get_tooltip_count())
        log.info("Reading the walkthrough tooltip title")
        tooltip_titles = ['Playbook Overview', 'Add Node', 'Connect Nodes', 'Zoom and Auto-arrange Nodes',
                          'Save and Run']
        for i in range(0, tooltip_count):
            time.sleep(ReadConfig.Wait_3_Sec())
            tooltip_text = action.getText(playbooks.get_tooltip_title())
            assert tooltip_text == tooltip_titles[i]
            action.click(playbooks.click_on_next_btn())
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_12_Check_Save_Options(self):
        """
            Verify user is able to see the save options
            Validation: Based on the save options visibility
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Mouse hover on the save button")
        action.mouse_hover_on_element(playbooks.mouse_hover_on_save_btn())
        text_save_and_run = action.getText(playbooks.get_save_and_run_txt())
        text_save_and_exit = action.getText(playbooks.get_save_and_exit_txt())
        assert text_save_and_exit == 'Save & Exit' and text_save_and_run == 'Save & Run'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_13_Check_Playbook_Overview_Slider(self):
        """
            Verify user is able to see the playbook overview slider
            Validation: Based on the slider title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the over view button")
        action.click(playbooks.click_on_playbook_overview_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the playbook overview slider title")
        slider_title = action.getText(playbooks.get_playbook_overview_slider_title())
        assert slider_title == 'Overview'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_14_Switch_Output_Parameters_Section(self):
        """
            Verify whether user is able to click on output parameter
            Validation: Based on the section title and add parameter button visibility
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the playbook data slider")
        action.click(playbooks.click_on_playbook_data())
        log.info("Click on the output parameters section")
        action.click(playbooks.click_on_output_parameters())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the section title")
        section_title = action.getText(playbooks.click_on_output_parameters())
        log.info("Check for visibility of output parameters button")
        bool = action.check_visibility_of_element(playbooks.click_on_add_parameter_btn())
        assert section_title == 'Output Parameters (0)' and bool is True

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_15_Add_Output_Parameter(self):
        """
            Verify user is able to add the output parameters
            Validation: Based on the params visibility
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on add parameter button")
        action.javascript_click_element(playbooks.click_on_add_parameter_btn())
        log.info("Check visibility of key field")
        bool1 = action.check_visibility_of_element(playbooks.check_visibility_of_key_field())
        log.info("Check visibility of value field")
        bool2 = action.check_visibility_of_element(playbooks.check_visibility_of_value_field())
        log.info("Deleting the created parameters")
        action.click(playbooks.click_on_parameter_delete_btn())
        assert bool1 is True and bool2 is True

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_16_Verify_Switch_to_Associated_Playbooks(self):
        """
            Verify user is able to switch to associated playbooks section
            Validation: Based on the section title and no state text
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the output parameters section")
        action.click(playbooks.click_on_output_parameters())
        log.info("Click on associated playbooks section")
        action.click(playbooks.click_on_associated_playbook())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the section title")
        section_title = action.getText(playbooks.click_on_associated_playbook())
        log.info("Read the no state text")
        text = action.getText(playbooks.get_no_state_validation_text())
        assert section_title == 'Associated Playbook (0)' and text == 'No Master Playbooks Available'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_17_Verify_Switch_to_Sub_Playbooks_tab(self):
        """
            Verify whether user is able to switch to sub-playbooks section
            Validation: Based on the subplaybooks tab color
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Switch to sub-playbooks tab")
        action.click(playbooks.switch_to_sub_playbooks_tab())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read no state text")
        text = action.getText(playbooks.get_no_state_validation_text())
        assert text == 'No Sub Playbooks Available'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_18_Verify_Switch_App_and_Actions(self):
        """
            Verify whether user is able to switch apps and actions section
            Validation based on section title and no state text
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Close the associated playbooks section")
        action.click(playbooks.click_on_associated_playbook())
        log.info("Click on apps and action section")
        action.click(playbooks.click_apps_and_actions())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the section title")
        section_title = action.getText(playbooks.click_apps_and_actions())
        log.info("Read the no state text")
        text = action.getText(playbooks.get_no_state_validation_text())
        log.info("click on the back button")
        action.click(playbooks.click_on_back_button())
        log.info("Click exit without save button")
        action.click(playbooks.click_exit_without_save())
        assert section_title == 'Apps (0) / Actions (0)' and text == 'No App/Actions Available'
        time.sleep(ReadConfig.Wait_10_Sec())

    @pytest.mark.smoke
    def test_19_Click_Customize_Table_btn(self):
        """
            Verify whether user is able to click on customize table
            Validation: Based on the slider title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the customize table button")
        action.click(playbooks.click_on_customize_table_btn())
        log.info("Read the slider title")
        time.sleep(ReadConfig.Wait_3_Sec())
        slider_txt = action.getText(playbooks.get_customize_table_txt())
        log.info("close the slider")
        action.click(playbooks.click_close_customize_table_btn())
        assert slider_txt == 'Customize Display Fields'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_20_Click_Filter_btn(self):
        """
            Verify whether user is able to click on filter button
            Validation: Based on the slider title
        """
        action = Action(self.driver)
        log = self.getlogger()
        playbooks = Playbooks(self.driver)
        log.info("Click on the filter button")
        action.click(playbooks.click_filter_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the filter slider title")
        slider_txt = action.getText(playbooks.get_filter_title())
        assert slider_txt == 'FILTERS'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_21_View_Playbook(self):
        """
            Verify opening playbook in view mode from cyware playbook
            Validation : Based on the window's title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        log.info("Switching to cyware playbook tab")
        action.click(playbooks.cyware_playbook_tab())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Click on the first playbook")
        action.click(playbooks.click_first_playbook())
        time.sleep(ReadConfig.Wait_10_Sec())
        log.info("Switch to new tab")
        global parent_window
        parent_window = action.switch_new_window(1)
        log.info("Read the window title")
        page_title = action.getTitle()
        assert page_title == 'View Playbook | Cyware Orchestrate'

    @pytest.mark.readOnly
    @pytest.mark.smoke
    def test_22_View_Mode_Close_automatic_walkthrough(self):
        """
            Close all automatically initiated walkthroughs for new poc
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbooks = Playbooks(self.driver)
        try:
            log.info("click on the next button")
            tooltip_count = action.get_walkthrough_slider_count(playbooks.get_tooltip_count())
            for i in range(0, tooltip_count):
                action.click(playbooks.click_on_next_btn())
        except NoSuchElementException:
            log.info("Automatic walkthrough was not initiated. Hence passing this testcase")
            pass

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_23_Check_Export_Options_visibility(self):
        """
            Verify whether user is able to seen the export options
            Validation: Based on the export options visibility
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbook = Playbooks(self.driver)
        log.info("Click on the more options")
        action.mouse_hover_on_element(playbook.click_playbook_more_options())
        log.info("Click on the export button")
        action.click(playbook.mouse_hover_export_btn())
        log.info("Check visibility of export options ")
        export_png = action.check_visibility_of_element(playbook.check_visibility_export_as_png())
        export_json = action.check_visibility_of_element(playbook.check_visibility_export_as_json())
        assert export_json is True and export_png is True
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_24_Check_Clone_btn_Visibility(self):
        """
        Verify whether user is able to see the clone button
        Validation: Based on the clone button visibility
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbook = Playbooks(self.driver)
        log.info("Click on the more options")
        action.mouse_hover_on_element(playbook.click_playbook_more_options())
        log.info("Check for clone button visibility")
        assert action.check_visibility_of_element(playbook.check_visibility_of_clone_btn()) is True
        time.sleep(ReadConfig.Wait_3_Sec())

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_25_Click_on_Test_Instances(self):
        """
        Verify whether user is able to click on the test connectivity
        Validation:- Based on the slider title
        """
        log = self.getlogger()
        action = Action(self.driver)
        playbook = Playbooks(self.driver)
        log.info("Click on the more options")
        action.mouse_hover_on_element(playbook.click_playbook_more_options())
        log.info("Click on the test instances button")
        action.click(playbook.click_on_test_instances_btn())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Read the slider title")
        slider_title = action.getText(playbook.get_test_instance_slider_text())
        log.info("Close the test instances slider")
        action.click(playbook.click_test_instance_slider_close_btn())
        log.info("Switch back to parent window and close child window")
        action.switch_back_parent_window(parent_window)
        assert slider_title == 'Test Instances'
