from selenium.webdriver.common.by import By


class FilterandSort:
    button_filter = (By.XPATH, "//div[@class='header__top--left d-flex flex-fill']/button")
    button_sort = (By.XPATH, "//span[@class='sort-tab']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnFilters(self):
        return self.driver.find_element(*FilterandSort.button_filter)

    def clickOnSort(self):
        return self.driver.find_element(*FilterandSort.button_sort)
