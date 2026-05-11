from playwright.sync_api import Page, expect

from pages.header import HeaderPage
from pages.products import ProductPage
from url.config import HOMEPAGE_URL


def test_add_to_cart_page(page: Page):
    header_page = HeaderPage(page)
    product_page = ProductPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_product_link()

    product_page.add_product_to_cart(0)

    product_page.click_continue_shopping_button()

    product_page.add_product_to_cart(1)

    product_page.click_view_cart()
   # assert product_page.product_cards.count() > 5
   # TODO: Continue the /view_cart page
   # TODO: Confirm there are 2 products on that table