from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class Test_Checkout:
    def test_checkout(self, login_done):
        driver = login_done
        inventory_page = InventoryPage(driver)
        sleep(2)
        inventory_page.add_item_to_cart(3)
        sleep(2)
        inventory_page.click_cart_icon()    
        sleep(5)
        cart_page = CartPage(driver)
        cart_items = cart_page.get_cart_items()
        assert len(cart_items) == 3, f"Expected 3 items in the cart, but found {len(cart_items)}."
        cart_page.remove_item_from_cart(cart_items[1].text, index=1)
        sleep(2)
        cart_page.click_checkout_button()
        sleep(2)
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_information("John", "Doe", "70000")
        sleep(2)
        assert checkout_page.is_checkout_complete(), "Checkout process did not complete successfully."
        
        
        
        
        

    
        