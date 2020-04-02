"""
Создать класс Page Object для страницы товара.

Опишите его в файле product_page.py в папке pages.

Описать в нем метод для добавления в корзину.
"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.basket_btn_loc)
        button_add_to_basket.click()

    def check_msg_when_add_to_basket(self):
        title_of_item = self.browser.find_element(*ProductPageLocators.product_title_loc).text
        message_if_added = self.browser.find_element(*ProductPageLocators.msg_after_add_loc).text
        assert title_of_item == message_if_added, 'Title of the product does not match to basket list'

    def check_equal_cost(self):
        price_item = self.browser.find_element(*ProductPageLocators.price_loc).text
        basket_total = self.browser.find_element(*ProductPageLocators.basket_total_loc).text
        assert price_item == basket_total, 'Price of item does not match to basket price'

    def check_if_item_added_to_basket(self):
        self.check_msg_when_add_to_basket()
        self.check_equal_cost()
