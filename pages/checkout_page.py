from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.confirmation_message = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        self.find_element(self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(self.last_name).send_keys(last_name)
    
    def enter_postal_code(self, postal_code):
        self.find_element(self.postal_code).send_keys(postal_code)

    def click_continue_button(self):
        self.find_element(self.continue_button).click()
    
    def click_finish_button(self):
        self.find_element(self.finish_button).click()
    
    def get_confirmation_message(self):
        return self.find_element(self.confirmation_message).text
    
    def is_checkout_complete(self):
        return self.get_confirmation_message() in ["Thank you for your order!", "Your order has been dispatched, and will arrive just as fast as the pony can get there!"]
    
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue_button()
        self.click_finish_button()