import allure

from data.base import EMAIL, PASSWORD
from pages.base_page import BasePage
from locators.account_locators import AccountLocators

class AccountPage(BasePage):

    @allure.step('Нажать на кнопку "Восстановление пароля"')
    def click_forgot_password_button(self):
        self.click_on_element(AccountLocators.FORGOT_PASSWORD_BUTTON)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_restore_password_button(self):
        self.click_on_element(AccountLocators.RESTORE_BUTTON)

    @allure.step('Нажать на иконку видимости пароля')
    def click_on_visibility_icon(self):
        self.click_on_element(AccountLocators.VISIBILITY_ICON)


    @allure.step('Нажать на кнопку "Выход из аккаунта"')
    def click_exit_account_button(self):
        self.check_displaying_of_element(AccountLocators.EXIT_BUTTON)
        self.click_on_element(AccountLocators.EXIT_BUTTON)

    # --методы ввода--
    @allure.step('Ввести email в поле')
    def enter_email(self):
        self.enter_text_to_element(AccountLocators.EMAIL_FORGOT_PASSWORD_INPUT, EMAIL)

    @allure.step('Ввести пароль в поле')
    def enter_password(self):
        self.enter_text_to_element(AccountLocators.FORGOT_PASSWORD_INPUT, PASSWORD)

    # --методы проверки--
    @allure.step('Проверить отображение кнопки "Сохранить"')
    def is_save_button_displayed(self):
        return self.check_displaying_of_element(AccountLocators.SAVE_BUTTON)

    @allure.step('Проверить, что поле пароля подсвечено')
    def is_password_field_highlighted(self):
        return self.check_displaying_of_element(AccountLocators.PASSWORD_FIELD_HIGHLIGHTED)

    @allure.step('Проверить отображение кнопки "Вход"')
    def is_login_button_displayed(self):
        return self.check_displaying_of_element(AccountLocators.LOGIN_BUTTON)


    @allure.step('Авторизация пользователя')
    def authorisation_user(self):
        self.check_displaying_of_element(AccountLocators.EMAIL_USER_INPUT)
        self.enter_text_to_element(AccountLocators.EMAIL_USER_INPUT, EMAIL)
        self.enter_text_to_element(AccountLocators.PASSWORD_USER_INPUT, PASSWORD)
        self.click_on_element(AccountLocators.LOGIN_BUTTON)

    @allure.step('Проверить отображение заголовка на главной странице')
    def is_header_burger_displayed(self):
       return self.check_displaying_of_element(AccountLocators.MAIN_PAGE_HEADER)
