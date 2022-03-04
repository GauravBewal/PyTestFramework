import pytest

from pageObjects.PlaybookTags import PlaybookTags
from pageObjects.AdminPage import Admin
from pageObjects.Navigation import Navigation
from utilities.Actions import Action
from utilities.Base import Base


@pytest.mark.usefixtures("setup")
class TestPlaybookTags(Base):
    global playbook_tag_text
    playbook_tag_text=''


    @pytest.mark.smoke
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


    @pytest.mark.smoke
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


    @pytest.mark.smoke
    def test_03_Search_Playbook_Tag(self):
        """
        Verify User is able to search Created PLaybookTag
        TC_ID: PlaybookTag-TC-003
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        tag_name = tag.get_playbooktag_name()
        log.info("Searching the Playbook Tag")
        tag.click_on_searchbar()
        tag.put_string_in_searchbar(playbook_tag_text)
        tag.click_on_close_button()
        assert tag_name == playbook_tag_text



    @pytest.mark.smoke
    def test_04_Update_PlaybookTag(self):
        """
        Update the PlaybookTag
        TC_ID: PlaybookTag-TC-004
        """
        log = self.getlogger()
        tag = PlaybookTags(self.driver)
        action = Action(self.driver)
        log.info("Updating the PlaybookTag")
        tag.click_playbooktag_name()
        log.info("Clicking on Editing Button in Slider")
        tag.click_on_Edit_Button()
        tag.clear_playbooktag_title()
        new_playbooktag_title="PlaybookTag_"+action.get_current_time()
        log.info("Adding New playbookTag Title")
        tag.put_playbooktag_title(new_playbooktag_title)
        log.info("Updating the PlaybookTag Title")
        tag.clear_playbooktag_description()
        tag.put_playbooktag_description("Updated Description")
        log.info("Click on Save/update PlaybookTag button")
        tag.save_playbookTag()
        updated_playbook_title=tag.get_playbooktag_name()
        assert updated_playbook_title == new_playbooktag_title








