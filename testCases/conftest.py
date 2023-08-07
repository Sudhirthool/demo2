import pytest
from selenium import webdriver

# add arg --browser this for your command liner

def pytest_addoption(parser):
    parser.addoption("--browser")

# passing the value to --browser

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# here we are passing actual value to --browser

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("------Launching Chrome Browser------")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("------Launching Firefox Browser------")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("------Launching Edge Browser------")

    else:
        print("headlessmode")
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)

    driver.maximize_window()
    driver.get("https://automation.credence.in/shop")
    return driver


# use parameter when you have small data set

@pytest.fixture(params=[
                        ("Credencetest@test.com", "Credence@123"),
                        ("Credencetest@test.com1", "Credence@123"),
                        ("Credencetest@test.com", "Credence@1231"),
                        ("Credencetest@test.com1", "Credence@1231")
])
def getDataForLogin(request):
    return request.param

