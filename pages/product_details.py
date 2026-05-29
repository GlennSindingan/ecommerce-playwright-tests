from playwright.sync_api import Page


class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page

        self.info_box = page.locator(".product-information")
        self.quantity_input = page.locator("#quantity")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")


        self.product_name = self.info_box.locator("h2")

        self.product_category = self.info_box.locator("p").filter(has_text="Category:")
        self.product_price = self.info_box.locator("span > span").filter(has_text="Rs.")
        self.product_availability = self.info_box.locator("p").filter(has_text="Availability:")
        self.product_condition = self.info_box.locator("p").filter(has_text="Condition:")
        self.product_brand = self.info_box.locator("p").filter(has_text="Brand:")

        self.review_name = page.locator("#name")
        self.review_email = page.locator("#email")
        self.review_message = page.locator("#review")
        self.review_button = page.locator("#button-review")

    def set_amount(self, amount: str):
        self.quantity_input.fill(amount)

    def click_add_to_cart(self):
        self.add_to_cart.click()

    def submit_product_review(self, name, email, message):
        self.review_name.fill(name)
        self.review_email.fill(email)
        self.review_message.fill(message)
        self.review_button.click()

