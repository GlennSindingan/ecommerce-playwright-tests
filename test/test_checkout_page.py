from playwright.sync_api import Page, expect
from url.config import HOMEPAGE_URL, CARTPAGE_URL
from pages.header import HeaderPage
from pages.products import ProductPage
from pages.cart import CartPage
from pages.login import LoginPage
from utils.test_data import my_address_data


def test_checkout(page: Page):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)
    header_page = HeaderPage(page)

    page.goto(HOMEPAGE_URL)

    product_page.add_product_to_cart(0)
    product_page.click_view_cart()

    expect(page).to_have_url(CARTPAGE_URL)
    cart_page.click_checkout_button()
    cart_page.click_register_login()

    login_page.account_signup("wenglong", "we441sadcczxc4axsd32241@gmail.com")
    login_page.enter_account_info("wenglong", "wengdie322")
    login_page.enter_address_info(my_address_data)

    expect(page.get_by_text("Account Created!")).to_be_visible()
    login_page.click_continue()
    expected_username = my_address_data["fname"]
    expect(header_page.get_logged_in_user_locator(expected_username)).to_be_visible()

    # TODO continue test case 14 ---- step 12


    

    
