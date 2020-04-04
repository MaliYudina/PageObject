"""
This module describes the methods actual for product items pages and interaction with basket page
"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Class for methods for product items & basket interactions
    """

    def add_to_basket(self):
        """
        Add to basket method that implements purchase of
        products through submitting the basket button
        """
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.basket_btn_loc)
        button_add_to_basket.click()

    def check_msg_when_add_to_basket(self):
        """
        Check if success message appeared after user or guest bought items
        """
        title_of_item = self.browser.find_element(*ProductPageLocators.product_title_loc).text
        message_if_added = self.browser.find_element(*ProductPageLocators.msg_after_add_loc).text
        assert title_of_item == message_if_added, 'Title of the product does not match to basket list'

    def check_equal_cost(self):
        """
        Check if price on product page is equal to the price in a basket page
        """
        price_item = self.browser.find_element(*ProductPageLocators.price_loc).text
        basket_total = self.browser.find_element(*ProductPageLocators.basket_total_loc).text
        assert price_item == basket_total, 'Price of item does not match to basket price'

    def check_if_item_added_to_basket(self):
        """
        Check if product was successfully added to the basket and price is equal
        """
        self.check_msg_when_add_to_basket()
        self.check_equal_cost()

    def should_not_be_success_message(self):
        """Success message shall not appear"""
        assert self.is_not_element_present(*ProductPageLocators.success_msg_loc), \
            'Success message is presented, but should not be'

    def should_be_success_message(self):
        """Method waits untill web element disappear after required actions or time period"""
        assert self.is_disappeared(*ProductPageLocators.success_msg_loc), \
            'Success message is not disappeared, but should be'
