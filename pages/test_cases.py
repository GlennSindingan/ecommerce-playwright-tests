from playwright.sync_api import Page

class TestCasesPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.get_by_text("Test Cases", exact=True).first
        self.page_subtext = page.get_by_text("Below is the list of test Cases", exact=False)