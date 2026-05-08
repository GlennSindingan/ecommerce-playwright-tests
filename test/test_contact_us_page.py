from playwright.sync_api import Page, expect
from pages.header import HeaderPage
from pages.contact_us import ContactPage
from url.config import LOGIN_URL, HOMEPAGE_URL
from utils.test_data import my_address_data

def test_contact_form(page: Page):
    contact_page = ContactPage(page)
    header_page = HeaderPage(page)

    page.goto(HOMEPAGE_URL)

    header_page.click_contact_us_link()
    contact_page.fill_contact_form(
        name="glenn",
        email="glenn@gmail.com",
        subject="test",
        message="thanks"
    )
    contact_page.upload_file("utils/dummy_upload.txt")
    contact_page.click_submit_button()