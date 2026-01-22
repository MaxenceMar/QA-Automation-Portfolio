from pages.login_page import LoginPage

def test_login_invalide(browser):
    login_page = LoginPage(browser)
    browser.get("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "MauvaisMdp") # On teste l'erreur ici
    assert "invalid" in login_page.get_message()

def test_login_valide(browser):
    login_page = LoginPage(browser)
    browser.get("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_message()