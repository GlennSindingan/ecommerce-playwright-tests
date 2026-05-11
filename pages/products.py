from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.product_cards = page.locator(".product-image-wrapper")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")
        self.view_cart = page.get_by_text("View Cart")

    def click_product_button(self):
        self.product_cards.first.get_by_role("link", name="View Product").click()

    def add_product_to_cart(self, index: int):
        self.product_cards.nth(index).locator(".add-to-cart").first.click()

    def click_continue_shopping_button(self):
        self.continue_shopping.click()

    def click_view_cart(self):
        self.view_cart.click()