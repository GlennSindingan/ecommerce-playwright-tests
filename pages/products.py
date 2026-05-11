from playwright.sync_api import Page


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.product_cards = page.locator(".product-image-wrapper")

    def click_product_button(self):
        self.product_cards.first.get_by_role("link", name="View Product").click()


# TODO: create Test Case 9: Search Product
