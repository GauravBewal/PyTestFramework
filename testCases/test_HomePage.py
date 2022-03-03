import pytest

from pageObjects.Navigation import Navigation
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
        log.info("Click on the main menu")
        nav.click_main_menu()
        log.info("Check for the visibility of menu synopsis button")
        assert nav.visibility_of_menu_synopsis_btn() is True
