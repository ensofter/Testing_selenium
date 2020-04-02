from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_h2_products_in_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.H2_PRODUCTS_IN_BUSKET), "H2 products is presented, but shouldn't be"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_THAT_BASKET_IS_EMPTY), "Message is not presented, basket is not empty"
