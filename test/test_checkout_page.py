from playwright.sync_api import Page, expect
from url.config import HOMEPAGE_URL, CARTPAGE_URL
from pages.header import HeaderPage
from pages.products import ProductPage
from pages.cart import CartPage
from pages.login import LoginPage

def test_checkout(self, page: Page):
    header_page = HeaderPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)

    page.goto(HOMEPAGE_URL)

    product_page.click_product_button()
    header_page.click_cart_link()
    expect(page).to_have_url(CARTPAGE_URL)

    cart_page.click_checkout_button()
    cart_page.click_register_login()

    login_page.account_signup()
    login_page.enter_account_info()
    login_page.enter_address_info()

    expect(page.get_by_text("Account Created!")).to_be_visible()
    login_page.click_continue()
    expect(header_page.get_logged_in_user_locator(expected_username)).to_be_visible()
    header_page.click_cart_link()
    cart_page.click_checkout_button()
    



    # TODO continue test case 14


    

    
