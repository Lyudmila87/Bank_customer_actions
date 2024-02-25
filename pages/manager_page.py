from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ManagerPage(BasePage):

    ADD_CUSTOMER_BUTTON_MANE = (By.XPATH, "//button[@ng-click='addCust()']")
    CUSTOMERS_BUTTON = (By.XPATH, "//button[@ng-click='showCust()']")

    def go_to_add_customer(self) -> None:
        self.element_is_clickable(self.ADD_CUSTOMER_BUTTON_MANE).click()

    def go_to_customers(self) -> None:
        self.element_is_clickable(self.CUSTOMERS_BUTTON).click()
