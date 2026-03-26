from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_HEADER = (By.XPATH, (By.XPATH, '//div[contains(@class, "Home_Header")]'))
    LOGO_YANDEX_BUTTON = (By.XPATH, '//a[contains(@class, "Header_LogoYandex")]')
    LOGO_SCOOTER_BUTTON = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    PAGE_TITLE = (By.XPATH, '//title')
    ORDER_BUTTONS = {
        'HEADER' : (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]'),
        'MAIN' : (By.XPATH, '//div[contains(@class, "Home_RoadMap")]//button[contains(text(), "Заказать")]')
    }
    FAQ_SECTION = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    @staticmethod
    def faq_answer(question_id):
        return By.XPATH, f'//div[contains(@class, "Home_FAQ")]//div[contains(@id,"accordion__panel-{question_id}")]'

    @staticmethod
    def faq_question(question_id):
       return By.XPATH, f'//div[contains(@class, "Home_FAQ")]//div[contains(@id, "accordion__heading-{question_id}")]/parent::div'