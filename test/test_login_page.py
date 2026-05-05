from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.header import HeaderPage
from url.config import LOGIN_URL
from utils.test_data import my_address_data



def test_register_and_delete_user(page: Page):
    login_page = LoginPage(page)
    header_page = HeaderPage(page)

    page.goto(LOGIN_URL)

    login_page.account_signup("korikong322", "fineek322 @gmail.com")
    expect(page.get_by_role("heading", name="Enter Account Information")).to_be_visible()
    login_page.enter_account_info("cofee", "pass322421123")
    login_page.enter_address_info(my_address_data)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    login_page.click_continue()

    header_page.delete_account()
    expect(page.get_by_text("Account Deleted")).to_be_visible()








