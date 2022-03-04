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

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Verify_searchbar_functionality(self):
        """
        Verify the user is able to search or not
        Validation-1 : Based on Search Result Visibility
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("clicking on search bar")
        nav.Enter_string_in_searchbar("Dashboard")
        name = nav.read_searchbar_result()
        assert name == 'Dashboard'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Verify_Get_Started_Functionality(self):
        """
        Verify the user is able to Click Get Started Button or not
        Validation-1 : Based on S
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("clicking on Get Started Button")
        nav.click_get_started_button()
        elements_list = nav.get_list_of_elements(nav.get_walkthrough_option_elements(), nav.walkthrough_options)
        for element in range(0, len(elements_list)):
            visibility = nav.visibility_of_walkthrough_option(elements_list[element])
            assert visibility is True
