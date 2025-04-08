from selenium.webdriver.common.by import By


class Locators:
    # кнопка перехода в личный кабинет
    PROFILE_BUTTON = By.XPATH, '//*[contains(@href, "/account")]'
    # ссылка на регистрацию
    REGISTER_LINK = By.XPATH, '//*[contains(@class, "Auth_link")]'
    # инпут для ввода имени в регистрации
    NAME_INPUT = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
    #инпут для ввода почты в регистрации
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    #инпут для ввода пароля в регистрации
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'
    # кнопка отправки формы в регистрации
    CONFIRM_REGISTER_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_medium") and contains(text(), "Зарегистрироваться")]'
    # заголовок страница входа
    LOGIN_PAGE = By.XPATH, '//h2[text()="Вход"]'
    # текст ошибки неправильного пароля в регистрации
    PASSWORD_ERROR_TEXT = By.XPATH, '//p[text()="Некорректный пароль"]'
    # кнопка логина на главной странице
    LOGIN_BUTTON_ON_MAIN_PAGE = By.XPATH, '//*[contains(@class, "button_button_size_large") and text()="Войти в аккаунт"]'
    # кнопка отправки формы логина
    CONFIRM_LOGIN_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_medium") and text()="Войти"]'
    # оформить заказ кнопка на главной
    CREATE_ORDER_BUTTON = By.XPATH, '//*[contains(@class, "button_button_size_large") and text()="Оформить заказ"]'
    # ссылка для логина
    LOGIN_LINK = By.XPATH, '//*[contains(@class, "Auth_link") and text()="Войти"]'
    # ссылка на сброс пароля
    RESET_PASSWORD_LINK = By.XPATH, '//*[contains(@class, "Auth_link") and text()="Восстановить пароль"]'
    # ссылка на профиль
    PROFILE_TITLE_LINK = By.XPATH, '//*[contains(@class, "Account_link_active")]'
    # ссылка на "Конструктор" страницу
    CONSTRUCTOR_LINK = By.XPATH, '//a[@href="/" and .//p[text()="Конструктор"]]'
    # ссылка на главную страницу
    MAIN_LOGO_LINK = By.XPATH, '//a[contains(@href, "/") and contains(@class, "AppHeader_header__link")]'
    # заголовок главной страницы
    MAIN_PAGE_TITLE = By.XPATH, '//*[contains(@class, "text_type_main") and text()="Соберите бургер"]'
    # кнопка логаута
    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button") and text()="Выход"]'
    # вкладка соусы на главной
    SAUCE_TAB = By.XPATH, '//*[contains(@class, "tab_tab") and .//span[text()="Соусы"]]'
    BURGER_BUNS_TAB = By.XPATH, '//*[contains(@class, "tab_tab") and .//span[text()="Булки"]]'
    BURGER_FILLING_TAB = By.XPATH, '//*[contains(@class, "tab_tab") and .//span[text()="Начинки"]]'
