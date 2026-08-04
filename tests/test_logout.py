from pages.login_page import LoginPage
from config.config import BASE_URL, APP_USERNAME, APP_PASSWORD
from playwright.sync_api import expect


def test_logout(page):

    login = LoginPage(page)

    login.open(BASE_URL)

    login.login(APP_USERNAME, APP_PASSWORD)

    page.locator("#react-burger-menu-btn").click()

    page.locator("#logout_sidebar_link").click()

    expect(page.locator("#login-button")).to_be_visible()

    expect(page.locator("#user-name")).to_be_visible()