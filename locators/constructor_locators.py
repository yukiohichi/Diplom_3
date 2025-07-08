from selenium.webdriver.common.by import By

class ConstructorLocators:

    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')
    DETAILS_INGREDIENT = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified") and ancestor::section[contains(@class, "Modal_modal_opened")]]')
    COUNTER_TWO_BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a//p[contains(@class, "counter__num") and text()="2"]')
    CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
    NUMBER_ORDER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')
