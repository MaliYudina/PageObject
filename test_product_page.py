"""
This module resolves running of tests for product pages for website
http://selenium1py.pythonanywhere.com website.
Checks actions of users and guests while buying products on the website.
"""
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """метод для добавленя товара в корзину, проверки названия и цены товара"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_if_item_added_to_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    """Тест: при переходе со страницы продукта корзина пуста и есть сообщение об этом"""
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тест: гость может перейти на страницу логина со страницы продукта"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    """Тест: гость видит ссылку login_link на странице продукта"""
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


class TestUserAddToBasketFromProductPage:
    """
    OK В файле test_product_page.py добавьте новый класс для тестов TestUserAddToBasketFromProductPage.
    OK Добавьте туда уже написанные тесты test_guest_cant_see_success_message и
    test_guest_can_add_product_to_basket и
    переименуйте, заменив guest на user.
    Шаги тестов не изменятся, добавится лишь регистрация перед тестами.
    Параметризация здесь уже не нужна, не добавляйте её.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        """
        OK
        setup-функция, подготавливает данные и выполняется перед запуском каждого теста из класса
        Открывает форму регистрации, регистрирует нового пользователя
        Проверяет, что пользователь залогинен

        Добавьте в класс фикстуру setup. В этой функции нужно:
        открыть страницу регистрации
        зарегистрировать нового пользователя
        проверить, что пользователь залогинен
        """
        login_page_link = 'http://selenium1py.pythonanywhere.com'
        page = LoginPage(browser, login_page_link)
        page.open()
        time.sleep(2)
        page.go_to_login_page()
        time.sleep(2)
        # page.register_new_user(email='GGGmy@fakemail.org', password="@#somefakepass19")
        email = 'GGGmy@fakemail.org'
        password = "@#somefakepass19"
        page.register_new_user(email=email, password=password)
        time.sleep(2)
        page.should_be_authorized_user()
        time.sleep(2)

    def test_user_cant_see_success_message(self, browser):
        """OK
        Тест нет success_message
        """
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, TestUserAddToBasketFromProductPage.link)
        page.open()
        time.sleep(2)
        page.add_to_basket()
        time.sleep(5)
        page.check_if_item_added_to_basket()
        page.check_equal_cost()
