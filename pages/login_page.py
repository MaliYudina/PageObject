from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Check if url has value 'login' """
        assert 'login' in self.browser.current_url,\
            "Current url doesn't have 'login'"

    def should_be_login_form(self):
        """Check if 'login' form is available from current page """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            'Login form does not exist on this page'

    def should_be_register_form(self):
        """Check if 'register' form is available from current page """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            'Register form does not exist on this page'
