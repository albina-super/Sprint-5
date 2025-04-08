from tests.locators import Locators


class TestConstructorPage:


    def test_go_to_tab_sauces_success(self, chrome):
        tab = chrome.find_element(*Locators.SAUCE_TAB)
        tab.click()
        class_name = tab.get_attribute('class')
        assert 'tab_tab_type_current' in class_name


    def test_go_to_tab_burger_filling_success(self, chrome):
        tab = chrome.find_element(*Locators.BURGER_FILLING_TAB)
        tab.click()
        class_name = tab.get_attribute('class')
        assert 'tab_tab_type_current' in class_name


    def test_go_to_tab_burger_buns_success(self, chrome):
        tab = chrome.find_element(*Locators.SAUCE_TAB)
        tab.click()
        class_name = tab.get_attribute('class')
        assert 'tab_tab_type_current' in class_name
