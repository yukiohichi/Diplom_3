import allure

from data.urls import BASE_URL, ORDER_FEED_URL, FORGOT_PASSWORD_URL
from pages.base_page import BasePage
from locators.navigation_locators import NavigationLocators


class Navigation(BasePage):

    @allure.step('Переход на главную страницу "Конструктор"')
    def go_to_constructor_page(self):
        self.go_to_url(BASE_URL)

    @allure.step('Переход на страницу Ленты заказов')
    def go_to_feed_order_page(self):
        self.go_to_url(ORDER_FEED_URL)

    @allure.step('Перейти на страницу восстановления пароля')
    def go_to_forgot_page(self):
        self.go_to_url(FORGOT_PASSWORD_URL)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.check_displaying_of_element(NavigationLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(NavigationLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_orders_button(self):
        self.click_on_element(NavigationLocators.HISTORY_ORDERS_BUTTON)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_list_orders_button(self):
        self.check_displaying_of_element(NavigationLocators.LIST_ORDERS_BUTTON)
        self.click_on_element(NavigationLocators.LIST_ORDERS_BUTTON)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructions_button(self):
        self.check_displaying_of_element(NavigationLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(NavigationLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверить отображение кнопки "Профиль"')
    def is_profile_user_displayed(self):
        return self.check_displaying_of_element(NavigationLocators.PROFILE_USER_BUTTON)

    @allure.step('Проверить отображение списка заказов')
    def is_order_list_displayed(self):
        return self.check_displaying_of_element(NavigationLocators.ORDER_HISTORY_LIST)

    @allure.step('Проверить, что готовность отображается')
    def is_ready_orders_displayed(self):
        return self.check_displaying_of_element(NavigationLocators.READY_ORDERS)

    @allure.step('Проверить отображение заголовка на главной странице')
    def is_header_burger_displayed(self):
        return self.check_displaying_of_element(NavigationLocators.HEADER_TAKE_BURGER)