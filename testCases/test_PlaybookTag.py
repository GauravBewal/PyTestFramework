import time

import pytest

from pageObjects.AdminPage import Admin
from pageObjects.Dashboard import Dashboard
from pageObjects.CommonElements import Tooltip, FilterandSort
from pageObjects.Navigation import Navigation
from pageObjects.PlaybookTags import PlaybookTags
from pageObjects.Playbooks import Playbooks
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybookTags(Base):


    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.playbooktag
    def test_01_Playbook_Tag_redirection(self):
        """
            Verify PlaybookTag Page redirection from Main Menu
            Validation-1: Based on the Page Name
            TC_ID: PlaybookTag-TC-001
        """
        log = self.getlogger()
        admin = Admin(self.driver)
        nav = Navigation(self.driver)
        action = Action(self.driver)
        log.info("Click on Admin Menu")
        nav.click_admin_menu()
        log.info("Click on Playbook Tags tab from Admin Page")
        admin.click_playbook_tags()
        error_msg_visibility = nav.verify_error_msg_after_navigation()
        assert action.get_title() == 'Playbook Tags | Cyware Orchestrate' and error_msg_visibility is False

    @pytest.mark.regression
    @pytest.mark.readOnly
    @pytest.mark.playbooktag
    def test_02_Create_Button_Visibility(self):
        """
        Verify the Create button Visibility
        Validation-1: Verify based on slider Name
        TC_ID: PlaybookTag-TC-002
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Click on Create New Playbook Tag")
        tag.click_new_playbookTag()
        Slider_Name = tag.get_slider_name()
        tag.close_slider_btn()
        assert Slider_Name == "Add Tag"

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_03_Create_New_Playbook_Tag(self):
        """
            Verify PlaybookTag Create functionality
            Validation-1: Validaion BAsed on the Count
            TC_ID: PlaybookTag-TC-003
        """
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        action = Action(self.driver)
        tag = PlaybookTags(self.driver)
        log.info("Reading the count of total playbookTags before creating a new playbookTag")
        before_playbookTag_creation_count = tag.get_playbookTag_count()
        log.info("Click on to create new PlaybookTag")
        tag.click_new_playbookTag()
        global playbook_tag_text
        playbook_tag_text = "PlaybookTag_" + action.get_current_time()
        log.info("Entering new PlaybookTag name")
        tag.put_playbooktag_title(playbook_tag_text)
        log.info("Entering PlaybookTag description")
        tag.put_playbooktag_description("Test Description")
        log.info("Click on Save PlaybookTag button")
        tag.save_playbookTag()
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        tooltip.click_close_tooltip()
        log.info("Check visibility of first playbooktag")
        assert tag.visibility_of_created_playbook_tag() is True
        log.info("Reading count of total labels after creating a new playbookTag")
        after_playbookTag_creation_count = tag.get_playbookTag_count()
        log.info("Validating total count of PlaybookTag before and after creation of new label, also checking the "
                 "newly created PlaybookTag is listing or not")
        assert before_playbookTag_creation_count + 1 == after_playbookTag_creation_count

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_04_Search_Playbook_Tag(self):
        """
        Verify User is able to search Created PLaybookTag
        Validation-1: Validation Based on the Top one Tag Name
        TC_ID: PlaybookTag-TC-006
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Searching the Playbook Tag")
        tag.click_on_searchbar()
        log.info("Enter playbook tag name to search")
        tag.put_string_in_searchbar(playbook_tag_text)
        log.info("CLick on enter")
        tag.press_enter()
        log.info("Read the first playbook tag name")
        tag_name = tag.get_playbooktag_name()
        assert tag_name == playbook_tag_text

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_05_Update_Playbook_Tag(self):
        """
            Update the PlaybookTag
            Validation-1: Validated Based on new Updated Name
            TC_ID: PlaybookTag-TC-007
        """
        global updated_playbooktag_title
        log = self.getlogger()
        tooltip = Tooltip(self.driver)
        tag = PlaybookTags(self.driver)
        action = Action(self.driver)
        log.info("Updating the PlaybookTag")
        tag.click_playbooktag()
        log.info("Clicking on Editing Button in Slider")
        tag.click_on_Edit_Button()
        tag.clear_playbooktag_title()
        updated_playbooktag_title = "PlaybookTag_" + action.get_current_time()
        log.info("Adding New playbookTag Title")
        tag.put_playbooktag_title(updated_playbooktag_title)
        log.info("Updating the PlaybookTag Title")
        tag.clear_playbooktag_description()
        tag.put_playbooktag_description("Updated Description")
        log.info("Click on Save/update PlaybookTag button")
        tag.save_playbookTag()
        tooltip_msg = tooltip.read_tooltip_msg()
        assert 'Success' == tooltip_msg
        tooltip.click_close_tooltip()
        tag.click_clear_search_btn()
        tag.put_string_in_searchbar(updated_playbooktag_title)
        tag.press_enter()
        assert tag.visibility_of_created_playbook_tag() is True \
               and updated_playbooktag_title == tag.get_playbooktag_name()
        tag.click_clear_search_btn()
        tag.press_enter()


    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_06_Verify_Default_TagName_Ascending_Sort(self):
        """
            Check the Sorting based on the Tag Name in Ascending
            Validation Based On the Names
            Tc_ID : PlaybookTAg-Tc-004
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        assert tag.visibility_of_created_playbook_tag() is True
        log.info("Checking The sort based on Tag Name")
        log.info("Verify the Ascending Order of the Tag Name")
        assert tag.get_first_tagname() < tag.get_second_playbookTag()

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_07_Check_Sort_Based_On_Created(self):
        """
                Verify User is able to sort based on Created Time of Playbook
                Validatio-1: Validation Based on the Button Name of Selected
                TC_ID: PlaybookTag-TC-005
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        filterandsort = FilterandSort(self.driver)
        log.info("Mouse overing the sort Option")
        filterandsort.mouse_hover_on_sort()
        log.info("Changing sort to the Created")
        filterandsort.click_on_created()
        assert tag.visibility_of_created_playbook_tag() is True
        log.info("Changing sort to Descending Order")
        filterandsort.changing_sort_to_descending_order()
        assert filterandsort.get_name_sorted_filter() == "Created"

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_08_Check_Created_Descending_Order(self):
        """
                Check the descending order for the created date of playbook
                Validation-1: Validate Based on created Date.
                TC_ID: PlaybookTag-TC-008
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Checking Descending of created data")
        assert tag.get_created_time1() > tag.get_created_time2()

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_09_Apply_Last_Week_Filter(self):
        """
            Verify the filters for last week
            Validation -1: Validate based on the Status of the radio button
            TC_ID : PlaybookTag-TC-009
        """
        log = self.getlogger()
        filterandsort = FilterandSort(self.driver)
        log.info("Clicking on the filter Button")
        filterandsort.click_on_filter_btn()
        log.info("Click on the last week Filter")
        filterandsort.select_last_week_filter()
        assert filterandsort.check_last_week_radio_status() is True

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_10_Apply_Last_Month_Filter(self):
        """
        Check the Filter for the Last Month
        Validation-1: Validate based on the radio button
        TC_ID: PlaybookTag-TC-010
        """
        log = self.getlogger()
        filterandsort = FilterandSort(self.driver)
        log.info("Clicking on the last month filter Button")
        filterandsort.select_last_month_filter()
        assert filterandsort.check_last_month_radio_status() is True

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_11_Apply_custom_date_filter_using_calendar(self):
        """
        Check the Filter for the Last 3 days
        Validation-1: Validate based on the radio button
        TC_ID: PlaybookTag-TC-011
        """
        log = self.getlogger()
        filterandsort = FilterandSort(self.driver)
        dashboard = Dashboard(self.driver)
        tag = PlaybookTags(self.driver)
        log.info("Click on the start date button")
        dashboard.click_start_date_btn()
        log.info("Select start date from calendar")
        dashboard.select_calendar_start_date()
        #Start date and end date will be same because we are applying current date filter
        log.info("Select end date from calendar")
        dashboard.select_calendar_start_date()
        log.info("Click on the start date button to check whether date is selected or not")
        dashboard.click_start_date_btn()
        start_date_color = dashboard.get_calendar_start_date_color()
        assert start_date_color == '#1a3ee8'
        log.info("Clear the Applied filters in the Playbook Tags")
        tag.click_clear_all_filters_btn()
        log.info("Close the Filter Slider")
        filterandsort.click_close_filter_btn()

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_12_Visibility_of_Playbook_tag_in_Playbooks(self):
        """
            Verify the Visibility of the created Playbook Tag in the Playbooks Module Listing
            Validation -1: Validation Based on the Visibility of the Tag in Listing division
            TC_ID : 012
        """
        log = self.getlogger()
        nav = Navigation(self.driver)
        playbook = Playbooks(self.driver)
        tag = PlaybookTags(self.driver)
        log.info("Click on the main menu button")
        nav.click_main_menu()
        log.info("Navigate to the Manage Playbook Module")
        nav.navigate_manage_playbook()
        log.info("Visibility of first playbook")
        playbook.Pass_even_first_custom_playbook_is_not_visible()
        log.info("Click on create a New Playbook Button")
        playbook.click_on_create_playbook_btn()
        log.info("Click on the Overview Button")
        playbook.click_on_playbook_overview_btn()
        log.info("Click on the Playbook Tag Field")
        tag.click_on_tag_field()
        log.info("Enter the playbook tag name to verify it is present/ visible in listing")
        visibility = tag.visibility_of_playbook_tag(updated_playbooktag_title)
        log.info("click on the back button")
        playbook.click_on_back_button()
        log.info("Click exit without save button")
        playbook.click_playbook_exit_without_save()
        assert visibility is True

    @pytest.mark.regression
    @pytest.mark.playbooktag
    def test_13_Delete_Playbook_Tag(self):
        """
            Verify the Deletion Functionality of the PlaybookTag
            Validation -1: Based on the count of the Playbook Tag
            TC_ID : 013
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        admin = Admin(self.driver)
        tooltip = Tooltip(self.driver)
        nav = Navigation(self.driver)
        log.info("Click on the Admin Button")
        nav.click_admin_menu()
        log.info("Navigate to the Playbook Tag Module")
        admin.click_playbook_tags()
        log.info("Click on the Searchbar")
        tag.click_on_searchbar()
        log.info("Search functionality ")
        tag.put_string_in_searchbar(updated_playbooktag_title)
        log.info("Get the Count of Playbook Tags before delete the Tag")
        log.info("Mouse HOver on the first element on Listing")
        tag.mouse_hover_on_first_element()
        log.info("Move Hover on the More options")
        tag.mouse_hover_on_more_options()
        log.info("Click on the delete Button displayed on the Dropdown")
        tag.delete_playbooktag()
        log.info("Confirm the deletion of the Playbook Tag")
        tag.click_confirm_delete()
        toast_msg = tooltip.read_tooltip_msg()
        assert 'Success' == toast_msg
        log.info("click on close tool tip")
        tooltip.click_close_tooltip()



