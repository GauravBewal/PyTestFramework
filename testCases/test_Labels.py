import time

import pytest

from configuration.readConfiguration import ReadConfig
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
    def test_02_create_label(self):
        """
            Verify Label Create functionality
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        before_label_creation_count = int(action.getcount(label.get_label_count()))
        action.click(label.click_New_Label())
        label_text = "Label_" + action.CurrentTime()
        action.sendKeys(label.put_Label_Name(), label_text)
        action.sendKeys(label.put_Description(), "Test Description")
        action.click(label.create_Label())
        action.click(label.click_close_tooltip())
        time.sleep(ReadConfig.sleepWait())
        after_label_creation_count = int(action.getcount(label.get_label_count()))
        get_created_label_name = action.getText(label.top_1_label_name())
        assert label_text == get_created_label_name and before_label_creation_count <= after_label_creation_count

    @pytest.mark.smoke
    def test_03_search_label(self):
        """
            Verify Search functionality of the Labels
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        search_text = "Label"
        action.sendKeys(label.put_Search_String(), search_text)
        action.clickEnter(label.put_Search_String())
        time.sleep(ReadConfig.sleepWait())
        read_top_search_result = action.getText(label.top_1_label_name())
        assert search_text in read_top_search_result

    @pytest.mark.smoke
    def test_04_update_label(self):
        """
          verify user is able to update the label
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        action.click(label.top_1_label_name())
        action.clear_field(label.put_Label_Name())
        new_label_name = "Label_" + action.CurrentTime()
        action.sendKeys(label.put_Label_Name(), new_label_name)
        action.clear_field(label.put_Description())
        action.sendKeys(label.put_Description(), "updated description")
        time.sleep(ReadConfig.sleepWait())
        action.click(label.click_update_label())
        action.click(label.click_close_tooltip())
        updated_label_name = action.getText(label.top_1_label_name())
        assert new_label_name == updated_label_name

    @pytest.mark.smoke
    def test_05_deactivate_label(self):
        """
        Verify label is being listed under inactive tab once label was de-activated
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        label_name_before_deactivating = action.getText(label.top_1_label_name())
        action.click(label.top_1_label_name())
        action.click(label.click_toggle())
        action.click(label.click_update_label())
        # navigating inactive tab to check whether the label is de-activated or not
        action.click(label.click_InActive())
        time.sleep(ReadConfig.sleepWait())
        label_name_after_deactivating = action.getText(label.top_1_label_name())
        ### checking whether same label is visible in inactive tab listing after deactivating it ###
        assert label_name_before_deactivating == label_name_after_deactivating

    @pytest.mark.smoke
    def test_06_create_label_without_name(self):
        """
        Verify user is able to get error message when tried to create a label without name
        """
        action = Action(self.driver)
        label = Labels(self.driver)
        action.click(label.click_New_Label())
        action.sendKeys(label.put_Description(), "description")
        action.click(label.create_Label())
        error_msg = action.getText(label.get_label_field_error_msg())
        assert error_msg in 'Label Name is required'
