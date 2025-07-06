import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликнуть по кнопке "Заказать" по переданному локатору')
    def click_on_order_button(self, locator):
        self.scroll_to_element(locator)
        self.wait_for_visible_element(locator)
        self.click_on_element(locator)

    @allure.step('Подождать загрузки кнопки "Заказать" в Хедере')
    def wait_loading_header_order_button(self):
        self.wait_for_visible_element(MainPageLocators.ORDER_BUTTONS['HEADER'])

    @allure.step('Кликнуть на кнопку "Заказать" в Хедере')
    def click_on_header_order_button(self):
       self.click_on_order_button(MainPageLocators.ORDER_BUTTONS['HEADER'])

    @allure.step('Подождать загрузки кнопки "Заказать" в середине страницы')
    def wait_loading_main_order_button(self):
        self.wait_for_visible_element(MainPageLocators.ORDER_BUTTONS['MAIN'])

    @allure.step('Кликнуть на кнопку "Заказать" в середине страницы')
    def click_on_main_order_button(self):
        self.click_on_order_button(MainPageLocators.ORDER_BUTTONS['MAIN'])

    @allure.step('Скролл до раздела FAQ')
    def scroll_to_faq_question(self, question_id):
        self.scroll_to_element(MainPageLocators.faq_question(question_id))

    @allure.step('Подождать загрузки вопроса FAQ')
    def wait_for_faq_question(self, question_id):
        self.wait_for_visible_element(MainPageLocators.faq_question(question_id))

    @allure.step('Клик по вопросу FAQ')
    def click_on_faq_question(self, question_id):
        self.click_on_element(MainPageLocators.faq_question(question_id))

    @allure.step('Подождать загрузки ответа FAQ')
    def wait_for_faq_answer(self, answer_id):
        self.wait_for_visible_element(MainPageLocators.faq_answer(answer_id))

    @allure.step('Получить отображаемый текст ответа FAQ')
    def get_text_from_faq_answer(self, answer_id):
        return self.get_text_on_element(MainPageLocators.faq_answer(answer_id))

    @allure.step('Подождать загрузки части лого "Самокат"')
    def wait_loading_logo_scooter_button(self):
        self.wait_for_visible_element(MainPageLocators.LOGO_SCOOTER_BUTTON)

    @allure.step('Кликнуть части лого "Самокат"')
    def click_on_logo_scooter_button(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER_BUTTON)

    @allure.step('Подождать загрузки части лого "Яндекс"')
    def wait_loading_logo_yandex_button(self):
        self.wait_for_visible_element(MainPageLocators.LOGO_YANDEX_BUTTON)

    @allure.step('Кликнуть части лого "Яндекс"')
    def click_on_logo_yandex_button(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX_BUTTON)


    @allure.step('Получить title страницы')
    def get_page_title(self):
        self.wait_for_presence_element(MainPageLocators.PAGE_TITLE)
        return self.driver.title

