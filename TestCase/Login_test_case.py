from Objectspages.Login_page import Login
from Utilities.Readproperties import readconfigs

class Test_Login_home_page:
    Base_url = readconfigs.geturl()
    username = readconfigs.getusername()
    password = readconfigs.getpassword()
    def Test_home_page(self,setup):
        self.driver = setup
        self.driver.get(self.Base_url)
        self.act_title = self.driver.title
        if self.act_title =="Your store. Login":
            assert True
        else:
            assert False
        self.driver.close()
    def Test_Login_page(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.setupusername(self.username)
        self.lp.setuppassword(self.password)
        self.lp.login_button()
        self.act_title_1 = self.driver.title
        if self.act_title_1 == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\"+"test_home.png")
        self.driver.close()

