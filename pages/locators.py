"""
This module describes the locators for web elements such as links, buttons, input fields and others.
"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    """
    Locators for obligatory elements for base pages
    """
    login_link_loc = (By.CSS_SELECTOR, '#login_link')
    basket_link_loc = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    user_icon_loc = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    """
    Locator for login link from main page
    """
    login_link_loc = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """
    Locators for login and register elements
    """
    login_form_loc = (By.CSS_SELECTOR, "#login_link")
    register_form_loc = (By.CSS_SELECTOR, "#register_form")
    register_email_loc = (By.CSS_SELECTOR, '#register_form #id_registration-email')
    register_pass_loc = (By.CSS_SELECTOR, '#register_form #id_registration-password1')
    confirm_pass_loc = (By.CSS_SELECTOR, '#register_form #id_registration-password2')
    submit_btn_loc = (By.NAME, 'registration_submit')


class ProductPageLocators:
    """
    Locators for products and following basket items
    """
    basket_btn_loc = (By.CSS_SELECTOR, '.btn-add-to-basket')
    product_title_loc = (By.CSS_SELECTOR, 'h1')
    msg_after_add_loc = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    success_msg_loc = (By.CSS_SELECTOR, '.alert-success:first-child')
    price_loc = (By.CSS_SELECTOR, '.product_main .price_color')
    basket_total_loc = (By.CSS_SELECTOR, '.alert-info .alertinner strong')



class BasketPageLocators:
    """
    Locators for basket only page
    """
    basket_items_loc = (By.CSS_SELECTOR, '.basket-items')
    basket_message_loc = (By.CSS_SELECTOR, '#content_inner')
