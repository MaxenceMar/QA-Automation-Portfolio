from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator pour le bouton du sac à dos
        self.add_backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        # Locator pour l'icône du panier (en haut à droite)
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_btn).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()