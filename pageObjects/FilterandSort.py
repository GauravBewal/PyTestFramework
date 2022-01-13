from selenium.webdriver.common.by import By


class FilterAndSort:

    def __init__(self, driver):
        self.driver = driver

    button_filter = (By.XPATH, "//div[@class='header__top--left d-flex flex-fill']/button")

    def clickOnFilters(self):
        return self.driver.find_element(*FilterAndSort.button_filter)

    button_sort = (By.XPATH, "//span[@class='sort-tab']")

    def clickOnSort(self):
        return self.driver.find_element(*FilterAndSort.button_sort)
