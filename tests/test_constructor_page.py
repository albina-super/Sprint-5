from tests.locators import Locators


class TestConstructorPage:


    def test_go_to_tab_sauces_success(self, chrome):
        chrome.find_element(*Locators.SAUCE_TAB).click()
        header = chrome.find_element(*Locators.SAUCE_TITLE).text
        assert header == 'Соусы'


    def test_go_to_tab_burger_filling_success(self, chrome):
        chrome.find_element(*Locators.BURGER_FILLING_TAB).click()
        header = chrome.find_element(*Locators.BURGER_FILLING_TITLE).text
        assert header == 'Начинки'


    def test_go_to_tab_burger_buns_success(self, chrome):
        chrome.find_element(*Locators.SAUCE_TAB).click()
        chrome.find_element(*Locators.BURGER_BUNS_TAB).click()
        header = chrome.find_element(*Locators.BURGER_BUNS_TITLE).text
        assert header == 'Булки'
