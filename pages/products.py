from playwright.sync_api import Page


class Product:
    def __init__(self, page: Page):
        self.page = page

        self.product_cards = page.locator(".product-image-wrapper")

        self.product_name = page.get_by_text("Blue Top")
        self.product_category = page.get_by_text("Category: Women > Tops")
        self.product_price = page.get_by_text("Rs. 500")
        self.product_availability = page.get_by_text("In Stock")
        self.product_condition = page.get_by_text("New")
        self.product_brand = page.get_by_text("Polo").first


    def click_product_button(self):
        self.product_cards.first.get_by_role("link", name="View Product").click()


# TODO: Product test case make it dynamic instead of hard coded data
