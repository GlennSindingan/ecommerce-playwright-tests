from playwright.sync_api import Page, expect
from pages.login import LoginPage
from url.config import LOGIN_URL


def test_account_signup(page: Page):
    login_page = LoginPage(page)

    page.goto(LOGIN_URL)

    expect(page.get_by_role("heading", name="Enter Account Information")).to_be_visible()
    login_page.account_signup("glenn", "glen322n@gmail.com")




