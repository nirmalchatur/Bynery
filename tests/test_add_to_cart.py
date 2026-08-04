from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, APP_USERNAME, APP_PASSWORD

def test_add_product(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.open(BASE_URL)
    login.login(APP_USERNAME, APP_PASSWORD)

    inventory.add_first_product()
    inventory.verify_cart_badge()