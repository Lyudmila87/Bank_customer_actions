from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CustomersPage(BasePage):

    COLUMN_FIRST_NAME = (By.XPATH, "//a[contains(@ng-click, 'fName')]")
    NAMES = (By.XPATH, "//tr[contains(@ng-repeat, 'cust in Customers')]/td[@class='ng-binding'][1]")
    NAME_TO_DELETE = (By.XPATH, ".//td[text()='{}']/parent::tr//button[@ng-click='deleteCust(cust)']")

    def sort_customers_by_first_name(self) -> None:
        self.element_is_clickable(self.COLUMN_FIRST_NAME).click()

    def get_names(self) -> list:
        result_list = self.elements_are_visible(self.NAMES)
        result_text = [item.text for item in result_list]
        return result_text

    def delete_customers(self, *names) -> None:
        for name in names:
            element = self.element_is_present(self.change_locator(self.NAME_TO_DELETE, name))
            self.driver.execute_script(
                "arguments[0].scrollIntoView({ block: 'center', inline: 'center' })", element)
            element.click()



