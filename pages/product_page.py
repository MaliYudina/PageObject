"""
Создать класс Page Object для страницы товара.

Опишите его в файле product_page.py в папке pages.

Описать в нем метод для добавления в корзину.
"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_add_to_basket.click()
