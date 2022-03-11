from selenium.webdriver.common.by import By

from utilities.Actions import Action


class FilterAndSort(Action):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    button_filter = "//i[@class='icon icon-filter']/parent::button"

    def click_on_filters(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.button_filter)

    button_sort = "//span[@class='sort-tab']"

    def click_on_sort(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.button_filter)

    sort_position = "//span[@class='sort-type el-dropdown-selfdefine']"

    def mouse_hover_on_sort(self):
        return Action.mouse_hover_on_element(self, By.XPATH, FilterAndSort.sort_position)

    def get_name_sorted_filter(self):
        return Action.get_text(self, By.XPATH, FilterAndSort.sort_position)

    created_sort = "(//ul[@class='el-dropdown-menu el-popper filters-sort-dropdown']" \
                   "//li[@class='el-dropdown-menu__item'])[2]"

    def click_on_created(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.created_sort)

    sort_order = "//span[@class='sort-tab']//span[@class='el-tooltip sort-button']"

    def changing_sort_to_descending_order(self):
        return Action.javascript_click(self, By.XPATH, FilterAndSort.sort_order)

    filter_close_btn = "//i[contains(@class,'cyicon-cross')]/parent::span"

    def close_filter_btn(self):
        return Action.wait_and_click(self, By.XPATH, FilterAndSort.filter_close_btn)

    playbook_filter_title = "//span[@class='filters__header__label']"

    def get_filters_slider_title(self):
        return Action.get_text(self, By.XPATH, FilterAndSort.playbook_filter_title)
