import pytest

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
        log.info("Click on inactive tab")
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
        log.info("Click On New Webhook Button")
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
        syslog.click_on_list_Source_Events_App()
        syslog.select_test_syslog_source_event_app()
        log.info("Select the Source Event Type for the Syslog")
        syslog.click_on_list_Source_Events_Type()
        syslog.select_test_syslog_source_event_type()
        syslog.click_save_btn()
        assert count + 1 == syslog.get_syslog_count()

    @pytest.mark.regression
    def test_06_check_the_dropdown_Edit_visibility(self):
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
    def test_07_delete_syslog(self):
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
        assert count_before_delete == syslog.get_syslog_count() + 1
