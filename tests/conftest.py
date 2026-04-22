from selenium import webdriver
import pytest
from time import sleep
from utils.config_reader import ConfigReader


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"profile.password_manager_leak_detection": False})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(ConfigReader.get_timeout()["implicit_wait"])
    driver.maximize_window()
    url = ConfigReader.get_base_url()
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def login_done(driver):
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    username = ConfigReader.get_username()
    password = ConfigReader.get_password()
    login_page.do_login(username, password)
    return driver
