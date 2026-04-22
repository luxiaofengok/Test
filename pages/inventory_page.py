from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from random import sample

class InventoryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.cart_icon = (By.ID, "shopping_cart_container")

    def get_inventory_items(self):
        return self.find_elements(self.inventory_items)
    
    def click_cart_icon(self):
        self.find_element(self.cart_icon).click()
 
    
    def add_item_to_cart(self, n):
        item_locator = (By.XPATH, "//div[@class='inventory_item']//button")
        add_buttons = self.driver.find_elements(*item_locator)
        for i in sample(range(len(add_buttons)), n):
            add_buttons[i].click()


