from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import chrome
from tests.data import EMAIL, PASSWORD
from tests.locators import Locators


class TestLogoutPage:

    def test_logout_success(self, chrome):
        chrome.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.element_to_be_clickable(Locators.PROFILE_BUTTON)
        )
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.LOGOUT_BUTTON)
        )
        chrome.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.LOGIN_PAGE)
        )
        assert chrome.find_element(*Locators.LOGIN_PAGE).text == "Вход"
