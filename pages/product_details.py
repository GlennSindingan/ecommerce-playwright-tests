from playwright.sync_api import Page


class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page

        self.info_box = page.locator(".product-information")


        self.product_name = self.info_box.locator("h2")

        self.product_category = self.info_box.locator("p").filter(has_text="Category:")
        self.product_price = self.info_box.locator("span > span").filter(has_text="Rs.")
        self.product_availability = self.info_box.locator("p").filter(has_text="Availability:")
        self.product_condition = self.info_box.locator("p").filter(has_text="Condition:")
        self.product_brand = self.info_box.locator("p").filter(has_text="Brand:")