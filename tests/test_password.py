import allure

from data.urls import FORGOT_PASSWORD_URL

@allure.epic('Восстановление пароля')
class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_forgot_password_redirect(self, account_page, navigation):
        navigation.click_personal_account_button()
        account_page.click_forgot_password_button()
        expected_url = FORGOT_PASSWORD_URL
        actual_url = account_page.get_current_url()
        assert actual_url == expected_url, \
            f"Ожидался переход на {expected_url}, но текущий URL: {actual_url}"


    @allure.title('Проверка ввода почты и нажатия на кнопку «Восстановить»')
    def test_password_recovery_with_email_input(self, account_page, navigation):
        navigation.click_personal_account_button()
        account_page.click_forgot_password_button()

        account_page.enter_email()
        account_page.click_restore_password_button()

        assert account_page.is_save_button_displayed(), \
            'Ожидался переход на страницу восстановления пароля'

    @allure.title('Проверка активации поля пароля после нажатия на иконку активации')
    def test_toggle_password_field_visibility(self, account_page, navigation):
        navigation.go_to_forgot_page()

        account_page.enter_email()
        account_page.click_restore_password_button()

        account_page.is_save_button_displayed()
        account_page.enter_password()
        account_page.click_on_visibility_icon()

        assert account_page.is_password_field_highlighted(), \
            'Ожидалось, что поле пароля подсветится'
