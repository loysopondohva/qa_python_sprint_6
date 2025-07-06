import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    @allure.step("Подождать присутствия элемента")
    def wait_for_presence_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_visible_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Перейти на другую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получить текущий url страницы")
    def get_page_url(self):
        return self.driver.current_url

    # @allure.step("Получить заголовок страницы")
    # def get_page_title(self):
    #     self.wait_for_presence_element(MainPageLocators.PAGE_TITLE)
    #     return self.driver.title