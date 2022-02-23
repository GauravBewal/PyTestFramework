import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestHomePage(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Verify_Main_Menu_redirection(self):
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
        assert action.check_visibility_of_element(nav.mouse_hover_menu_synopsis()) is True
