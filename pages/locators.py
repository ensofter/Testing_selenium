from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, "h1")
    SUCCESS_MESSAGE_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) > .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_IN_MESSAGE_PRODUCT_IN_SHOPPINGCART = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner p > strong")
