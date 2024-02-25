import allure
import pytest

from data.data import Customer
from pages.add_customer_page import AddNewCustomerPage
from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage


@allure.feature("XYZ Bank")
@allure.story("UI")
@allure.title("Создание клиента")
@allure.description("""
    Цель: Проверить создание клиента

    Предусловие:
        - Открыть браузер

    Шаги:
    1. Открытие страницы XYZ bank
    2. Добавление клиента
    3. Убеждение, что добавленный клиент присутствует в таблице
    
    Постусловие:
        - Удалить добавленного клиента
        - Закрыть браузер
    
    Ожидаемый результат:
        -  в таблицу добавлен новый клиент
    """)
@pytest.mark.ui
def test_add_customer(driver, delete_customers):

    with allure.step("Открытие страницы XYZ bank"):
        manager_page = ManagerPage(driver)
        manager_page.open()

    with (allure.step("Добавление клиента")):
        manager_page.go_to_add_customer()
        add_customer_page = AddNewCustomerPage(driver)
        customer = Customer()
        add_customer_page.fill_customer_form(customer)
        assert "Customer added successfully with customer id" in add_customer_page.get_text_from_alert_window(),\
            "Надпись на всплывающем окне не соответствует ожидаемому результату"

    with allure.step("Убеждение, что добавленный клиент присутствует в таблице"):
        manager_page.switch_to_alert_and_accept()
        manager_page.go_to_customers()
        customer_page = CustomersPage(driver)
        customer_names = customer_page.get_names()
        assert customer.first_name in customer_names, "Добавленный клиент присутствует в таблице"
        delete_customers.append(customer.first_name)
