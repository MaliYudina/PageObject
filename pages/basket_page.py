"""
BasketPage. Реализуйте там необходимые проверки, в том числе отрицательную,
которую мы обсуждали в предыдущих шагах.

"""

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        """Проверка на пустую корзину"""
        self.should_not_be_items_in_the_basket()
        self.should_be_text_empty_basket()

    def should_not_be_items_in_the_basket(self):
        """Проверка: не должно быть товаров в корзине"""
        assert self.is_not_element_present(*BasketPageLocators.basket_items_loc), \
            'Success message is presented, but should not be'

    def should_be_text_empty_basket(self):
        """Проверка: есть сообщение корзина пуста"""
        text_message_in_basket = self.browser.find_element(*BasketPageLocators.basket_message_loc).text
        assert 'Your basket is empty' in text_message_in_basket, \
            'The basket not exist the message that basket is empty'
