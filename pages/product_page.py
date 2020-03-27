from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_shoppingcart_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to shopping cart is not presented"

    def add_to_shopping_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_button.click()

    def should_be_success_message_about_add_to_shopping_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_CART), "Message add to shopping cart is not presented"

    def product_name_equal_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1)
        success_message_add_to_cart = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_CART)
        assert product_name.text in success_message_add_to_cart.text

    def should_be_cost(self):
        product_cost = self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Product cost is not presented"

    def shoulb_be_cost_in_shoppingcart(self):
        product_cost_in_shoppingcart = self.is_element_present(*ProductPageLocators.COST_IN_SHOPPINGCART), "Product cost in shoppingcart is not presented"

    def product_cost_and_product_cost_in_shoppingcart_should_be_equal(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        product_cost_in_shoppingcart = self.browser.find_element(*ProductPageLocators.COST_IN_SHOPPINGCART)
        assert product_cost.text == product_cost_in_shoppingcart.text, "Product cost and product cost in shoppingcart is not equal"

