import pytest

from pageObjects.PlaybookTags import PlaybookTags
from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base
from pageObjects.FilterandSort import FilterAndSort


@pytest.mark.usefixtures("setup")
class TestPlaybookTags(Base):
    global playbook_tag_text
    playbook_tag_text = ''

    @pytest.mark.regression
    @pytest.mark.readOnly
    def test_01_Playbook_Tag_redirection(self):
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
        global playbook_tag_text
        playbook_tag_text = "PlaybookTag_" + action.get_current_time()
        log.info("Entering new PlaybookTag name")
        tag.put_playbooktag_title(playbook_tag_text)
        log.info("Entering PlaybookTag description")
        tag.put_playbooktag_description("Test Description")
        log.info("Click on Save PlaybookTag button")
        tag.save_playbookTag()
        log.info("Reading count of total labels after creating a new playbookTag")
        after_playbookTag_creation_count = tag.get_playbookTag_count()
        log.info("Validating total count of PlaybookTag before and after creation of new label, also checking the "
                 "newly created PlaybookTag is listing or not")
        assert before_playbookTag_creation_count + 1 == after_playbookTag_creation_count

    @pytest.mark.regression
    def test_03_Check_Sort_Based_On_Created(self):
        """
                Verify User is able to sort based on Created Time of Playbook
                TC_ID: PlaybookTag-TC-003
                """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        filter_sort = FilterAndSort(self.driver)
        log.info("Mouse overing the sort Option")
        filter_sort.mouse_over_on_sort()
        log.info("Changing sort to the Created")
        filter_sort.click_on_created()
        log.info("Changing sort to Descending Order")
        filter_sort.changing_sort_to_descending_order()
        assert filter_sort.get_name_sorted_filter() == "Created"

    @pytest.mark.regression
    def test_04_Search_Playbook_Tag(self):
        """
        Verify User is able to search Created PLaybookTag
        TC_ID: PlaybookTag-TC-004
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Searching the Playbook Tag")
        tag.click_on_searchbar()
        tag.put_string_in_searchbar(playbook_tag_text)
        tag_name = tag.get_playbooktag_name()
        tag.click_on_close_button()
        assert tag_name == playbook_tag_text

    @pytest.mark.regression
    def test_05_Update_PlaybookTag(self):
        """
        Update the PlaybookTag
        TC_ID: PlaybookTag-TC-005
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        action = Action(self.driver)
        log.info("Updating the PlaybookTag")
        tag.click_playbooktag_name()
        log.info("Clicking on Editing Button in Slider")
        tag.click_on_Edit_Button()
        tag.clear_playbooktag_title()
        new_playbooktag_title = "PlaybookTag_" + action.get_current_time()
        log.info("Adding New playbookTag Title")
        tag.put_playbooktag_title(new_playbooktag_title)
        log.info("Updating the PlaybookTag Title")
        tag.clear_playbooktag_description()
        tag.put_playbooktag_description("Updated Description")
        log.info("Click on Save/update PlaybookTag button")
        tag.save_playbookTag()
        updated_playbook_title = tag.get_playbooktag_name()
        assert updated_playbook_title == new_playbooktag_title

    @pytest.mark.regression
    def test_06_Check_Descending_Order(self):
        """
                Check the descending order for the created date of playbook
                TC_ID: PlaybookTag-TC-006
                """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        log.info("Checking Descending of created data")
        assert tag.get_created_time1() > tag.get_created_time2()
