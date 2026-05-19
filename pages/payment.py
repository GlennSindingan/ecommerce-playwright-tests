from playwright.sync_api import Page

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

        self.card_name = page.locator("[data-qa='name-on-card']")
        self.card_number = page.locator("[data-qa='card-number']")
        self.cvc = page.locator("[data-qa='cvc']")
        self.expiration_month = page.locator("[data-qa='expiry-month']")
        self.expiration_year = page.locator("[data-qa='expiry-year']")
        self.confirm_order = page.locator("[data-qa='pay-button']")

    def fill_payment_details(self, name, card_number, cvc, month_expiry, year_expiry):
        self.card_name.fill(name)
        self.card_number.fill(card_number)
        self.cvc.fill(cvc)
        self.expiration_month.fill(month_expiry)
        self.expiration_year.fill(year_expiry)

    def click_pay_and_confirm(self):
        self.confirm_order.click()
        


