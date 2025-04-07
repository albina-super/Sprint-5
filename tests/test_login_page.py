from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import chrome
from tests.data import EMAIL, PASSWORD
from tests.locators import Locators


class TestLoginPage:

    def test_login_from_main_page_success(self, chrome):
        chrome.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.CREATE_ORDER_BUTTON)
        )
        assert chrome.find_element(*Locators.CREATE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_login_from_profile_success(self, chrome):
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.CREATE_ORDER_BUTTON)
        )
        assert chrome.find_element(*Locators.CREATE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_login_from_register_form_success(self, chrome):
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.REGISTER_LINK).click()
        chrome.find_element(*Locators.LOGIN_LINK).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.CREATE_ORDER_BUTTON)
        )
        assert chrome.find_element(*Locators.CREATE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_login_from_reset_password_success(self, chrome):
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.RESET_PASSWORD_LINK).click()
        chrome.find_element(*Locators.LOGIN_LINK).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.CREATE_ORDER_BUTTON)
        )
        assert chrome.find_element(*Locators.CREATE_ORDER_BUTTON).text == 'Оформить заказ'
