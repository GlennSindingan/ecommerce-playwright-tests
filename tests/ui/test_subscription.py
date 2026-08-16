from playwright.sync_api import Page, expect
from pages.header import HeaderPage
from url.config import HOMEPAGE_URL
from pages.footer import FooterPage


def test_subscription_on_homepage(page: Page, dynamic_email):
    footer_page = FooterPage(page)
    page.goto(HOMEPAGE_URL)

    expect(footer_page.subscription_heading).to_be_visible()
    footer_page.fill_subscription(dynamic_email)
    expect(footer_page.success_message).to_be_visible()

def test_subscription_on_cart(page: Page, dynamic_email):
    footer_page = FooterPage(page)
    header_page = HeaderPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_cart_link()
    expect(footer_page.subscription_heading).to_be_visible()
    footer_page.fill_subscription(dynamic_email)
    expect(footer_page.success_message).to_be_visible()

