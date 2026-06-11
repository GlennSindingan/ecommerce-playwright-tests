from playwright.sync_api import Page, expect
from pages.header import HeaderPage
from pages.product_details import ProductDetailsPage
from pages.products import ProductPage
from url.config import HOMEPAGE_URL
from utils.test_data import REVIEW_MSG


def test_product_review(page: Page, dynamic_email):
    product_page = ProductPage(page)
    header_page = HeaderPage(page)
    details_page = ProductDetailsPage(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_product_link()
    product_page.click_product_button()
    details_page.submit_product_review(
        name="glenn",
        email=dynamic_email,
        message="Quality Product!"
    )
    expect(page.get_by_text(REVIEW_MSG)).to_be_visible()