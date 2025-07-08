import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти по адресу: {url}')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    @allure.step('Проверить, что текста нет в элементе')
    def check_no_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, 15).until_not(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step('Проверить что текст есть в элементе')
    def check_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()


    @allure.step('Найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Добавить текст')
    def enter_text_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        text = element.text.strip()
        return text

    @allure.step('Вернуть текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Найти все элементы на странице')
    def find_all_element(self, locator):
        all_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator))
        return all_number

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)
