import pytest
import allure

from data import *
from pages.main_page import MainPage
from pages.order_page import OrderPage

from locators.main_page_locators import  *

# Класс тестирования заказа самоката
class TestOrderScooter:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверка проверка оформления заказа самоката из двух точек входа при заполнении всех полей формы')

    # Передаём в параметрах локаторы кнопок заказа из заголовка и основной страницы и данные для заполнения формы заказа
    @pytest.mark.parametrize('button, order_data', [(MainPageLocators.ORDER_BUTTONS['HEADER'], Credentials.users[0]) ,(MainPageLocators.ORDER_BUTTONS['MAIN'], Credentials.users[1])])
    def test_order_scooter(self, driver, button, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_button(button)
        order_page.filling_first_part_order_form(order_data)
        order_page.filling_second_part_order_form(order_data)
        assert order_page.check_order_complete()


