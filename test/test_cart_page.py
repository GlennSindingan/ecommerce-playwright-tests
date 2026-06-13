from playwright.sync_api import Page, expect
from pages.cart import CartPage
from pages.header import HeaderPage
from pages.product_details import ProductDetailsPage
from pages.products import ProductPage
from url.config import HOMEPAGE_URL


def test_add_to_cart(page: Page):
    header_page = HeaderPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_product_link()

    product_page.add_product_to_cart(0)

    product_page.click_continue_shopping_button()

    product_page.add_product_to_cart(1)

    product_page.click_view_cart()
    expect(cart_page.cart_items).to_have_count(2)

    # Verify the First Product (Blue Top)
    cart_page.verify_cart_row_details(0, "Rs. 500", "1", "Rs. 500")

    # Verify the Second Product (Men Tshirt)
    cart_page.verify_cart_row_details(1, "Rs. 400", "1", "Rs. 400")

def test_product_quantity_cart(page: Page):
    product_page = ProductPage(page)
    product_details = ProductDetailsPage(page)
    cart_page = CartPage(page)
    header_page = HeaderPage(page)

    page.goto(HOMEPAGE_URL)
    header_page.click_product_link()
    product_page.click_product_button()
    expect(page).to_have_url(f"{HOMEPAGE_URL}/product_details/1")
    product_details.set_amount("4")

    product_details.click_add_to_cart()
    product_page.click_view_cart()
    cart_page.verify_cart_row_details(0, "Rs. 500", "4", "Rs. 2000")

def test_remove_product(page: Page):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    page.goto(HOMEPAGE_URL)

    product_page.add_product_to_cart(0)
    product_page.click_view_cart()
    expect(cart_page.product_1_row).to_be_visible()
    cart_page.click_delete_button()
    expect(cart_page.product_1_row).to_be_hidden()
    expect(cart_page.empty_cart_message).to_be_visible()


    






