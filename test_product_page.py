from .pages.product_page import ProductPage
import pytest
import time
from .pages.basket_page import BasketPage



@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shopping_cart()
    product_page.should_not_be_success_message()

class TestUserAddToBasketFromProductPage:
    self.link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_button_add_to_shoppingcart()
        product_page.add_to_shopping_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_success_message_about_add_to_shopping_cart()
        product_name = product_page.return_product_name()
        product_page.product_name_equal_product_name_in_success_message(product_name)
        product_page.should_be_price()
        product_page.shoulb_be_price_in_message_add_to_shoppingcart()
        product_price = product_page.return_product_price()
        product_page.product_price_equal_product_price_in_message_add_to_shoppingcart(product_price)



@pytest.mark.xfail
def test_message_disappered_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shopping_cart()
    product_page.should_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_h2_products_in_busket()
    basket_page.should_be_message_that_basket_is_empty()
