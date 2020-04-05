"""
This module resolves running of tests for product pages of
http://selenium1py.pythonanywhere.com website.
Checks actions of users and guests while buying products on the website.
"""
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time


class TestGuestUserAddToBasketFromProductPage:
    """
    Tests for non-authorized guest user
    """
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """
        Guest can add items to the basket, the name and price of the product
        shall be equal to the name and price in the basket after submit button click
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.check_if_item_added_to_basket()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """
        Guest redirected to the basket page without submitting the basket button.
        The basket shall be empty and 'empty message' is present.
        """
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """
        Guest can open login page from any product page
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/google-hacking_197/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        """
        Guest can see login link with 'login' text value from any product page
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


class TestUserAddToBasketFromProductPage:
    """
    Class for registration a test user for the following implementation of user action
    when using product pages
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/silence-on-the-wire_196/"

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        """
        Prepare data for a new user to authorize profile for a test user
        Check if the test user was authenticated
        """
        login_page_link = 'http://selenium1py.pythonanywhere.com'
        page = LoginPage(browser, login_page_link)
        page.open()
        page.go_to_login_page()
        email = f'{str(time.time())}@fake-mail.ru'
        password = "@#somefakepass19"
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        Success message does not exist when a user opened product page
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Test if authorized user can add products to a basket
        The price from product page and basket page should be equal
        """
        page = ProductPage(browser, TestUserAddToBasketFromProductPage.link)
        page.open()
        page.add_to_basket()
        page.check_if_item_added_to_basket()
        page.check_equal_cost()
