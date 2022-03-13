import pytest

from pageObjects.Navigation import Navigation
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestHomePage(Base):

    @pytest.mark.regression
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

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_02_Verify_searchbar_functionality(self):
        """
        Verify the user is able to search or not
        Validation-1 : Based on Search Result Visibility
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("Enter string in search bar")
        nav.Enter_string_in_searchbar("Dashboard")
        name = nav.read_searchbar_result()
        log.info("Click on clear search button")
        nav.click_clear_search_result_btn()
        assert name == 'Dashboard'

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Verify_get_started_functionality(self):
        """
        Verify the user is able to Click Get Started Button or not
        Validation-1 : Based on Visibility of Walkthrough options
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("clicking on Get Started Button")
        nav.click_get_started_button()
        elements_list = nav.get_list_of_elements(nav.get_walkthrough_option_elements(), nav.walkthrough_options)
        for element in range(0, len(elements_list)):
            visibility = nav.visibility_of_walkthrough_option(elements_list[element])
            assert visibility is True

    @pytest.mark.readOnly
    @pytest.mark.regression
    def test_04_Verify_Overview_walkthrough_btn(self):
        """
        Veirfy whether user is able to click on the walkthrough overview button
        Validation 1: Based on the walkthrough intiated visibility
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("Click on the over view button")
        nav.click_on_overview_btn()
        log.info("Check whether walkthrough is initiated or not")
        visibility = nav.visibility_of_walkthrough_close_btn()
        assert visibility is True
        log.info("Click on the close walkthrough button")
        nav.click_on_close_walkthrough()

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_05_Verify_Manage_Playbooks_walkthrough_btn(self):
        """
        Verify whether user is able to start the playbook walkthrough after clicking
        Validation 1: Based on the walkthrough initiated in playbooks module
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("clicking on Get Started Button")
        nav.click_get_started_button()
        log.info("Click on the Manage Playbook walkthrough button")
        nav.click_playbook_walkthrough_btn()
        log.info("Check Walkthrough is initiated or not")
        visibility = nav.visibility_of_walkthrough_close_btn()
        assert visibility is True
        log.info("Close the walkthrough")
        nav.click_on_close_walkthrough()

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_06_Verify_Apps_walkthrough_btn(self):
        """
        Verify whether user is able to start the apps walkthrough after clicking
        Validation 1: Based on the walkthrough initiated in apps module
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        log.info("Click on the main menu")
        nav.click_main_menu()
        log.info("clicking on Get Started Button")
        nav.click_get_started_button()
        log.info("Click on the apps walkthrough button")
        nav.click_apps_walkthrough_btn()
        log.info("Check Walkthrough is initiated or not")
        visibility = nav.visibility_of_walkthrough_close_btn()
        assert visibility is True
        log.info("Close the walkthrough")
        nav.click_on_close_walkthrough()
