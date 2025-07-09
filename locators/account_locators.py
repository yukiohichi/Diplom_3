from selenium.webdriver.common.by import By


class AccountLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    EMAIL_FORGOT_PASSWORD_INPUT = (By.XPATH, '//input[@name="name"]')
    RESTORE_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    FORGOT_PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')
    VISIBILITY_ICON = (By.XPATH,'//div[contains(@class, "input__icon-action")]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
    PASSWORD_FIELD_HIGHLIGHTED = (By.XPATH, '//div[contains(@class, "input_status_active")]')


    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    EMAIL_USER_INPUT = (By.XPATH, '//input[@type="text"]')
    PASSWORD_USER_INPUT = (By.XPATH, '//input[@type="password"]')

    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')

    MAIN_PAGE_HEADER = (By.XPATH, '//h1[text()="Соберите бургер"]')

