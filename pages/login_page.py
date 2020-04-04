from .base_page import BasePage
from .locators import LoginPageLocators
import time
import pdb


class LoginPage(BasePage):
    """
    Добавьте в LoginPage метод register_new_user(email, password),
    который принимает две строки и регистрирует пользователя.
    Реализуйте его, описав соответствующие элементы страницы.
    """

    def register_new_user(self, email, password):
        """ метод register_new_user(email, password),
        который принимает две строки и регистрирует пользователя.
        """
        email_f = f'{str(time.time())}@mail.ru'
        password_f = "@#somefakepass19"
        email = self.browser.find_element(*LoginPageLocators.register_email_loc)
        email.send_keys(email_f)
        password = self.browser.find_element(*LoginPageLocators.register_pass_loc)
        password.send_keys(password_f)
        confirm_pass = self.browser.find_element(*LoginPageLocators.confirm_pass_loc)
        confirm_pass.send_keys(password_f)
        submit_btn = self.browser.find_element(*LoginPageLocators.submit_btn_loc)
        submit_btn.click()
        time.sleep(5)
        # self.should_be_authorized_user()

    def should_be_login_page(self):
        """
        OK
        Check if login page and obligatory functions are available
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Check if url has value 'login'
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
