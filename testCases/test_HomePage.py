import time

import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base
from configuration.readConfiguration import ReadConfig


@pytest.mark.usefixtures("setup")
class TestHomePage(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_verify_main_menu_redirection(self):
        """
            Verify Main Menu is clickable
            Validation: Based on the menu sysnopsis button visibility
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on the main menu")
        action.click(nav.click_Main_Menu())
        time.sleep(ReadConfig.Wait_3_Sec())
        log.info("Check for the visibility of menu synopsis button")
        assert action.check_visibility_of_element(nav.click_synopsis_btn()) is True
