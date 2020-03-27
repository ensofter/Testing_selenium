from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_shopping_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message_about_add_to_shopping_cart()
    product_page.product_name_equal_product_name_in_success_message()
    product_page.should_be_cost()
    product_page.should_be_cost()
    product_page.shoulb_be_cost_in_shoppingcart()
    product_page.product_cost_and_product_cost_in_shoppingcart_should_be_equal()
