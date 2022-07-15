import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    url = 'https://www.google.com/'
    print('\nStart Chrome browser for test...')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # убирает ненужные системные логи варнинги (usb/ssl)
    driver = webdriver.Chrome(options=options)
    print('\nStart Google search page')
    driver.get(url)
    driver.implicitly_wait(5)
    yield driver
    print('\nQuit browser')
    driver.quit()
