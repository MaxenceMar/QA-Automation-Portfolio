import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # SETUP : On lance le navigateur
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver # C'est ici que tes tests vont "emprunter" le navigateur
    # TEARDOWN : On ferme après le test
    driver.quit()