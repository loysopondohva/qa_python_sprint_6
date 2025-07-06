from selenium.webdriver.common.by import By


class OrderFormLocators:
    HEADER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(text(), "Заказать")]')
    MAIN_ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Home_RoadMap")]//button[contains(text(), "Заказать")]')
    TITLE_PERSONAL_PAGE = (By.XPATH, '//div[contains(text(),"Для кого самокат") and contains(@class, "Order_Header")]')
    FIRST_NAME = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
    LAST_NAME = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
    ADDRESS = (By.XPATH, '//input[contains(@placeholder, "Адрес")]')
    METRO = (By.XPATH, '//input[contains(@placeholder, "Станция метро")]')
    METRO_DROPDOWN_ITEM = (By.XPATH, '//li[contains(@class, "select-search__row")][1]')
    PHONE = (By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    CONTINUE_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')
    TITLE_RENT_PAGE = (By.XPATH, '//div[contains(text(),"Про аренду") and contains(@class, "Order_Header")]')
    DELIVERY_DATE = (By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]')
    RENTAL_TIME_DROPDOWN = (By.XPATH, '//div[contains(@class, "Dropdown-placeholder")]')
    RENTAL_TIME_FIELD = (By.XPATH, '//div[contains(text(), "* Срок аренды")]')

    COURIER_COMMENTS = (By.XPATH, '//div[contains(@class,"Order_Form")]//input[contains(@placeholder, "Комментарий для курьера")]')

    BACK_BUTTON = (By.XPATH,'//div[contains(@class,"Order_Buttons")]//button[contains(text(), "Назад")]')
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class,"Order_Buttons")]//button[contains(text(), "Заказать")]')



    @staticmethod
    def rental_time_dropdown(rental_time):
        option_locator = (By.XPATH,
                          f'//div[contains(@class,"Dropdown-menu")]/div[contains(text(), "{rental_time}")]')
        return option_locator

    @staticmethod
    def scooter_color(color):
        option_locator = (By.XPATH,
                          f'//div[contains(@class,"Order_Checkboxes")]//input[@id = "{color}"]')
        return option_locator

class OrderConfirmationLocators:
    CONFIRM_BUTTON_NO = (By.XPATH,'//div[contains(@class,"Order_Modal")]//button[contains(text(), "Нет")]')
    CONFIRM_BUTTON_YES = (By.XPATH, '//div[contains(@class,"Order_Modal")]//button[contains(text(), "Да")]')

class OrderCompleteLocators:
    COMPLETE_HEADER_TEXT = (By.XPATH, '//div[contains(@class,"Order_Modal")]//div[contains(text(), "Заказ оформлен")]')
    COMPLETE_BUTTON_STATUS = (By.XPATH, '//div[contains(@class,"Order_Modal")]//button[contains(text(), "Посмотреть '
                                        'статус")]')
