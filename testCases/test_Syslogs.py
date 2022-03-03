import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Syslogs import Syslogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestSyslogs(Base):

    @pytest.mark.smoke
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
        assert action.get_title() in 'Syslogs | Cyware Orchestrate'

    @pytest.mark.smoke
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

    @pytest.mark.smoke
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

    @pytest.mark.smoke
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
