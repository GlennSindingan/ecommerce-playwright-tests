from playwright.sync_api import Page

class ContactPage:
    def __init__(self, page: Page):
        self.page = page

        self.contact_name = page.locator("[data-qa='name']")
        self.contact_email = page.locator("[data-qa='email']")
        self.contact_subject = page.locator("[data-qa='subject']")
        self.contact_message = page.locator("[data-qa='message']")
        self.upload_button = page.locator("input[name='upload_file']")
        self.submit_button = page.locator("[data-qa='submit-button']")
        self.alert_message = page.locator(".status.alert.alert-success")

    def fill_contact_form(self, name: str, email: str, subject: str, message: str):
        self.contact_name.fill(name)
        self.contact_email.fill(email)
        self.contact_subject.fill(subject)
        self.contact_message.fill(message)

    def upload_file(self, file_path: str):
        self.upload_button.set_input_files(file_path)

    def click_submit_button(self):
        self.submit_button.click()


