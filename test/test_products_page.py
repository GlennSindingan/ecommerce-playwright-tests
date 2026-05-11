from playwright.sync_api import Page, expect
from pages.header import HeaderPage
from pages.products import Product
from url.config import HOMEPAGE_URL


def test_all_products_display(page: Page):
    product_page = Product(page)
    header_page = HeaderPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_product_link()
    expect(page).to_have_url("https://automationexercise.com/products")
    expect(product_page.product_cards.first).to_be_visible()
    assert product_page.product_cards.count() > 5

    product_page.click_product_button()
    expect(product_page.product_name).to_be_visible()
    expect(product_page.product_category).to_be_visible()
    expect(product_page.product_price).to_be_visible()
    expect(product_page.product_availability).to_be_visible()
    expect(product_page.product_condition).to_be_visible()
    expect(product_page.product_brand).to_be_visible()