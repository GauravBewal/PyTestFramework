import pytest

from pageObjects.Labels import Labels
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestLabels(Base):

    @pytest.mark.smoke
    def test_01_labels_redirection(self):
        """
            Verify Labels redirection from Main Menu
        """
        nav = Navigation(self.driver)
        action = Action(self.driver)
        action.click(nav.Click_Main_Menu())
        action.click(nav.Navigate_Labels())
        assert action.getTitle() in 'Label List | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_04_create_label(self):
        """
            Verify Label Create functionality
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        action.click(label.click_New_Label())
        action.sendKeys(label.put_Label_Name(), "Label_" + action.CurrentTime())
        action.sendKeys(label.put_Description(), "Test Description")
        action.click(label.create_Label())

    @pytest.mark.smoke
    def test_03_search_label(self):
        """
            Verify Search functionality of the Labels
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        action.sendKeys(label.put_Search_String(), "Label")
        action.clickEnter()
