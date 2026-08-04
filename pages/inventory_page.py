from playwright.sync_api import expect

class InventoryPage:

    def __init__(self, page):
        self.page = page

    def add_first_product(self):
        self.page.locator(".inventory_item button").first.click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def verify_cart_badge(self):
        expect(self.page.locator(".shopping_cart_badge")).to_have_text("1")
        