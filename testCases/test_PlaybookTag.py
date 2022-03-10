import time

import pytest

from pageObjects.PlaybookTags import PlaybookTags
from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybookTags(Base):
    global playbook_tag_name
    playbook_tag_name = ''


    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_PlaybookTag_redirection(self):
        """
            Verify PlaybookTag Page redirection from Main Menu
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
        assert action.get_title() == 'Playbook Tags | Cyware Orchestrate'

    # @pytest.mark.regression
    # @pytest.mark.readOnly
    # def test_02_Sort_by_created(self):
    #     """
    #     Verify whether user is able to apply sort based on the created
    #     Validation-1: Based on the
    #     """
    #     log = self.getlogger()
    #     tag = TestPlaybookTags(self.driver)
    #     log.info("Store the list of all the ")


    @pytest.mark.regression
    def test_02_Create_New_Playbook_Tag(self):
        """
        Verify PlaybookTag Create functionality
        TC_ID: PlaybookTag-TC-002
        """
        log = self.getlogger()
        action = Action(self.driver)
        tag = PlaybookTags(self.driver)
        log.info("Reading the count of total playbookTags before creating a new playbookTag")
        before_playbookTag_creation_count = tag.get_playbookTag_count()
        log.info("Click on to create new PlaybookTag")
        tag.click_new_playbookTag()
        global playbook_tag_name
        playbook_tag_name = "PlaybookTag_" + action.get_current_time()
        log.info("Entering new PlaybookTag name")
        tag.put_playbooktag_title(playbook_tag_name)
        log.info("Entering PlaybookTag description")
        tag.put_playbooktag_description("Test Description")
        log.info("Click on Save PlaybookTag button")
        tag.save_playbookTag()
        log.info("close tool tip")
        tag.close_tool_tip()
        log.info("Reading count of total labels after creating a new playbookTag")
        after_playbookTag_creation_count = tag.get_playbookTag_count()
        log.info("Validating total count of PlaybookTag before and after creation of new label, also checking the "
                 "newly created PlaybookTag is listing or not")
        assert before_playbookTag_creation_count + 1 == after_playbookTag_creation_count


    @pytest.mark.regression
    def test_03_Search_Playbook_Tag(self):
        """
        Verify User is able to search Created PLaybookTag
        TC_ID: PlaybookTag-TC-003
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Searching the Playbook Tag")
        tag.put_string_in_searchbar(playbook_tag_name)
        search_result = tag.get_top_first_search_result(playbook_tag_name)
        tag.click_on_close_button()
        assert search_result == playbook_tag_name

    @pytest.mark.regression
    def test_04_Update_PlaybookTag(self):
        """
        Update the PlaybookTag
        TC_ID: PlaybookTag-TC-004
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        action = Action(self.driver)
        log.info("Updating the PlaybookTag")
        tag.click_top_first_tag()
        log.info("Clicking on Editing Button in Slider")
        tag.click_on_Edit_Button()
        log.info("Remove the existing data from tag name field")
        tag.clear_tag_name_field()
        log.info("Adding New playbookTag Title")
        updated_tag_name = "PlaybookTag_"+action.get_current_time()
        log.info("Updating the PlaybookTag Title")
        tag.put_playbooktag_title(updated_tag_name)
        log.info("Remove the existing data from tag description field")
        tag.clear_playbooktag_description()
        tag.put_playbooktag_description("Updated Description")
        log.info("Click on Save/update PlaybookTag button")
        tag.save_playbookTag()
        log.info("close tool tip")
        tag.close_tool_tip()
        tag.put_string_in_searchbar(updated_tag_name)
        search_result = tag.get_top_first_search_result(updated_tag_name)
        assert search_result == updated_tag_name








