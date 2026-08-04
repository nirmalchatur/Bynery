from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import BASE_URL, APP_USERNAME, APP_PASSWORD


def test_login(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open(BASE_URL)
    login.login(APP_USERNAME, APP_PASSWORD)

    dashboard.verify_inventory_page()
    dashboard.verify_title()

    assert dashboard.get_product_count() > 0