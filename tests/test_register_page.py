from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.data import NAME
from tests.locators import Locators
from helpers import generate_email, generate_password


class TestRegisterPage:

    def test_register_success(self, chrome):
        password = generate_password(8)
        email = generate_email()
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.REGISTER_LINK).click()
        chrome.find_element(*Locators.NAME_INPUT).send_keys(NAME)
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        chrome.find_element(*Locators.CONFIRM_REGISTER_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.LOGIN_PAGE)
        )
        assert chrome.find_element(*Locators.LOGIN_PAGE).text == "Вход"

    def test_register_bad_password(self, chrome):
        password = generate_password(5)
        email = generate_email()
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        chrome.find_element(*Locators.REGISTER_LINK).click()
        chrome.find_element(*Locators.NAME_INPUT).send_keys(NAME)
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        chrome.find_element(*Locators.CONFIRM_REGISTER_BUTTON).click()
        assert chrome.find_element(*Locators.PASSWORD_ERROR_TEXT).text == "Некорректный пароль"
