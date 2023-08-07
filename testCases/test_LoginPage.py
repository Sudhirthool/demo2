from pageObjects.LoginPage import Login_Page

class Test_CredKart_Login:

    def test_CredKart_Login_001(self, setup):
        self.driver = setup
        self.lp =Login_Page(self.driver)

        # 1 get Url
        self.lp.Login_URL()

        # 2 Enter Email
        self.lp.Enter_Email("Credencetest@test.com")

        # Enter Password
        self.lp.Enter_Password("Credence@123")

        # Press Login Button
        self.lp.CLick_Logic_Button()

        # Verify Login
        if self.lp.Login_Status() == True:
            assert True

        else:
            assert False

        self.driver.quit()




