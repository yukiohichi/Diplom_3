from selenium.webdriver.common.by import By


class NavigationLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')

    HISTORY_ORDERS_BUTTON = (By.XPATH, '//a[text()="История заказов"]')

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')

    LIST_ORDERS_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')

    PROFILE_USER_BUTTON = (By.XPATH, '//a[text()="Профиль"]')

    ORDER_HISTORY_LIST = (By.XPATH, '//div[contains(@class, "OrderHistory_orderHistory")]')

    READY_ORDERS = (By.XPATH, '//p[text()="Готовы:"]')

    HEADER_TAKE_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')