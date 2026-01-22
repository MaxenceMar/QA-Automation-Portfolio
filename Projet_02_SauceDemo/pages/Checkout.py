from selenium.webdriver.common.by import By
import time

class Checkout:
    def __init__(self, driver):
        self.driver = driver

        # Locator pour le bouton Checkout
        self.checkout_button = (By.ID, "checkout")

        #Locator pour Informations First Name
        self.first_name = (By.ID, "first-name")

        #Locator pour Informations Last Name
        self.last_name = (By.ID, "last-name")

        #Locator pour Informations ZIP/Postal Code
        self.postal_code = (By.ID, "postal-code")

        #Locator pour Continue
        self.continu = (By.ID, "continue")

        #Locator pour Finish
        self.finish = (By.ID, "finish")

        #Locator pour backhome
        self.back_home = (By.ID, "back-to-products")


    def checkout_personnale_informations(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continu).click()
    
    def finish_order(self):
        # Cette méthode sera appelée après le chargement de la page récapitulative
        self.driver.find_element(*self.finish).click()
        self.driver.find_element(*self.back_home).click()
