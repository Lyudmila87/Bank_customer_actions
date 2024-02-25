from selenium.webdriver.common.by import By

from data.data import Customer
from pages.base_page import BasePage


class AddNewCustomerPage(BasePage):

    FIRST_NAME_INPUT = (By.XPATH, "//input[@ng-model='fName']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@ng-model='lName']")
    POST_CODE_INPUT = (By.XPATH, "//input[@ng-model='postCd']")
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_customer_form(self, customer: Customer) -> None:
        self.element_is_visible(self.POST_CODE_INPUT).send_keys(customer.post_code)
        self.element_is_visible(self.FIRST_NAME_INPUT).send_keys(customer.first_name)
        self.element_is_visible(self.LAST_NAME_INPUT).send_keys(customer.last_name)
        self.element_is_clickable(self.ADD_CUSTOMER_BUTTON).click()
