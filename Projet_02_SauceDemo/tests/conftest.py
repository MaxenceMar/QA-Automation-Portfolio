import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()
    
    # Mode invité : Chrome ne se connecte à aucun compte et ignore les préférences de sécurité
    chrome_options.add_argument("--guest")
    
    # Désactive l'alerte de mot de passe compromis
    chrome_options.add_argument("--disable-features=SafeBrowsingPasswordCheck")
    
    # Autres options pour stabiliser le robot
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-infobars")

    # On force la désactivation via les préférences internes
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "safebrowsing.enabled": False # Désactive la vérification de sécurité
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10) # Optionnel : ouvre en plein écran pour mieux voir
    
    yield driver
    driver.quit()