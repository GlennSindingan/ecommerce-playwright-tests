from playwright.sync_api import Page, expect
from pages.login import LoginPage
from pages.header import HeaderPage
from url.config import LOGIN_URL, HOMEPAGE_URL
from utils.test_data import my_address_data, LOGIN_PASSWORD, LOGIN_EMAIL


def test_register_and_delete_user(page: Page, dynamic_email: str):
    login_page = LoginPage(page)
    header_page = HeaderPage(page)
    page.goto(LOGIN_URL)

    login_page.account_signup("wendiee", dynamic_email)
    expect(page.get_by_role("heading", name="Enter Account Information")).to_be_visible()
    login_page.enter_account_info("cofee", "pass322421123")
    login_page.enter_address_info(my_address_data)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    login_page.click_continue()
    header_page.delete_account()
    expect(page.get_by_text("Account Deleted")).to_be_visible()

def test_account_login(page: Page):
    login_page = LoginPage(page)
    header_page = HeaderPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_login_link()
    login_page.account_login(LOGIN_EMAIL, LOGIN_PASSWORD)
    expected_username = my_address_data["fname"]
    expect(header_page.get_logged_in_user_locator(expected_username)).to_be_visible()

def test_incorrect_credentials(page: Page):
    login_page = LoginPage(page)
    page.goto(LOGIN_URL)

    login_page.account_login(LOGIN_EMAIL, "123")
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

def test_account_logout(page: Page):
    login_page = LoginPage(page)
    header_page = HeaderPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_login_link()
    login_page.account_login(LOGIN_EMAIL, LOGIN_PASSWORD)
    expected_username = my_address_data["fname"]
    expect(header_page.get_logged_in_user_locator(expected_username)).to_be_visible()
    header_page.click_logout_link()
    expect(page.get_by_text("Login to your account")).to_be_visible()

def test_existing_email(page: Page):
    login_page = LoginPage(page)
    page.goto(LOGIN_URL)

    login_page.account_signup("glenn", LOGIN_EMAIL)
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()



    

