import pytest

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import *
#from data import *
#from locators import Locators


#  Подключаем webdriver для Chrome
@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
