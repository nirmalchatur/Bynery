from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def verify_inventory_page(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def verify_title(self):
        expect(self.page.locator(".title")).to_have_text("Products")

    def get_product_count(self):
        return self.page.locator(".inventory_item").count()