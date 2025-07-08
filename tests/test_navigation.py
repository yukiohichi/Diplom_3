import allure


@allure.epic('Навигация по сайту')
class TestNavigation:
    @allure.title('Переход в "Личный кабинет" по нажатию на кнопку')
    def test_personal_account_button(self, authorized_user, navigation):
        navigation.go_to_constructor_page()
        navigation.click_personal_account_button()

        assert navigation.is_profile_user_displayed()


    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_history_orders_user(self, authorized_user, navigation):
        navigation.click_personal_account_button()
        navigation.is_profile_user_displayed()
        navigation.click_history_orders_button()

        assert navigation.is_order_list_displayed, \
            'Ожидался успешный переход на страницу "Истории заказов"'


    @allure.title('Проверка перехода в раздел "Конструктор"')
    def test_redirect_constructions_page(self, navigation):
        navigation.go_to_feed_order_page()
        navigation.click_constructions_button()

        assert navigation.is_header_burger_displayed(), \
            'Ожидался успешный переход в раздел "Конструктор"'


    @allure.title('Проверка перехода в раздел "Лента Заказов"')
    def test_redirect_feed_page(self, navigation):
        navigation.go_to_constructor_page()
        navigation.click_list_orders_button()

        assert navigation.is_ready_orders_displayed(), \
            'Ожидался успешный переход в раздел "Ленты заказа"'
