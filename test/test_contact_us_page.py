from playwright.sync_api import Page, Dialog, expect
from pages.header import HeaderPage
from pages.contact_us import ContactPage
from url.config import HOMEPAGE_URL

def test_contact_form(page: Page):
    contact_page = ContactPage(page)
    header_page = HeaderPage(page)

    def handle_dialog(dialog: Dialog):
        dialog.accept()


    page.on("dialog", handle_dialog)

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

    page.wait_for_load_state("networkidle")
    expect(contact_page.alert_message).to_be_visible()

