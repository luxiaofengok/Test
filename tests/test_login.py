from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

class Test_Login:

    def test_login(self, driver):
        login_page = LoginPage(driver)
        sleep(5)
        username = ConfigReader.get_username()
        password = ConfigReader.get_password()
        login_page.do_login(username, password)
        sleep(5)
        assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed, URL did not match expected inventory page URL."

    # def test_login_failed(self, driver):
    #     login_page = LoginPage(driver)
    #     login_page.do_login("invalid_user", "invalid_pass")
    #     sleep(5)
    #     error_message = login_page.get_error_message()
    #     assert error_message == "Epic sadface: Username and password do not match any user in this service", f"Unexpected error message: {error_message}"
    
       