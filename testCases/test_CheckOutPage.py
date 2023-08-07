# import time
import time

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.LoginPage import Login_Page


class Test_Checkout_Page:
    def test_checkout_page(self, setup):
        self.driver = setup
        self.COP = CheckOutPage(self.driver)
        self.lp = Login_Page(self.driver)
        self.driver.implicitly_wait(20)
        # 1 get Url
        self.lp.Login_URL()

        # 2 Enter Email
        self.lp.Enter_Email("Credencetest@test.com")

        # Enter Password
        self.lp.Enter_Password("Credence@123")

        # Press Login Button
        self.lp.CLick_Logic_Button()

        # Click On Headphone
        self.COP.Click_Headphone()

        # Click on ADD to Cart
        self.COP.Add_to_Cart()

        # Click on Continue to Shopping
        self.COP.Continue_Shopping()

        # Click on Mackbook
        self.COP.Click_Mackbook()

        # Click on ADD to Cart
        self.COP.Add_to_Cart()

        #  Click on Continue to Shopping
        self.COP.Continue_Shopping()

        # Click on Ipad
        self.COP.Click_Ipad()

        # Click on ADD to Cart
        self.COP.Add_to_Cart()

        # Select Headphone Quantity
        self.COP.Select_Headphone_quantity(3)

        # Select MackBook Quantity
        self.COP.Select_Mackbook_quantity(3)

        # Select Ipad Quantity
        self.COP.Select_Ipad_quantity(3)
        time.sleep(5)

        #  Click on Proceed to Checkout
        self.COP.Proceed_to_Checkout()

        self.driver.implicitly_wait(10)
        # Enter First_Name
        self.COP.Enter_Fname("Rohit")

        # Enter Last_Name
        self.COP.Enter_Lname("Verma")

        # Enter Phone
        self.COP.Enter_Phone("8767675645")

        # Enter Address
        self.COP.Enter_Address("Palkawadi Pune")

        # Enter Zip
        self.COP.Enter_Zip("443001")

        # Select State
        self.COP.Select_State(2)

        # Enter Owner
        self.COP.Enter_Owner_Name("Rohit Verma")

        # Enter CVV
        self.COP.Enter_CVV("043")

        # Enter Card Number
        self.COP.Enter_Card_NO("5281")
        self.COP.Enter_Card_NO("0370")
        self.COP.Enter_Card_NO("4891")
        self.COP.Enter_Card_NO("6168")

        # Select Expiry year
        self.COP.Select_Card_Exp_Year(2)

        # Select Expiry Month
        self.COP.Select_Card_Exp_Month(3)
        self.driver.implicitly_wait(10)
        # Click Continue to checkout
        self.COP.Click_Continue_to_checkout()

        # Check Out Status
        self.COP.Check_Order_Status()

        self.driver.quit()
