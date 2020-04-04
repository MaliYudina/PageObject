"""
This module implements base function for pages, such as open, redirect,
check presence or non-presence of elements and interact with submit elements
"""

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math
import time


class BasePage:
    """
    Common methods for base page functions
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        """
        Check if the user authorized
        """
        assert self.is_element_present(*BasePageLocators.user_icon_loc), \
            'User icon is not presented, probably unauthorised user'

    def is_element_present(self, how, what):
        """
        Check the presence of an element
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Check the absence of an element
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Check if an element will dissapear after required actions or time period
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """
        Solve math quiz from alert to get promo code and submit the promo code
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        time.sleep(2)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            time.sleep(3)
            print(f'Your code: {alert.text}')
            alert.accept()
            time.sleep(30)
        except NoAlertPresentException:
            print('No second alert presented')

    def go_to_basket_page(self):
        """
        Redirect to the basket page
        """
        link = self.browser.find_element(*BasePageLocators.basket_link_loc)
        link.click()

    def go_to_login_page(self):
        """
        Redirect to the login page
        """
        link = self.browser.find_element(*BasePageLocators.login_link_loc)
        link.click()

    def should_be_login_link(self):
        """
        Check if the login link available
        """
        assert self.is_element_present(*BasePageLocators.login_link_loc), 'Login link is not presented'
