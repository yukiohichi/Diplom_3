import allure

from conftest import account_page

allure.epic('Управление аккаунтом')
class TestAccount:

    @allure.title('Проверка авторизации пользователя')
    def test_authorisation_user(self, account_page, navigation):
        navigation.go_to_constructor_page()
        navigation.click_personal_account_button()
        account_page.authorisation_user()

        assert account_page.is_header_burger_displayed(), \
            'Ожидалась успешная авторизация'


    @allure.title('Проверка успешного выхода пользователя из аккаунта')
    def test_exit_account(self, authorized_user, navigation):
        navigation.click_personal_account_button()
        authorized_user.click_exit_account_button()

        assert authorized_user.is_login_button_displayed(), \
            'Ожидался успешный выход из системы'

