from playwright.sync_api import Page


class HeaderPage:
    def __init__(self, page: Page):
        self.page = page

        # Header
        self.delete_link = page.get_by_role("link", name="Delete Account")
        self.login_link = page.get_by_role("link", name=" Signup / Login")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.product_link = page.get_by_role("link", name="Products")
        self.contact_link = page.get_by_role("link", name="Contact us")


    def delete_account(self):
        self.delete_link.click()

    def click_login_link(self):
        self.login_link.click()

    def get_logged_in_user_locator(self, username: str):
        return self.page.get_by_text(f"Logged in as {username}")

    def click_logout_link(self):
        self.logout_link.click()

    def click_contact_us_link(self):
        self.contact_link.click()

    def click_product_link(self):
        self.product_link.click()