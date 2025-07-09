import allure

from pages.base_page import BasePage
from locators.orders_feed_locators import OrdersFeedLocators
from data.urls import ORDER_HISTORY_URL, ORDER_FEED_URL


class OrdersFeedPage(BasePage):

    @allure.step('Проверить, что готовность отображается')
    def is_ready_orders_displayed(self):
        return self.check_displaying_of_element(OrdersFeedLocators.READY_ORDERS_HEADER)


    @allure.step('Кликнуть на заказ')
    def click_orders_button(self):
        self.click_on_element(OrdersFeedLocators.ORDER_FEED_NUMBER)

    @allure.step('Поиск элемента в списке "В работе"')
    def find_number_order_list(self, text):
        return self.check_text_in_element(OrdersFeedLocators.IN_PROGRESS_ORDERS_LIST, text)

    @allure.step('Проверить отображение деталей заказа')
    def is_details_order_displayed(self):
        return self.check_displaying_of_element(OrdersFeedLocators.ORDER_DETAILS_HEADER)

    @allure.step('Проверить наличие заказа в истории')
    def find_order_to_history(self, number):
        display_order_elements = self.find_all_element(OrdersFeedLocators.ORDER_HISTORY_NUMBER)
        order_number = f'#0{number}'
        return any(el.text.strip() == order_number for el in display_order_elements)

    @allure.step('Проверить наличие заказа в списке заказов')
    def find_order_to_feed_orders(self, number):
        display_order_elements = self.find_all_element(OrdersFeedLocators.ORDER_FEED_NUMBER)
        order_number = f'#0{number}'
        return any(el.text.strip() == order_number for el in display_order_elements)

    @allure.step('Получение количества завершённых заказов за сегодня')
    def get_today_completed_counter(self):
        return int(self.get_text_from_element(OrdersFeedLocators.TODAY_DONE_COUNT))

    @allure.step('Получение общего количества завершённых заказов')
    def get_total_completed_counter(self):
        return int(self.get_text_from_element(OrdersFeedLocators.TOTAL_DONE_COUNT))

    @allure.step('')
    def wait_for_order_completion(self, order_number):
        return self.check_no_text_in_element(OrdersFeedLocators.IN_PROGRESS_ORDERS_LIST, order_number)







