import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Syslogs import Syslogs
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestSyslogs(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_admin_SysLogs(self):
        """
            Verify redirection of SysLogs from the admin page
            Validation - 1. On the basis of Window's title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on Main menu")
        action.click(nav.click_Admin_Menu())
        log.info("Click on SysLogs tab from Admin Page")
        action.click(syslog.click_SysLogs())
        assert action.getTitle() in 'Syslogs | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_click_new_syslogs(self):
        """
            Verify create button functionality of new webhook
            Validation - 2. On the basis of slider title
        """
        log = self.getlogger()
        syslog = Syslogs(self.driver)
        action = Action(self.driver)
        log.info("Click on add syslog button")
        action.click(syslog.click_new_Syslog())
        log.info("Read the slider title")
        slider_title = action.getText(syslog.get_slider_title())
        log.info("Click on close slider button")
        action.click(syslog.click_slider_close())
        assert slider_title == 'Configure Syslog'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_switch_inactive_tab(self):
        """
            Verify switch to inactive tab from active tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        action = Action(self.driver)
        syslog = Syslogs(self.driver)
        log.info("Click on inactive tab")
        action.click(syslog.click_inactive_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(syslog.click_inactive_tab())
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_switch_All_tab(self):
        """
            Verify switch to All tab from inactive tab
            Validation - 3. On the basis of tab color
        """
        log = self.getlogger()
        action = Action(self.driver)
        syslog = Syslogs(self.driver)
        log.info("Click on inactive tab")
        action.click(syslog.click_All_tab())
        log.info("Read the tab color after switching")
        tab_color = action.getElementColor(syslog.click_All_tab())
        assert tab_color == '#1a3ee8'

