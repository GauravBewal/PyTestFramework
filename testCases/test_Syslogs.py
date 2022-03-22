import pytest

from pageObjects.ConfigureTrigger import ConfigureTrigger
from pageObjects.Labels import Labels
from pageObjects.Navigation import Navigation
from pageObjects.Syslogs import Syslogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestSyslogs(Base):

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Verify_Admin_SysLogs_redirection(self):
        """
            Verify redirection of SysLogs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Main menu")
        nav.click_admin_menu()
        log.info("Click on SysLogs tab from Admin Page")
        syslog.click_syslogs()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() in 'Syslogs | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Click_New_Syslogs_btn(self):
        """
            Verify create button functionality of new syslogs
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Click on add syslog button")
        syslog.click_new_syslog()
        log.info("Read the slider title")
        slider_title = syslog.get_slider_title()
        log.info("Click on close slider button")
        syslog.click_slider_close()
        assert slider_title == 'Configure Syslog'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_Switch_Inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Click on inactive tab")
        syslog.click_inactive_tab()
        log.info("Read the tab color after switching")
        tab_color = syslog.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Verify_Switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        log.info("Click on all tab")
        syslog.click_all_tab()
        log.info("Read the tab color after switching")
        tab_color = syslog.get_all_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.regression
    def test_05_create_syslog(self):
        """
            verify the create syslog
            Validation . On basis of increase in number of syslogs
            TC_ID : 005
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        label = Labels(self.driver)
        config_trigger = ConfigureTrigger(self.driver)
        log.info("Click on to main menu")
        nav.click_main_menu()
        log.info("Click on to label module for redirection")
        nav.navigate_labels()
        label.visibility_of_first_label()
        label.click_new_label()
        global label_text
        label_text = "test_syslog" + action.get_current_time()
        log.info("Entering new label name")
        label.put_label_name(label_text)
        log.info("Entering label description")
        label.put_description("Test Description")
        log.info("Click on create label button")
        label.create_Label()
        log.info("Click on to close label creation tooltip ")
        label.click_close_tooltip()
        log.info("Click on Main menu")
        nav.click_main_menu()
        log.info("Click on configure event")
        nav.navigate_configure_event()
        config_trigger.visibility_of_first_configure_trigger()
        log.info("Creating a New Configure Trigger")
        config_trigger.click_new_configure_trigger_btn()
        log.info("Enter the data into Input Fields")
        global source_app
        source_app = "TestSource_App" + action.get_current_time()
        config_trigger.put_source_app_name(source_app)
        global Event_Type
        log.info("Enter the SourceEvent Data")
        Event_Type = "TestSourceEvent_Type" + action.get_current_time()
        config_trigger.put_source_event_type(Event_Type)
        config_trigger.click_on_label_field()
        label_path = "//ul[@id='dropdown-list']//li//div//div//div[text()='" + label_text + "']"
        log.info("Select the test_syslog label")
        config_trigger.select_test_syslog_label(label_path)
        log.info("Enter the Create Button")
        config_trigger.click_create_btn()
        log.info("click on close toop tip")
        config_trigger.click_close_tooltip()
        log.info("Click on Main menu")
        nav.click_admin_menu()
        log.info("Click on SysLogs tab from Admin Page")
        syslog.click_syslogs()
        log.info("Click on all tab")
        syslog.click_all_tab()
        log.info("Click On New Syslog Button")
        global syslog_title
        log.info("Generating the new Syslog title")
        syslog_title = "test_syslog_" + action.get_current_time()
        log.info("Get the Syslog count before the create function")
        count = syslog.get_syslog_count()
        log.info("Click on the create new button")
        syslog.click_new_syslog()
        log.info("Add the Syslog title in the specified input field")
        syslog.put_syslog_title(syslog_title)
        port_number = "1045"
        log.info("Add the Port Number in the specified input field")
        syslog.put_port_number(port_number)
        log.info("Select the Source Event App for the Syslog")
        log.info("Add the Source App Name in the specified input field")
        source_app_path = "//ul[@id='dropdown-list']//li//div//div//div[text()='" + source_app + "']"
        log.info("Select the Source Event App for the Syslog")
        syslog.click_on_list_Source_Events_App()
        syslog.select_test_syslog_source_event_app(source_app_path)
        log.info("Select the Source Event Type for the Syslog")
        syslog.click_on_list_Source_Events_Type()
        syslog.select_first_source_event_type()
        syslog.click_save_btn()
        log.info("click on close toop tip")
        syslog.click_close_tooltip()
        assert count + 1 == syslog.get_syslog_count()

    @pytest.mark.regression
    def test_06_Search_syslog(self):
        """
            Verify the Searchbar Functionality is working.
            Validation-1: On basis of the Name Comparison.

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Search Functionality of Syslogs")
        syslog.search_input_string(syslog_title)
        syslog.click_enter_for_search()
        search_result = syslog.get_name_first_syslog()
        log.info("Clearing the Search Field")
        syslog.clear_search()
        assert syslog_title == search_result

    @pytest.mark.regression
    def test_07_check_the_dropdown_Edit_visibility(self):
        """
            Verify the dropdown button Visibility.
            Validation -1 : Check The Edit Slider Title

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        log.info("Click on Edit button in Drop down")
        syslog.click_edit_button()
        log.info("Get the Slider Name")
        slider_title = syslog.get_slider_title()
        log.info("Close the Slider")
        syslog.click_slider_close()
        assert slider_title == "Edit Syslog"

    @pytest.mark.regression
    def test_08_deactivating_syslog(self):
        """
            Verify the deactivating syslog functionality
            Validation 1: Based on the Status of the syslog

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Get the status of Syslogs before deactivating")
        status_before_deactivating = syslog.get_status_of_syslog()
        log.info("Mouse hover the dropdown")
        syslog.check_drop_down()
        syslog.click_deactivate_button()
        log.info("Get the status of Syslogs after deactivating")
        status_after_deactivating = syslog.get_status_of_syslog()
        log.info("click on close toop tip")
        syslog.click_close_tooltip()
        assert status_before_deactivating == 'Active' and status_after_deactivating == 'Inactive'

    @pytest.mark.regression
    def test_09_activating_syslog(self):
        """
            Verify the deactivating syslog functionality
            Validation 1: Based on the Status of the syslog

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Get the status of Syslogs before activating")
        status_before_activating = syslog.get_status_of_syslog()
        log.info("Mouse hover the dropdown")
        syslog.check_drop_down()
        syslog.click_activate_button()
        log.info("Get the status of Syslogs after activating")
        status_after_activating = syslog.get_status_of_syslog()
        log.info("click on close toop tip")
        syslog.click_close_tooltip()
        assert status_after_activating == 'Active' and status_before_activating == 'Inactive'

    @pytest.mark.regression
    def test_10_delete_syslog(self):
        """
            Verify the delete syslog functionality
            Validation 1: Based on the Count of the syslogs

        """
        syslog = Syslogs(self.driver)
        log = self.getlogger()
        log.info("Get the number of Syslogs before delete")
        count_before_delete = syslog.get_syslog_count()
        log.info("Mouse over the dropdown")
        syslog.check_drop_down()
        syslog.click_delete_button()
        log.info("click on close toop tip")
        syslog.click_close_tooltip()
        assert count_before_delete == syslog.get_syslog_count() + 1
