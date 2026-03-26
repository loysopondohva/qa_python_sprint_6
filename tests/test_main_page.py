import pytest
import allure

import urls
from pages.main_page import MainPage
from data import *


class TestMainPageFAQ:

    @allure.title('Проверка раздела "Вопросы о Важном"')
    @allure.description('Проверка появления нужного текста при клике на каждую иконку разворачивания в разделе')
    # В параметрах передаём данные для проверки отображения содержимого при клике на Вопросы о Важном
    @pytest.mark.parametrize('question_number, expected_answer', TestFAQData.faq_content)
    def test_displayed_faq_text(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_question(question_number)
        main_page.wait_for_faq_question(question_number)
        main_page.click_on_faq_question(question_number)
        main_page.wait_for_faq_answer(question_number)
        answer_text = main_page.get_text_from_faq_answer(question_number)
        assert answer_text == expected_answer

    @allure.title('Проверка перехода по клику на лого Самоката')
    @allure.description('Проверка перехода на главную страницу, при клике на лого Самоката')
    def test_transition_by_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_header_order_button()
        main_page.wait_loading_header_order_button()
        main_page.click_on_logo_scooter_button()
        main_page.wait_loading_header_order_button()
        website_url = main_page.get_page_url()
        website_title = main_page.get_page_title()
        assert website_title == TransitionData.scooter_title
        assert website_url == urls.main_site

    @allure.title('Проверка перехода по клику на лого Яндекса')
    @allure.description('Проверка перехода на страницу Дзена, при клике на лого Яндекса')
    def test_transition_by_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex_button()
        main_page.switch_to_next_tab()
        website_title = main_page.get_page_title()
        website_url = main_page.get_page_url()
        assert website_title == TransitionData.dzen_title
        assert website_url == urls.dzen_page