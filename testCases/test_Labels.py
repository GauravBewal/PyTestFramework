import time

import pytest

from configuration.readConfiguration import ReadConfig
from pageObjects.Labels import Labels
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestLabels(Base):
    global active_labels
    active_labels = 0
    global inactive_labels
    inactive_labels = 0
    global label_text
    label_text = ''

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_01_Labels_redirection(self):
        """
            Verify Labels Page redirection from Main Menu
            TC_ID: Label-TC-001
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Click on to main menu")
        nav.click_Main_Menu()
        log.info("Click on to label module for redirection")
        nav.Navigate_Labels()
        log.info("Read the no of active labels available")
        global active_labels
        active_labels = label.get_label_count()
        log.info("Validating the page title")
        assert action.getTitle() == 'Labels | Cyware Orchestrate'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_02_Switch_to_Inactive_tab(self):
        """
        Verify whether user is able to switch to inactive tab
        Validation based on the tab color
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Click on the inactive tab")
        label.click_inactive_tab()
        log.info("Read the no of inactive labels available")
        global inactive_labels
        inactive_labels = label.get_label_count()
        log.info("Read the tab color")
        tab_color = label.get_inactive_tab_color()
        assert tab_color == '#1a3ee8'

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_03_Switch_to_All_tab(self):
        """
                Verify whether user is able to switch to all tab
                Validation based on the tab color
                """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Click on the inactive tab")
        label.click_All_tab()
        log.info("Read the tab color")
        tab_color = label.get_all_tab_color()
        log.info("Read the no of active labels available")
        all_created_labels = label.get_label_count()
        assert tab_color == '#1a3ee8' and all_created_labels == inactive_labels + active_labels

    @pytest.mark.smoke
    @pytest.mark.readOnly
    def test_04_Create_Label_Without_Name(self):
        """
            Verify user is able to get error message when tried to create a label without any name
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Switch to active tab")
        label.click_Active_tab()
        log.info("Click on to New Label Button")
        label.click_New_Label()
        log.info("Enter description of a label")
        label.put_Description("description")
        log.info("Click on to create label button")
        label.create_Label()
        error_msg = label.get_label_field_error_msg()
        log.info("Click on to close label slider button")
        label.close_label_slider()
        log.info("Validating the error message")
        assert error_msg in 'Label Name is required'

    @pytest.mark.smoke
    def test_05_Create_Label(self):
        """
            Verify Label Create functionality
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Reading the count of total labels before creating a new label")
        before_label_creation_count = label.get_label_count()
        log.info("Click on to create new label")
        label.click_New_Label()
        global label_text
        label_text = "Label_" + action.currentTime()
        log.info("Entering new label name")
        label.put_Label_Name(label_text)
        log.info("Entering label description")
        label.put_Description("Test Description")
        log.info("Click on create label button")
        label.create_Label()
        log.info("Click on to close label creation tooltip ")
        label.click_close_tooltip()
        log.info("Reading count of total labels after creating a new label")
        after_label_creation_count = label.get_label_count()
        get_created_label_name = label.top_1_label_name()
        log.info("Validating total count of labels before and after creation of new label, also checking the "
                 "newly created label is listing or not")
        assert label_text == get_created_label_name and before_label_creation_count + 1 == after_label_creation_count

    @pytest.mark.smoke
    def test_06_Search_Label(self):
        """
            Verify Search functionality of the Labels
            TC_ID: Label-TC-005
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Entering" + label_text + "text for searching")
        label.put_Search_String(label_text)
        log.info("Click on ENTER")
        label.click_Enter_for_Search()
        read_top_search_result = label.top_1_label_name()
        label.clear_search()
        log.info("Validating search results")
        assert label_text in read_top_search_result

    @pytest.mark.smoke
    def test_07_Update_Label(self):
        """
          verify user is able to update the label
          TC_ID: Label-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        label = Labels(self.driver)
        log.info("Click on label present at top in listing")
        label.click_top_first_label()
        log.info("Deleting and Entering new name to the existing label")
        label.clear_label_field()
        new_label_name = "Label_" + action.currentTime()
        label.put_Label_Name(new_label_name)
        log.info("Deleting and entering new description the existing label")
        label.clear_Description_field()
        label.put_Description("updated description")
        log.info("Click on update label button")
        label.click_update_label()
        log.info("Click on close tooltip")
        label.click_close_tooltip()
        updated_label_name = label.top_1_label_name()
        log.info("Validating the new label name is updated or not ")
        assert new_label_name == updated_label_name

    @pytest.mark.smoke
    def test_08_Read_Modified_Created_Column_Data(self):
        """
        Verify user is able to see the created by and modified by details after creating and modifying label
        TC_ID: Label-TC-002
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Reading label created user name")
        label_created_user_name = label.get_label_created_user()
        log.info("Reading label modified user name")
        label_modified_user_name = label.get_label_modified_user()
        log.info("Validating both created and modified user")
        assert label_created_user_name == label_modified_user_name

    @pytest.mark.smoke
    def test_09_Deactivate_Label(self):
        """
        Verify label is being listed under inactive tab once label was de-activated
        TC_ID: Label-TC-003
        """
        log = self.getlogger()
        label = Labels(self.driver)
        label_name_before_deactivating = label.top_1_label_name()
        log.info("Click on label present at top in listing")
        label.click_top_first_label()
        log.info("Click on label inactive toggle")
        label.click_inactive_toggle()
        log.info("Click on update label button")
        label.click_update_label()
        label.click_close_tooltip()
        log.info("Click on inactive button")
        # navigating inactive tab to check whether the label is de-activated or not
        label.click_inactive_tab()
        label_name_after_deactivating = label.top_1_label_name()
        log.info("Validating label name before and after deactivating")
        # checking whether same label is visible in inactive tab listing after deactivating it
        assert label_name_before_deactivating == label_name_after_deactivating
