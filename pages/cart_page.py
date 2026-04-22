from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.remove_buttons = (By.XPATH, "//button[text()='Remove']")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def click_checkout_button(self):  
        return self.find_element(self.checkout_button).click()

    def click_continue_shopping(self):
        return self.find_element(self.continue_shopping_button).click()

    def remove_item_from_cart(self, item_name, index=None):
        cart_items = self.get_cart_items()
        for item in cart_items:
            if item.text == item_name:
                remove_button = item.find_elements(*self.remove_buttons)
                if index is not None:
                    remove_button[index].click()
                else:
                    remove_button[0].click()
                break
