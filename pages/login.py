from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        #Login functions
        self.login_email = page.locator("[data-qa='login-email']")
        self.login_password = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")


        #Sign up functions
        self.signup_name = page.locator("[data-qa='signup-name']")
        self.signup_email = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")

    def account_login(self, email, password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def account_signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()
