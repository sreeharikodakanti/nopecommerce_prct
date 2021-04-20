import pytest
from selenium import webdriver
from Objectspages.Login_page import Login
from Utilities.Readproperties import readconfigs
from Utilities import xlutiles
import time
class DDT_Login:
    Base_url = readconfigs.geturl()
    file = ".//Test_data/Login_data.xlsx"

    def Test_DDT_login(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.lp = Login(self.driver)
        self.rows = xlutiles.getrowcount(self.file, "Sheet")
        for r in range(2, self.rows+1):
            self.user = xlutiles.readdata(self.file, 'Sheet', r, 1)
            self.password = xlutiles.readdata(self.file, 'Sheet', r, 2)
            self.expect = xlutiles.readdata(self.file, 'Sheet', r, 3)
            self.lp.setupusername(self.user)
            self.lp.setuppassword(self.password)
            self.lp.login_button()
            time.sleep(5)
            act_title1 = self.driver.title




            if


