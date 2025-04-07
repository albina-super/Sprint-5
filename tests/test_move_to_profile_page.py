from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import PASSWORD, EMAIL
from tests.locators import Locators


class TestMoveToProfilePage:

    def test_move_to_profile_success(self, chrome):
        chrome.find_element(*Locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        chrome.find_element(*Locators.EMAIL_INPUT).send_keys(EMAIL)
        chrome.find_element(*Locators.PASSWORD_INPUT).send_keys(PASSWORD)
        chrome.find_element(*Locators.CONFIRM_LOGIN_BUTTON).click()
        chrome.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(chrome, 10).until(
            expected_conditions.presence_of_element_located(Locators.PROFILE_TITLE_LINK)
        )
        element = chrome.find_element(*Locators.PROFILE_TITLE_LINK)
        assert element.text == 'Профиль'

