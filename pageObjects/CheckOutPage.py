from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# from testCases.conftest import setup


class CheckOutPage:
    """ATTRIBUTES"""
    Apple_Mack_Book_pro_XPATH = (By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[1]/img")
    Apple_iPad_Retina_XPATh = (By.XPATH, "//h3[normalize-space()='Apple iPad Retina']")
    Headphones_XPATH = (By.XPATH, "//img[@src='https://automation.credence.in/img/headphones.jpg']")
    Add_To_Cart_CSS = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    Select_Headphones_Quantity_XPATH = (By.XPATH, "/html/body/div/table/tbody/tr[1]/td[3]/select")
    Select_Apple_Mack_Book_pro_XPATH = (By.XPATH, "/html/body/div/table/tbody/tr[2]/td[3]/select")
    Select_Apple_iPad_Retina_XPATh = (By.XPATH, "/html/body/div/table/tbody/tr[3]/td[3]/select")
    Click_Continue_Shopping_CSS = (By.CSS_SELECTOR, ".btn.btn-primary.btn-lg")
    Click_Proceed_to_Checkout_XPATH = (By.LINK_TEXT, "Proceed to Checkout")
    First_Name_XPATH = (By.NAME, "first_name")
    Last_Name_XPATH = (By.NAME, "last_name")
    Phone_XPATH = (By.NAME, "phone")
    Address_XPATH = (By.NAME, "address")
    ZIP_CODE_XPATH = (By.NAME, "zip")
    State_XPATH = (By.ID, "state")
    Owner_Name_XPATH = (By.NAME, "owner")
    CVV_XPATH = (By.NAME, "cvv")
    Card_Number_XAPATH = (By.NAME, "cardNumber")
    Card_Expiry_year_XPATH = (By.NAME, "exp_year")
    Card_Month_year_XPATH = (By.NAME, "exp_month")
    Continue_to_checkout_XPATH = (By.ID, "confirm-purchase")
    Order_Success_Msg_XPATH = (By.XPATH, "//p[@class='lead w-lg-50 mx-auto']")

    """BEHAVIOUR"""

    def __init__(self, driver):
        self.driver = driver

    def Click_Headphone(self):
        self.driver.find_element(*CheckOutPage.Headphones_XPATH).click()

    def Click_Mackbook(self):
        self.driver.find_element(*CheckOutPage.Apple_Mack_Book_pro_XPATH).click()

    def Click_Ipad(self):
        self.driver.find_element(*CheckOutPage.Apple_iPad_Retina_XPATh).click()

    def Add_to_Cart(self):
        self.driver.find_element(*CheckOutPage.Add_To_Cart_CSS).click()

    def Continue_Shopping(self):
        self.driver.find_element(*CheckOutPage.Click_Continue_Shopping_CSS).click()

    def Select_Headphone_quantity(self, r):
        Select(self.driver.find_element(*CheckOutPage.Select_Headphones_Quantity_XPATH)).select_by_index(r)

    def Select_Mackbook_quantity(self, k):
        Select(self.driver.find_element(*CheckOutPage.Select_Apple_Mack_Book_pro_XPATH)).select_by_index(k)

    def Select_Ipad_quantity(self, s):
        Select(self.driver.find_element(*CheckOutPage.Select_Apple_iPad_Retina_XPATh)).select_by_index(s)

    def Proceed_to_Checkout(self):
        self.driver.find_element(*CheckOutPage.Click_Proceed_to_Checkout_XPATH).click()

    def Enter_Fname(self, fname):
        self.driver.find_element(*CheckOutPage.First_Name_XPATH).send_keys(fname)

    def Enter_Lname(self, lname):
        self.driver.find_element(*CheckOutPage.Last_Name_XPATH).send_keys(lname)

    def Enter_Phone(self, phone):
        self.driver.find_element(*CheckOutPage.Phone_XPATH).send_keys(phone)

    def Enter_Address(self, address):
        self.driver.find_element(*CheckOutPage.Address_XPATH).send_keys(address)

    def Enter_Zip(self, zip):
        self.driver.find_element(*CheckOutPage.ZIP_CODE_XPATH).send_keys(zip)

    def Select_State(self, state):
        Select(self.driver.find_element(*CheckOutPage.State_XPATH)).select_by_index(state)

    def Enter_Owner_Name(self, owner):
        self.driver.find_element(*CheckOutPage.Owner_Name_XPATH).send_keys(owner)

    def Enter_CVV(self, cvv):
        self.driver.find_element(*CheckOutPage.CVV_XPATH).send_keys(cvv)

    def Enter_Card_NO(self, card_no):
        self.driver.find_element(*CheckOutPage.Card_Number_XAPATH).send_keys(card_no)

    def Select_Card_Exp_Year(self, a):
        Select(self.driver.find_element(*CheckOutPage.Card_Expiry_year_XPATH)).select_by_index(a)

    def Select_Card_Exp_Month(self, b):
        Select(self.driver.find_element(*CheckOutPage.Card_Month_year_XPATH)).select_by_index(b)

    def Click_Continue_to_checkout(self):
        self.driver.find_element(*CheckOutPage.Continue_to_checkout_XPATH).click()

    def Check_Order_Status(self):
        try:
            self.driver.find_element(*CheckOutPage.Order_Success_Msg_XPATH)
            print("Check Out testcase Successfully Passed ")
        except:
            print("Check Out testcase Failed")
