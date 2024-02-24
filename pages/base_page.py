from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from data.config import WAIT_TIMEOUT, URL


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = URL

    def open(self) -> None:
        self.driver.get(self.url)

    def element_is_visible(self, locator: tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator: tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = WAIT_TIMEOUT) -> list:
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def change_locator(locator_path: tuple, value: str) -> tuple:
        """Принимает кортеж (BY, локатор) для изменения локатора и возвращает обновленный кортеж"""

        new_locator = locator_path[1].format(value)
        return locator_path[0], new_locator

    def switch_to_alert_and_accept(self) -> None:
        self.driver.switch_to.alert.accept()
