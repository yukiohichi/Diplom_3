import pytest


from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.account_page import AccountPage
from data.urls import BASE_URL
from pages.constructor_page import ConstructorPage
from pages.navigation import Navigation
from pages.orders_feed_page import OrdersFeedPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        DRIVER_NAME = 'chrome'
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        DRIVER_NAME = 'firefox'
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()

@pytest.fixture()
def account_page(driver):
    account_page = AccountPage(driver)
    account_page.go_to_url(BASE_URL)

    return account_page

@pytest.fixture()
def navigation(driver):
    navigation = Navigation(driver)
    return navigation

@pytest.fixture()
def constructor_page(driver, navigation):
    constructor_page = ConstructorPage(driver)
    navigation.go_to_constructor_page()
    return constructor_page

@pytest.fixture()
def orders_feed_page(driver):
    orders_feed_page = OrdersFeedPage(driver)
    return orders_feed_page


@pytest.fixture()
def authorized_user(account_page, navigation):
    navigation.click_personal_account_button()
    account_page.authorisation_user()
    account_page.is_header_burger_displayed()

    return account_page


@pytest.fixture()
def order(authorized_user, constructor_page):
    constructor_page.create_order()
    order = constructor_page.get_number_order()
    constructor_page.close_modal_order()

    return order

@pytest.fixture()
def completed_counters_before(navigation, orders_feed_page):
    navigation.go_to_feed_order_page()
    return {
        'today': orders_feed_page.get_today_completed_counter(),
        'total': orders_feed_page.get_total_completed_counter(),
    }
