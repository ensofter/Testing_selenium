from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import random


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setUp(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        random_int = random.randint(0, 1000)
        login = f"buble{random_int}@gmail.com"
        pwd = "Passw0rd!"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(login, pwd)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/?promo=newYear2019."
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


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
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
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shopping_cart()
    product_page.should_not_be_success_message()

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
