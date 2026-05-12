from playwright.sync_api import Page, expect
from pages.cart import CartPage
from pages.header import HeaderPage
from pages.products import ProductPage
from url.config import HOMEPAGE_URL


def test_add_to_cart_page(page: Page):
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

    # TODO: Complete the test case above