import pytest

from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestDataSync(Base):

    @pytest.mark.smoke
    def test_01_data_sync_redirection(self):
        """
            Verify Data Sync redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Main_Menu())
        action.click(nav.Navigate_Data_Sync())
        assert action.getTitle() in 'Data Sync Jobs | Cyware Orchestrate'
