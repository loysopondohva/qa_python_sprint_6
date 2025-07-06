import allure
from locators.order_page_locators import *
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняение первой части формы заказа самоката')
    def filling_first_part_order_form(self, test_data):
        self.wait_for_visible_element(OrderFormLocators.FIRST_NAME)
        self.click_on_element(OrderFormLocators.FIRST_NAME)
        self.send_keys_to_input(OrderFormLocators.FIRST_NAME, test_data['first_name'])
        self.click_on_element(OrderFormLocators.LAST_NAME)
        self.send_keys_to_input(OrderFormLocators.LAST_NAME, test_data['last_name'])
        self.click_on_element(OrderFormLocators.ADDRESS)
        self.send_keys_to_input(OrderFormLocators.ADDRESS, test_data['address'])
        self.click_on_element(OrderFormLocators.METRO)
        self.send_keys_to_input(OrderFormLocators.METRO, test_data['metro'])
        self.click_on_element(OrderFormLocators.METRO_DROPDOWN_ITEM)
        self.click_on_element(OrderFormLocators.PHONE)
        self.send_keys_to_input(OrderFormLocators.PHONE, test_data['phone'])
        self.click_on_element(OrderFormLocators.CONTINUE_BUTTON)

    @allure.step('Заполняение второй части формы заказа самоката')
    def filling_second_part_order_form(self, test_data):
        self.wait_for_visible_element(OrderFormLocators.DELIVERY_DATE)
        self.click_on_element(OrderFormLocators.DELIVERY_DATE)
        self.send_keys_to_input(OrderFormLocators.DELIVERY_DATE, test_data['delivery_date'])
        self.click_on_element(OrderFormLocators.scooter_color(test_data['scooter_color']))
        self.click_on_element(OrderFormLocators.RENTAL_TIME_FIELD)
        self.click_on_element(OrderFormLocators.rental_time_dropdown(test_data['rental_time']))

        self.click_on_element(OrderFormLocators.COURIER_COMMENTS)
        self.send_keys_to_input(OrderFormLocators.COURIER_COMMENTS, test_data['comments'])
        self.click_on_element(OrderFormLocators.ORDER_BUTTON)
        self.wait_for_visible_element(OrderConfirmationLocators.CONFIRM_BUTTON_YES)
        self.click_on_element(OrderConfirmationLocators.CONFIRM_BUTTON_YES)


    @allure.step('Проверить видимость заголовка "Заказ Оформлен"')
    def check_order_complete(self):
        order_header = self.wait_for_visible_element(OrderCompleteLocators.COMPLETE_HEADER_TEXT)
        return order_header.is_displayed()