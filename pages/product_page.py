from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_button_add_to_shoppingcart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to shopping cart is not presented"

    def add_to_shopping_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_be_success_message_about_add_to_shopping_cart(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADD_TO_CART), "Message add to shopping cart is not presented"

    def product_name_equal_product_name_in_success_message(self, product_name):
        success_message_product_add_to_cart = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADD_TO_CART)
        assert product_name in success_message_product_add_to_cart.text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def shoulb_be_price_in_message_add_to_shoppingcart(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_MESSAGE_PRODUCT_IN_SHOPPINGCART), "Product price in shoppingcart is not presented"

    def product_price_equal_product_price_in_message_add_to_shoppingcart(self, product_price):
        product_price_in_shoppingcart = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE_PRODUCT_IN_SHOPPINGCART)
        assert product_price == product_price_in_shoppingcart.text, "Product price and product price in message add to shoppingcart is not equal"

    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1)
        return product_name.text

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADD_TO_CART), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADD_TO_CART), "Succeess message is presented, but should disappeared"
