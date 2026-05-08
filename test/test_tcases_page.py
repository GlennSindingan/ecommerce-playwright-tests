from playwright.sync_api import Page, expect
from pages.header import HeaderPage
from pages.test_cases import TestCases
from url.config import HOMEPAGE_URL

def test_verify_tc_page(page: Page):
    header_page = HeaderPage(page)
    tcases_page = TestCases(page)
    page.goto(HOMEPAGE_URL)

    header_page.click_testcases_link()
    expect(tcases_page.page_title).to_be_visible()
    expect(tcases_page.page_subtext).to_be_visible()