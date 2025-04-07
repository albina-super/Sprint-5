from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import EMAIL, PASSWORD
from tests.locators import Locators


class TestMoveToLogosFromProfilePage:

    def test_move_from_profile_to_constructor_success(self, chrome):
        correct_class_name = 'AppHeader_header__link_active'
        chrome.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        constructor_link = chrome.find_element(*Locators.CONSTRUCTOR_LINK)
        constructor_link.click()
        class_name = constructor_link.get_attribute('class')
        assert correct_class_name in class_name


    def test_move_from_profile_to_main_logo_success(self, chrome):
        chrome.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.MAIN_LOGO_LINK).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        assert chrome.find_element(*Locators.MAIN_PAGE_TITLE).text == 'Соберите бургер'


