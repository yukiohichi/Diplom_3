import allure


@allure.epic('Конструктор бургера')
class TestConstructor:

    @allure.title('Проверка появления всплывающего окна с деталями')
    def test_details_ingredients(self, constructor_page):
        constructor_page.click_ingredients_button()
        assert constructor_page.is_detail_ingredients_displayed(), \
            'Ожидалось, что появится поле с деталями заказа'


    @allure.title('Проверка закрытия всплывающего окна')
    def test_modal_ingredients_close(self, constructor_page):
        constructor_page.click_ingredients_button()
        constructor_page.is_detail_ingredients_displayed()
        constructor_page.click_modal_close_button()

        assert constructor_page.is_ingredients_displayed(), \
            'Ожидалось, что модальное окно закроется'


    @allure.title('Проверка добавления ингредиента в заказ')
    def test_ingredient_counter_increases_on_add(self, constructor_page):
        constructor_page.add_ingredient_to_order()

        assert constructor_page.is_ingredients_added_to_order(), \
            'Ожидалось, что ингредиент добавится'


    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_create_order(self, constructor_page, authorized_user):
        constructor_page.add_ingredient_to_order()
        constructor_page.click_create_order_button()

        assert constructor_page.is_order_identifier_displayed(), \
            'Ожидалось успешное создание заказа'
