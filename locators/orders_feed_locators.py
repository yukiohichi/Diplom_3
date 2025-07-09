
from selenium.webdriver.common.by import By

class OrdersFeedLocators:

    READY_ORDERS_HEADER = (By.XPATH, '//p[text()="Готовы:"]')

    ORDER_FEED_NUMBER = (By.XPATH, '//p[contains(@class, "text_type_digits-default") and starts-with(normalize-space(.), "#0")]')

    ORDER_DETAILS_HEADER = (By.XPATH, '//p[text()="Cостав"]')

    ORDER_HISTORY_NUMBER = (By.XPATH, '//p[contains(text(), "#")]')

    IN_PROGRESS_ORDERS_LIST = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li')

    TODAY_DONE_COUNT = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/parent::*//p[contains(@class, "text_type_digits")]')

    TOTAL_DONE_COUNT = (By.XPATH, '//p[text()="Выполнено за все время:"]/parent::*//p[contains(@class, "text_type_digits")]')
