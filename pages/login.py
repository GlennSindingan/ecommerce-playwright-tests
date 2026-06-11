from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Login functions
        self.login_email = page.locator("[data-qa='login-email']")
        self.login_password = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

        # Sign up functions
        self.signup_name = page.locator("[data-qa='signup-name']")
        self.signup_email = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")

        # Account info functions
        self.select_gender = page.locator("#id_gender1")
        self.name = page.locator("#name")
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.days_dropdown = page.locator("#days")
        self.months_dropdown = page.locator("#months")
        self.years_dropdown = page.locator("#years")

        # Address info functions
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company_name = page.locator("#company")
        self.address1_name = page.locator("#address1")
        self.address2_name = page.locator("#address2")
        self.country_dropdown = page.locator("#country")
        self.state_name = page.locator("#state")
        self.city_name = page.locator("#city")
        self.zip_code = page.locator("#zipcode")
        self.mobile_number = page.locator("#mobile_number")
        self.create_button = page.locator("[data-qa='create-account']")

        # After account creation
        self.continue_button = page.locator("[data-qa='continue-button']")

    def account_login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def account_signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def enter_account_info(self, name, password):
        self.select_gender.check()
        self.name.fill(name)

        self.password.fill(password)
        self.days_dropdown.select_option("10")
        self.months_dropdown.select_option("7")
        self.years_dropdown.select_option("2000")

    def enter_address_info(self, data: dict):
        self.first_name.fill(data["fname"])
        self.last_name.fill(data["lname"])
        self.company_name.fill(data["company"])
        self.address1_name.fill(data["address1"])
        self.address2_name.fill(data["address2"])
        self.country_dropdown.select_option(data["country"])
        self.state_name.fill(data["state"])
        self.city_name.fill(data["city"])
        self.zip_code.fill(data["zipcode"])
        self.mobile_number.fill(data["mobile_number"])
        self.create_button.click()

    def click_continue(self):
        self.continue_button.click()




