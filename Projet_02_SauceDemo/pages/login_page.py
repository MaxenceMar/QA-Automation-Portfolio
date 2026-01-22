from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # On centralise les adresses (Locators) ici
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
    
    def login(self, user, pwd):
        # On définit l'action "Se connecter"
        self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()