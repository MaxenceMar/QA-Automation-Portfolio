from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # On centralise les adresses (Locators) ici
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.message_area = (By.ID, "flash")

    def login(self, user, pwd):
        # On définit l'action "Se connecter"
        self.driver.find_element(*self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        return self.driver.find_element(*self.message_area).text