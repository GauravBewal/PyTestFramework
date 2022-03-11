import pytest

from pageObjects.Labels import Labels
from pageObjects.Navigation import Navigation
from pageObjects.Playbooks import Playbooks
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

    @pytest.mark.regression
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
        log.info("Check if walk through is initiated")
        nav.click_on_close_walkthrough()
        log.info("Click on to main menu")
        nav.click_main_menu()
        log.info("Click on to label module for redirection")
        nav.navigate_labels()
        log.info("Read the no of active labels available")
        global active_labels
        active_labels = label.get_label_count()
        log.info("Validating the page title")
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'Labels | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
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

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_03_Switch_to_All_tab(self):
        """
                Verify whether user is able to switch to all tab
                Validation based on the tab color
                """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Click on the inactive tab")
        label.click_all_tab()
        log.info("Read the tab color")
        tab_color = label.get_all_tab_color()
        log.info("Read the no of active labels available")
        all_created_labels = label.get_label_count()
        assert tab_color == '#1a3ee8' and all_created_labels == inactive_labels + active_labels

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_04_Create_Label_Without_Name(self):
        """
            Verify user is able to get error message when tried to create a label without any name
            TC_ID: Label-TC-002
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Switch to active tab")
        label.click_active_tab()
        log.info("Click on to New Label Button")
        label.click_new_label()
        log.info("Enter description of a label")
        label.put_description("description")
        log.info("Click on to create label button")
        label.create_Label()
        error_msg = label.get_label_field_error_msg()
        log.info("Click on to close label slider button")
        label.close_label_slider()
        log.info("Validating the error message")
        assert error_msg in 'Label Name is required'

    @pytest.mark.regression
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
        label.click_new_label()
        global label_text
        label_text = "Label_" + action.get_current_time()
        log.info("Entering new label name")
        label.put_label_name(label_text)
        log.info("Entering label description")
        label.put_description("Test Description")
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

    @pytest.mark.regression
    def test_06_Search_Label(self):
        """
            Verify Search functionality of the Labels
            TC_ID: Label-TC-005
        """
        log = self.getlogger()
        label = Labels(self.driver)
        log.info("Entering" + label_text + "text for searching")
        label.put_search_string(label_text)
        log.info("Click on ENTER")
        label.click_enter_for_search()
        read_top_search_result = label.top_1_label_name()
        label.clear_search()
        log.info("Validating search results")
        assert label_text in read_top_search_result

    @pytest.mark.regression
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
        global new_label_name
        new_label_name = "Label_" + action.get_current_time()
        label.put_label_name(new_label_name)
        log.info("Deleting and entering new description the existing label")
        label.clear_description_field()
        label.put_description("updated description")
        log.info("Click on update label button")
        label.click_update_label()
        log.info("Click on close tooltip")
        label.click_close_tooltip()
        updated_label_name = label.top_1_label_name()
        log.info("Validating the new label name is updated or not ")
        assert new_label_name == updated_label_name

    @pytest.mark.regression
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

    @pytest.mark.regression
    def test_09_create_playbook_with_label(self):
        """
        Verify whether user is able to see the created label in playbook
        Validation-1: Based on the label visibility
        """
        log = self.getlogger()
        playbook = Playbooks(self.driver)
        action = Action(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to playbook module")
        nav.navigate_manage_playbook()
        log.info("Visibility of first playbook")
        playbook.visibility_of_first_playbook()
        log.info("Click on create new playbook")
        playbook.click_on_create_playbook_btn()
        log.info("Clear default name")
        playbook.click_on_close_walkthrough()
        playbook.remove_default_playbook_name()
        log.info("Enter playbook name")
        global playbook_name
        playbook_name = "label_test" + action.get_current_time()
        playbook.enter_playbook_name(playbook_name)
        log.info("Click on labels dropdown")
        playbook.click_on_label_field()
        log.info("Enter the label name")
        playbook.put_label_name(new_label_name)
        visibility = playbook.visibility_of_label(new_label_name)
        assert visibility is True
        playbook.click_on_top_searched_label()
        log.info("Click on label field to close")
        playbook.click_on_label_field()
        log.info("Mouse hover on the save button")
        playbook.mouse_hover_on_save_btn()
        log.info("Click on save and exit button")
        playbook.click_save_and_exit_btn()
        log.info("Read the playbook created successful message")
        successful_msg = playbook.get_playbook_created_successful_txt()
        playbook.close_tooltip()
        playbook.click_on_back_button()
        assert successful_msg == 'Playbook created successfully.'

    @pytest.mark.regression
    def test_10_Deactivate_Label(self):
        """
        Verify label is being listed under inactive tab once label was de-activated
        TC_ID: Label-TC-003
        """
        log = self.getlogger()
        label = Labels(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on main menu")
        nav.click_main_menu()
        log.info("Navigate to playbook module")
        nav.navigate_labels()
        log.info("Check for visibility of first label")
        label.visibility_of_first_label()
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
