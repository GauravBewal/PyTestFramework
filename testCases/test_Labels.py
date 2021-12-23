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
            TC_ID: Label-TC-001
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on to main menu")
        action.click(nav.Click_Main_Menu())
        log.info("Click on to label module for redirection")
        action.click(nav.Navigate_Labels())
        log.info("Validating the page title")
        assert action.getTitle() in 'Label List | Cyware Orchestrate'

    @pytest.mark.smoke
    def test_02_create_label_without_name(self):
        """
        Verify user is able to get error message when tried to create a label without name
         TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Click on to New Label Button")
        action.click(label.click_New_Label())
        log.info("Enter description of a label")
        action.sendKeys(label.put_Description(), "description")
        log.info("Click on to create label button")
        action.click(label.create_Label())
        time.sleep(ReadConfig.sleepWait())
        error_msg = action.getText(label.get_label_field_error_msg())
        log.info("Click on to close label slider button")
        action.click(label.close_label_slider())
        log.info("Validating the error message")
        assert error_msg in 'Label Name is required'

    @pytest.mark.smoke
    def test_03_create_label(self):
        """
            Verify Label Create functionality
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        time.sleep(ReadConfig.sleepWait())
        log.info("Reading the count of total labels before creating a new label")
        before_label_creation_count = (action.getCountfromString(label.get_label_count()))
        log.info("Click on to create new label")
        action.click(label.click_New_Label())
        label_text = "Label_" + action.CurrentTime()
        log.info("Entering new label name")
        action.sendKeys(label.put_Label_Name(), label_text)
        log.info("Entering label description")
        action.sendKeys(label.put_Description(), "Test Description")
        log.info("Click on create label button")
        action.click(label.create_Label())
        log.info("Click on to close label creation tooltip ")
        action.click(label.click_close_tooltip())
        time.sleep(ReadConfig.sleepWait())
        log.info("Reading count of total labels after creating a new label")
        after_label_creation_count = action.getCountfromString(label.get_label_count())
        get_created_label_name = action.getText(label.top_1_label_name())
        log.info("Validating total count of labels before and after creation of new label, also checking the "
                 "newly created label is listing or not")
        assert label_text == get_created_label_name and before_label_creation_count + 1 == after_label_creation_count

    @pytest.mark.smoke
    def test_04_search_label(self):
        """
            Verify Search functionality of the Labels
            TC_ID: Label-TC-005
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        search_text = "Label"
        log.info("Entering" + search_text + "text for searching")
        action.sendKeys(label.put_Search_String(), search_text)
        log.info("Click on ENTER")
        action.clickEnter(label.put_Search_String())
        time.sleep(ReadConfig.sleepWait())
        action.click(label.clear_search())
        read_top_search_result = action.getText(label.top_1_label_name())
        log.info("Validating search results")
        assert search_text in read_top_search_result

    @pytest.mark.smoke
    def test_05_update_label(self):
        """
          verify user is able to update the label
          TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Click on label present at top in listing")
        action.click(label.top_1_label_name())
        log.info("Deleting and Entering new name to the existing label")
        action.clear_field(label.put_Label_Name())
        new_label_name = "Label_" + action.CurrentTime()
        action.sendKeys(label.put_Label_Name(), new_label_name)
        log.info("Deleting and entering new description the existing label")
        action.clear_field(label.put_Description())
        action.sendKeys(label.put_Description(), "updated description")
        time.sleep(ReadConfig.sleepWait())
        log.info("Click on update label button")
        action.click(label.click_update_label())
        log.info("Click on close tooltip")
        action.click(label.click_close_tooltip())
        updated_label_name = action.getText(label.top_1_label_name())
        log.info("Validating the new label name is updated or not ")
        assert new_label_name == updated_label_name

    @pytest.mark.smoke
    def test_06_read_modified_created_column_data(self):
        """
        Verify user is able to see the created by and modified by details after creating and modifying label
        TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Reading label created user name")
        label_created_user_name = action.getText(label.get_label_created_user())
        log.info("Reading label modified user name")
        label_modified_user_name = action.getText(label.get_label_modified_user())
        log.info("Validating both created and modified user")
        assert label_created_user_name == label_modified_user_name

    @pytest.mark.smoke
    def test_07_deactivate_label(self):
        """
        Verify label is being listed under inactive tab once label was de-activated
        TC_ID: Label-TC-003
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        label_name_before_deactivating = action.getText(label.top_1_label_name())
        log.info("Click on label present at top in listing")
        action.click(label.top_1_label_name())
        time.sleep(ReadConfig.sleepWait())
        log.info("Click on label toggle")
        action.click(label.click_toggle())
        log.info("Click on update label button")
        time.sleep(ReadConfig.sleepWait())
        action.click(label.click_update_label())
        log.info("Click on inactive button")
        # navigating inactive tab to check whether the label is de-activated or not
        action.click(label.click_InActive())
        time.sleep(ReadConfig.sleepWait())
        # log.info("Click on to close label creation tooltip ")
        # action.click(label.click_close_tooltip())
        label_name_after_deactivating = action.getText(label.top_1_label_name())
        log.info("Validating label name before and after deactivating")
        # checking whether same label is visible in inactive tab listing after deactivating it
        assert label_name_before_deactivating == label_name_after_deactivating
