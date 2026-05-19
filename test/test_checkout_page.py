from playwright.sync_api import Page, expect

from pages.checkout import CheckoutPage
from pages.payment import PaymentPage
from url.config import HOMEPAGE_URL, CARTPAGE_URL
from pages.header import HeaderPage
from pages.products import ProductPage
from pages.cart import CartPage
from pages.login import LoginPage
from utils.test_data import my_address_data, SUCCESS_MSG
import time


def test_checkout(page: Page):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)
    header_page = HeaderPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)

    page.goto(HOMEPAGE_URL)

    product_page.add_product_to_cart(0)
    product_page.click_view_cart()

    expect(page).to_have_url(CARTPAGE_URL)
    cart_page.click_checkout_button()
    cart_page.click_register_login()

    dynamic_email = f"wenglong_{time.time()}@gmail.com"

    login_page.account_signup("wenglong", dynamic_email)
    login_page.enter_account_info("wenglong", "wengdie322")
    login_page.enter_address_info(my_address_data)

    expect(page.get_by_text("Account Created!")).to_be_visible()
    login_page.click_continue()
    expected_username = my_address_data["fname"]
    expect(header_page.get_logged_in_user_locator(expected_username)).to_be_visible()
    header_page.click_cart_link()
    cart_page.click_checkout_button()

    # TODO add check description

    checkout_page.enter_comment("Thank u!")
    checkout_page.click_place_order()
    payment_page.fill_payment_details(
        name="Glenn",
        card_number="5555555555555555",
        cvc="322",
        month_expiry="05",
        year_expiry="2029"
    )
    payment_page.click_pay_and_confirm()
    expect(page.get_by_text(SUCCESS_MSG)).to_be_visible()
    header_page.delete_account()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    login_page.click_continue()





    

    
