from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator("#cart_info_table tbody tr")
        self.checkout_button = page.get_by_text("Proceed To Checkout")
        self.register_login = page.get_by_role("link", name="Register / Login")
        self.delete_button = page.locator(".cart_quantity_delete")
        self.product_1_row = page.locator("#product-1")
        self.empty_cart_message = page.locator("#empty_cart")


    def verify_cart_row_details(self, row_index: int, expected_price: str, expected_qty: str, expected_total: str):
        row = self.cart_items.nth(row_index)
        expect(row.locator(".cart_price p")).to_have_text(expected_price)
        expect(row.locator(".cart_quantity button")).to_have_text(expected_qty)
        expect(row.locator(".cart_total p")).to_have_text(expected_total)

    def click_checkout_button(self):
        self.checkout_button.click()

    def click_register_login(self):
        self.register_login.click()

    def click_delete_button(self):
        self.delete_button.click()