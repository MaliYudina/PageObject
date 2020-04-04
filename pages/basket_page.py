"""
This module checks the status of the basket message and the following
success message when a user or a guest submits the goods pucrhase
"""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Check the status of basket and success message
    """

    def should_be_empty_basket(self):
        """
        Check if the basket is empty
        """
        self.should_not_be_items_in_the_basket()
        self.should_be_text_empty_basket()

    def should_not_be_items_in_the_basket(self):
        """
        Check if basket has no items and no success message after purchasing goods
        """
        assert self.is_not_element_present(*BasketPageLocators.basket_items_loc), \
            'Success message is presented, but should not be'

    def should_be_text_empty_basket(self):
        """
        Check if basket has no items but purchasing success message appeared
        """
        text_message_in_basket = self.browser.find_element(*BasketPageLocators.basket_message_loc).text
        assert 'Your basket is empty' in text_message_in_basket, \
            'The basket not exist the message that basket is empty'
