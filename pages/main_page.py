"""
This module describes methods for main page only
"""
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """
    Main page methods that are based on BasePage methods
    """

    def go_to_login_page(self):
        """
        Redirect to login page
        """
        link = self.browser.find_element(*MainPageLocators.login_link_loc)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """
        Check if link for login form is available
        """
        assert self.is_element_present(*MainPageLocators.login_link_loc)
