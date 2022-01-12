from selenium.webdriver.common.by import By


class HomePage:
    emailId = (By.XPATH, "//input[@aria-placeholder='Enter your e-mail address']")
    passWord = (By.XPATH, "//input[@aria-placeholder='Enter your password']")
    loginButton = (By.XPATH, "//button[contains(text(),'Login')]")

    def __init__(self, driver):
        self.driver = driver

    def putEmailId(self):
        return self.driver.find_element(*HomePage.emailId)

    def putPassword(self):
        return self.driver.find_element(*HomePage.passWord)

    def clickLoginButton(self):
        return self.driver.find_element(*HomePage.loginButton)


"""
    def login(self, emailID, password):
        action = Action(self)
        action.sendKeys(self.putEmailId(), emailID)
        action.sendKeys(self.putPassword(), password)
        action.click(self.clickLoginButton())
"""
