from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):

        self.page = page

    def open(self, url):

        self.page.goto(url)

    def login(self, username, password):

        self.page.fill("#user-name", username)

        self.page.fill("#password", password)

        self.page.click("#login-button")

    def verify_login(self):

        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")