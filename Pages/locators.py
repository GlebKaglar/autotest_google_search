from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, 'div.a4bIc > input')
    SEARCH_BUTTON = (By.CLASS_NAME, 'gNO89b')


class SearchResultPageLocators():
    CALCULATE_FIELD = (By.CSS_SELECTOR, '.jlkklc > div')
    CALCULATE_MEMORY_STRING = (By.CSS_SELECTOR, 'div.xwgN1d.XSNERd > div > span')
    CALCULATE_RESULT = (By.ID, 'cwos')
    NUM_0 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(5) >td:nth-child(1)')
    DOT = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(5) >td:nth-child(2)')
    EQUALS = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(5) >td:nth-child(3)')
    PLUS = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(5) >td:nth-child(4)')
    NUM_1 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(4) >td:nth-child(1)')
    NUM_2 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(4) >td:nth-child(2)')
    NUM_3 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(4) >td:nth-child(3)')
    MINUS = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(4) >td:nth-child(4)')
    NUM_4 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(3) >td:nth-child(1)')
    NUM_5 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(3) >td:nth-child(2)')
    NUM_6 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(3) >td:nth-child(3)')
    MULT = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(3) >td:nth-child(4)')
    NUM_7 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(2) >td:nth-child(1)')
    NUM_8 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(2) >td:nth-child(2)')
    NUM_9 = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(2) >td:nth-child(3)')
    DIV = (By.CSS_SELECTOR, '.ElumCf > tbody > tr:nth-child(2) >td:nth-child(4)')

