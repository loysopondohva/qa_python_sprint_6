import pytest

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *

#  Подключаем webdriver для FireFox
@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(main_site)
    yield browser
    browser.quit()
