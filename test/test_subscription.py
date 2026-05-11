from playwright.sync_api import Page, expect
from url.config import HOMEPAGE_URL
from pages.footer import FooterPage


def test_subscription_on_homepage(page: Page):
    footer_page = FooterPage(page)
    page.goto(HOMEPAGE_URL)

    expect(footer_page.subscription_heading).to_be_visible()
    footer_page.fill_subscription("glin@gmail.com")
    expect(footer_page.success_message).to_be_visible()
