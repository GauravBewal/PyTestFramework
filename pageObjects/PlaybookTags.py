import time

from selenium.webdriver.common.by import By
from utilities.Actions import Action
from configuration.readConfiguration import ReadConfig


class PlaybookTags(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    search_bar = "//input[@placeholder='Search Tag(s)']"

    def click_on_searc_bar(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.search_bar)

    def put_string_in_searchbar(self, value):
        return Action.send_keys(self, By.XPATH, PlaybookTags.search_bar, value)

    click_close_button = "//i[contains(@class,'search-input__close')]/parent::span"

    def click_on_close_button(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.click_close_button)

    top_first_tag = "(//span[contains(@class,'csol-tag__title')])[1]"

    def get_top_first_search_result(self, value):
        return Action.read_search_result(self, By.XPATH, PlaybookTags.top_first_tag, value)

    def get_top_first_tag(self):
        return Action.get_text(self, By.XPATH, PlaybookTags.top_first_tag)

    def click_top_first_tag(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.top_first_tag)

    create_new_playbookTag = "//header//button"

    def click_new_playbookTag(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.create_new_playbookTag)

    playbooktag_title = "//input[@placeholder='Enter Tag Name']"

    def put_playbooktag_title(self, value):
        return Action.send_keys(self, By.XPATH, PlaybookTags.playbooktag_title, value)

    def clear_tag_name_field(self):
        return Action.clear_field(self, By.XPATH, PlaybookTags.playbooktag_title)


    playbooktag_description = "//input[@placeholder='Enter Description']"

    def put_playbooktag_description(self, value):
        return Action.send_keys(self, By.XPATH, PlaybookTags.playbooktag_description, value)

    def clear_playbooktag_description(self):
        return Action.clear_field(self, By.XPATH, PlaybookTags.playbooktag_description)


    text_playbookTag_count = "//h1[contains(text(),'Playbook Tags (')]"

    def get_playbookTag_count(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_count_from_string(self, By.XPATH, PlaybookTags.text_playbookTag_count)

    button_save = "//div[@class='text-right']/button[contains(text(),'Save')]"

    def save_playbookTag(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.button_save)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tool_tip(self):
        return Action.javascript_click(self, By.XPATH, PlaybookTags.tooltip_close)

    edit_button = "//div[contains(@class,'header__icons')]/i[contains(@class,'cyicon-edit')]"

    def click_on_Edit_Button(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.edit_button)
