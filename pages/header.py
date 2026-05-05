from playwright.sync_api import Page


class HeaderPage:
    def __init__(self, page: Page):
        self.page = page

        # Header
        self.delete_link = page.get_by_role("link", name="Delete Account")
        self.login_link = page.get_by_role("link", name=" Signup / Login")


    def delete_account(self):
        self.delete_link.click()

    def click_login_link(self):
        self.login_link.click()

    def get_logged_in_user_locator(self, username: str):
        return self.page.get_by_text(f"Logged in as {username}")