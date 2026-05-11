from playwright.sync_api import Page

class FooterPage:
    def __init__(self, page: Page):
        self.page = page
    
        self.footer_container = page.locator("#footer")
        self.subscription_heading = self.footer_container.locator("h2").filter(has_text="Subscription")
        self.email_input = self.footer_container.locator("#susbscribe_email")
        self.subscribe_button = self.footer_container.locator("#subscribe")
        self.success_message = page.get_by_text("You have been successfully subscribed!")

    def fill_subscription(self, email: str):
        self.email_input.fill(email)
        self.subscribe_button.click()