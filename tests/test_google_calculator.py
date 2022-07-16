from ..Pages.base_page import BasePage
from ..Pages.search_result_page import SearchResultPage


def test_calculate(driver):
    print('Запуск теста')
    base_page = BasePage(driver)
    base_page.search()
    search_result_page = SearchResultPage(driver)
    search_result_page.calculate()
