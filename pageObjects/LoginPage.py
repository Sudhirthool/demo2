import time

from selenium.webdriver.common.by import By

class Login_Page:
    Text_Email_XPath = (By.XPATH, "//input[@id='email']")
    Text_Password_CSS = (By.CSS_SELECTOR, "#password")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    login_status = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self, driver):
        self.driver = driver

    def Login_URL(self):
        self.driver.get("https://automation.credence.in/login")

    def Enter_Email(self, email):
        self.driver.find_element(*Login_Page.Text_Email_XPath).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login_Page.Text_Password_CSS).send_keys(password)

    def CLick_Logic_Button(self):
        self.driver.find_element(*Login_Page.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        try:
            self.driver.find_element(*Login_Page.login_status)
            return True
        except:
            return False

