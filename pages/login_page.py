"""
This module initiate the methods of user registration & login
and checks the presence of the corresponding web elements
"""
from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    """
    Class initiates registration and login methods
    """

    def register_new_user(self, email, password):
        """
        Register new user through email and password params
        """
        email_field = self.browser.find_element(*LoginPageLocators.register_email_loc)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.register_pass_loc)
        password_field.send_keys(password)
        confirm_pass_field = self.browser.find_element(*LoginPageLocators.confirm_pass_loc)
        confirm_pass_field.send_keys(password)
        submit_btn = self.browser.find_element(*LoginPageLocators.submit_btn_loc)
        submit_btn.click()
        time.sleep(5)

    def should_be_login_page(self):
        """
        Check if login page and registration form are available
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Check if url has readable value 'login'
        """
        assert 'login' in self.browser.current_url, \
            "Current url doesn't have 'login'"

    def should_be_login_form(self):
        """
        Check if 'login' form is available from current page
        """
        assert self.is_element_present(*LoginPageLocators.login_form_loc), \
            'Login form does not exist on this page'

    def should_be_register_form(self):
        """
        Check if 'register' form is available from current page
        """
        assert self.is_element_present(*LoginPageLocators.register_form_loc), \
            'Register form does not exist on this page'
