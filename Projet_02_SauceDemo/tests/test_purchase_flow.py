from pages.login_page import LoginPage
from pages.ProductsPage import ProductsPage
from pages.Checkout import Checkout

def test_achat_sac_a_dos(browser):
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = Checkout(browser)
    
    # 1. Connexion
    browser.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # 2. Ajout au panier
    products_page.add_backpack_to_cart()

    # 3. Aller au panier 
    products_page.go_to_cart()

    # 4. Continuer au checkout
    checkout_page.checkout_personnale_informations("Max","Ben","zsc")

    checkout_page.finish_order()