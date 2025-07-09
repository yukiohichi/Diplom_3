import allure

from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):

    @allure.step('Нажать на ингредиент')
    def click_ingredients_button(self):
        self.check_element_is_clickable(ConstructorLocators.BUN_INGREDIENT)
        self.click_on_element(ConstructorLocators.BUN_INGREDIENT)

    @allure.step('Проверить что детали ингредиента отображаются')
    def is_detail_ingredients_displayed(self):
        return self.check_displaying_of_element(ConstructorLocators.DETAILS_INGREDIENT)


    @allure.step('Проверить, что ингредиенты отображаются')
    def is_ingredients_displayed(self):
        return self.check_displaying_of_element(ConstructorLocators.BUN_INGREDIENT)

    @allure.step('Закрыть модальное окно Ингредиента')
    def click_modal_close_button(self):
        self.check_element_is_clickable(ConstructorLocators.INGREDIENT_MODAL_CLOSE_BUTTON)
        self.click_on_element(ConstructorLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        source = self.wait_and_find_element(ConstructorLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(ConstructorLocators.BURGER_CONSTRUCTOR)

        self.drag_and_drop_element(source, target)

    @allure.step('Проверить что элемент добавлен')
    def is_ingredients_added_to_order(self):
        count = self.get_text_from_element(ConstructorLocators.COUNTER_TWO_BUN)
        return count == '2'

    @allure.step('Нажать на кнопку создания заказа')
    def click_create_order_button(self):
        self.click_on_element(ConstructorLocators.CREATE_ORDER)

    @allure.step('Номер заказа отображается')
    def is_order_identifier_displayed(self):
        return self.check_displaying_of_element(ConstructorLocators.NUMBER_ORDER)

    @allure.step('Cоздать заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_create_order_button()


    @allure.step('Получить номер заказа')
    def get_number_order(self):
        self.check_displaying_of_element(ConstructorLocators.NUMBER_ORDER)
        self.check_no_text_in_element(ConstructorLocators.NUMBER_ORDER, '9999')
        return self.get_text_from_element(ConstructorLocators.NUMBER_ORDER)

    @allure.step('')
    def close_modal_order(self):
        self.click_on_element(ConstructorLocators.ORDER_MODAL_CLOSE_BUTTON)
