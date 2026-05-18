from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.comment_box = page.locator("textarea[name='message']")
        self.place_order_button = page.get_by_role("link", name="Place Order")

    def enter_comment(self, message_text: str):
        self.comment_box.fill(message_text)

    def click_place_order(self):
        self.place_order_button.click()