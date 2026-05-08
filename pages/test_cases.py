from playwright.sync_api import Page

class TestCases:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.get_by_text("Test Cases", exact=True)
        self.page_subtext = page.get_by_text("Below is the list of test Cases for you to practice the Automation. "
        "Click on the scenario for detailed Test Steps:"
        )

        