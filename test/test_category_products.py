from playwright.sync_api import Page, expect
from pages.cart import CartPage
from pages.header import HeaderPage
from pages.products import ProductPage
from pages.category_products import CategoryPage
from url.config import HOMEPAGE_URL

def test_view_category_products(page: Page):
    category_products = CategoryPage(page)
    page.goto(HOMEPAGE_URL)

    expect(category_products.left_sidebar).to_be_visible()
    category_products.click_women_category()
    category_products.click_dress_category()
    expect(category_products.dress_heading).to_be_visible()

    category_products.click_women_category()
    category_products.click_top_category()
    expect(category_products.top_heading).to_be_visible()

    category_products.click_men_category()
    category_products.click_tshirt_category()
    expect(category_products.tshirt_heading).to_be_visible()

    category_products.click_men_category()
    category_products.click_jeans_category()
    expect(category_products.jeans_heading).to_be_visible()



