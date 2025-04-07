import pytest
from selenium import webdriver

from tests.data import URL


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.quit()
