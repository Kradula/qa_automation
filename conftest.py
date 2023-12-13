import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options


@pytest.fixture(scope='function', autouse=True)
def driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
