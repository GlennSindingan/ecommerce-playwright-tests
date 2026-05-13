from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator("#cart_info_table tbody tr")

    def verify_cart_row_details(self, row_index: int, expected_price: str, expected_qty: str, expected_total: str):
        # 1. Grab the specific row we want to check (0 for the first shirt, 1 for the second)
        row = self.cart_items.nth(row_index)
        
        # 2. Look inside that row for the specific columns, and assert the text!
        # (We use the built-in Playwright expect() here to make it super fast)
        
        expect(row.locator(".cart_price p")).to_have_text(expected_price)
        expect(row.locator(".cart_quantity button")).to_have_text(expected_qty)
        expect(row.locator(".cart_total p")).to_have_text(expected_total)