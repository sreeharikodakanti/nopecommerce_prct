from selenium import webdriver

username_id = ""
logout_button_linktext = ""
class Login:
    def __init__(self,driver):
        self.driver = driver

    def setupusername(self,username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)
    def setuppassword(self,Password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(Password)
    def login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
    def logout_button(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()