import allure
import pytest

from data.urls import ORDER_FEED_URL


@allure.epic('Отслеживание заказов')
class TestFeedsOrders:

    @allure.title('Тест отображения деталей заказа')
    def test_details_order_displayed(self, orders_feed_page):
        orders_feed_page.go_to_url(ORDER_FEED_URL)
        orders_feed_page.click_orders_button()

        assert orders_feed_page.is_details_order_displayed(), \
            'Ожидалось успешное открытие модального окна с деталями заказа'


    @allure.title('Тест что заказ из истории есть в общей ленте')
    def test_order_from_history_is_visible_in_feed(self, authorized_user, order, orders_feed_page, navigation):
        navigation.click_personal_account_button()
        navigation.click_history_orders_button()
        history = orders_feed_page.find_order_to_history(order)

        navigation.go_to_feed_order_page()

        feed = orders_feed_page.find_order_to_feed_orders(order)

        assert history == feed, \
            'Ожидалось что заказ из Истории будет в разделе "Лента заказов"'


    @allure.title('Тест номер заказа есть в списке "В работе"')
    def test_order_appears_in_progress_section(self, authorized_user, order, orders_feed_page, navigation):
        navigation.go_to_feed_order_page()
        assert orders_feed_page.find_number_order_list(order), \
            f"Заказ {order} не найден в разделе 'В работе'"


    @pytest.mark.parametrize(
        "counter_key, get_counter_method, title",
        [
            ("today", "get_today_completed_counter",
             'Тест увеличения счётчика "Выполнено за сегодня" после создания заказа'),
            ("total", "get_total_completed_counter", 'Тест на увеличение счетчика "Выполнено за все время"'),
        ],
        ids=["today_counter", "total_counter"]
    )
    def test_completed_counter_increments(
            self,
            authorized_user,
            completed_counters_before,
            orders_feed_page,
            order,
            navigation,
            counter_key,
            get_counter_method,
            title
    ):
        allure.dynamic.title(title)
        navigation.go_to_feed_order_page()
        before = completed_counters_before[counter_key]
        orders_feed_page.wait_for_order_completion(order)
        after = getattr(orders_feed_page, get_counter_method)()

        assert after > before, \
            f"Счётчик '{counter_key}': было {before}, стало {after}, ожидалось {before > after}"
