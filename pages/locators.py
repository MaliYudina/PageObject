from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    basket_btn_loc = (By.CSS_SELECTOR, '.btn-add-to-basket')
    product_title_loc = (By.CSS_SELECTOR, 'h1')
    msg_after_add_loc = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    price_loc = (By.CSS_SELECTOR, '.product_main .price_color')
    basket_total_loc = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    success_msg_loc = (By.CSS_SELECTOR, '.alert-success:first-child')
