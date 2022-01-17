import pytest

from pageObjects.Navigation import Navigation
from pageObjects.Dashboard import Dashboard
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestDashBoard(Base):

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_dashboard_redirection(self):
        """
            Verify Dashboard redirection from Main Menu
            Validation - 1. On the basis of Window's title
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.click_Main_Menu())
        action.click(nav.Navigate_Dashboard())
        assert action.getTitle() in 'Dashboard | Cyware Orchestrate'

    # @pytest.mark.smoke
    # @pytest.mark.readOnly
    # def test_02_click_on_view_all(self):
    #     """
    #         Verify that View All button is working as expected or not
    #         Validation - 1. On the basis of Legends button visibility
    #     """
    #
    #     dashboard = Dashboard(self.driver)
    #     action = Action(self.driver)
    #     elements_list = dashboard.get_all_elements()
    #     for element in range(0, len(elements_list)):
    #         elements_list[element].click()
    #         t = action.check_visibility_of_element(dashboard.visibility_of_legends_btn())
    #         action.click(dashboard.click_on_back_btn())
    #         assert t is True
