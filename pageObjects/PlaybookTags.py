import time

from selenium.webdriver.common.by import By

from configuration.readConfiguration import ReadConfig
from utilities.Actions import Action


class PlaybookTags(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    close_walkthrough_tooltip = "//a[@class='introjs-skipbutton']"

    def click_on_close_walkthrough(self):
        return Action.click_if_element_found(self, By.XPATH, PlaybookTags.close_walkthrough_tooltip)

    click_search_bar = "//input[@placeholder='Search Tag(s)']"

    def click_on_searchbar(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.click_search_bar)

    click_close_button = "//i[@class='cursor-pointer el-input__icon icon icon-cross-o-active search-input__close']"

    def click_on_close_button(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.click_close_button)

    def put_string_in_searchbar(self, value):
        return Action.send_keys(self, By.XPATH, PlaybookTags.click_search_bar, value)

    create_new_playbookTag = "//header//button"

    def click_new_playbookTag(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.create_new_playbookTag)

    playbooktag_title = "//input[@placeholder='Enter Tag Name']"

    def put_playbooktag_title(self, value):
        return Action.send_keys(self, By.XPATH, PlaybookTags.playbooktag_title, value)

    def clear_playbooktag_title(self):
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

    button_save = "//div[@class='text-right']//button[contains(text(),'Save')]"

    def save_playbookTag(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.button_save)

    playbooktag_name = "(//tbody/tr[1]/td[1]//span)[1]"

    def get_playbooktag_name(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        return Action.get_text(self, By.XPATH, PlaybookTags.playbooktag_name)

    def get_first_tagname(self):
        time.sleep(ReadConfig.Wait_3_Sec())
        text = Action.get_text(self, By.XPATH, PlaybookTags.playbooktag_name)
        return Action.convert_string_to_lower(self, text)

    def click_playbooktag_name(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.playbooktag_name)

    edit_button = "//i[@class='el-tooltip cyicon-edit cursor-pointer']"

    def click_on_Edit_Button(self):
        return Action.wait_and_click(self, By.XPATH, PlaybookTags.edit_button)

    created_time1 = "(//tbody/tr[1]/td[4]//span)[1]"

    def get_created_time1(self):
        time1 = Action.get_text(self, By.XPATH, PlaybookTags.created_time1)
        return Action.convert_12to24hrs_time_format(self, time1)

    created_time2 = "(//tbody/tr[2]/td[4]//span)[1]"

    def get_created_time2(self):
        time2 = Action.get_text(self, By.XPATH, PlaybookTags.created_time2)
        return Action.convert_12to24hrs_time_format(self, time2)

    second_tag_name = "(//tbody/tr[2]/td[1]//span)[1]"

    def get_second_playbookTag(self):
        second_playbooktag = Action.get_text(self, By.XPATH, PlaybookTags.second_tag_name)
        return Action.convert_string_to_lower(self, second_playbooktag)

    slider_name = "//div[contains(@class,'cy-right-modal-header__label')]//div//div"

    def get_slider_name(self):
        return Action.get_text(self, By.XPATH, PlaybookTags.slider_name)

    slider_close = "(//div[@class='cy-right-modal-header__icons']//span[@class='cyicon-cross'])[2]"

    def close_slider_btn(self):
        return Action.javascript_click(self, By.XPATH, PlaybookTags.slider_close)

    tooltip_close = "//div[contains(@class,'notification__closeBtn')]"

    def close_tooltip(self):
        return Action.normal_click(self, By.XPATH, PlaybookTags.tooltip_close)
