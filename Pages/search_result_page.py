import time

from .base_page import BasePage
from .locators import SearchResultPageLocators


class SearchResultPage(BasePage):  # 1*2-3+1
    def calculate(self):
        print('Вводим выражение')
        num_1 = self.driver.find_element(*SearchResultPageLocators.NUM_1)
        num_2 = self.driver.find_element(*SearchResultPageLocators.NUM_2)
        num_3 = self.driver.find_element(*SearchResultPageLocators.NUM_3)
        mult = self.driver.find_element(*SearchResultPageLocators.MULT)
        minus = self.driver.find_element(*SearchResultPageLocators.MINUS)
        plus = self.driver.find_element(*SearchResultPageLocators.PLUS)
        equals = self.driver.find_element(*SearchResultPageLocators.EQUALS)
        num_1.click()
        mult.click()
        num_2.click()
        minus.click()
        num_3.click()
        plus.click()
        num_1.click()
        equals.click()
        memory_string = self.driver.find_element(*SearchResultPageLocators.CALCULATE_MEMORY_STRING).text
        assert memory_string == '1 × 2 - 3 + 1 =', 'Memory string memory does not match'
        print('ОР_1 = ФР_1')
        answer = self.driver.find_element(*SearchResultPageLocators.CALCULATE_RESULT).text
        assert answer == '0', 'Answer is wrong'
        print('ОР_2 = ФР_2')
        time.sleep(3)
