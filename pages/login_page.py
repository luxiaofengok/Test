from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import pytest
from utils.config_reader import ConfigReader
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "user-name")
        self.password = (By.NAME, "password")
        self.lgn_btn = (By.ID, "login-button")

    def enter_username(self, username):
        self.find_element(self.username).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.password).send_keys(password)

    def click_login_button(self):
        self.find_element(self.lgn_btn).click()

    def get_error_message(self):
        error_message_locator = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        return self.find_element(error_message_locator).text

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
