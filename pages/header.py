from playwright.sync_api import Page


class HeaderPage:
    def __init__(self, page: Page):
        self.page = page

        # Header
        self.delete_account_button = page.locator(".fa-trash-o")

    def delete_account(self):
        self.delete_account_button.click()