import time

from selenium.common import NoSuchElementException

from .locators import BasePageLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def search(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_FIELD), 'SEARCH_FIELD not found'
        search_field = self.driver.find_element(*BasePageLocators.SEARCH_FIELD)
        print('Вводим поисковый запрос')
        search_field.send_keys('Калькулятор')
        assert self.is_element_present(*BasePageLocators.SEARCH_BUTTON), 'SEARCH_BUTTON not found'
        search_button = self.driver.find_element(*BasePageLocators.SEARCH_BUTTON)
        print('Нажимаем на поиск')
        search_button.click()
        time.sleep(2)