from pages.login_page import LoginPage
from playwright.sync_api import expect
from config.config import BASE_URL

def test_invalid_login(page):
    login = LoginPage(page)

    login.open(BASE_URL)

    login.login("invalid_user", "wrong_password")

    expect(page.locator("[data-test='error']")).to_be_visible()