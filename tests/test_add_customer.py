import allure
import pytest

from data.data import Customer
from pages.add_customer_page import AddNewCustomerPage
from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage


@allure.feature("XYZ Bank")
@allure.story('UI')
@allure.title('Создание клиента')
@allure.description("""
    Цель: Проверить создание клиента

    Предусловие:
        - Открыть браузер

    Шаги:
    1. Перейти на страницу XYZ Bank
    2. Нажать кнопку 'Add Customer'
    3. Ввести значение "Post Code", состоящее из любых 10 цифр
    4. Рассчитать и ввести значение "First Name" по следующей формуле:
         - Post Code разбивается на двузначные числа
         - Каждое число преобразовывается в букву английского алфавита по порядку от 0 до 25
    5. Ввести любое значение "Last Name" 
    5. Нажать кнопку 'Add Customer', расположенную под полями для ввода значений
    6. Убедиться, что появилось всплывающее окно с надписью "Customer added successfully with customer id"
    
    Постусловие:
        - Удалить добавленного клиента
        - Закрыть браузер
    
    Ожидаемый результат:
        -  в таблицу добавлен новый клиент
    """)
@pytest.mark.ui
def test_add_customer(driver, delete_customers):

    with allure.step('Открытие страницы XYZ bank'):
        manager_page = ManagerPage(driver)
        manager_page.open()

    with (allure.step('Добавление клиента')):
        manager_page.go_to_add_customer()
        add_customer = AddNewCustomerPage(driver)
        customer = Customer()
        add_customer.fill_customer_form(customer)
        assert "Customer added successfully with customer id" in driver.switch_to.alert.text, "Надпись на всплывающем \
         окне не соответствует ожидаемому результату"

    with allure.step('Убедиться, что добавленный клиент присутствует в таблице'):
        manager_page.switch_to_alert_and_accept()
        manager_page.go_to_customers()
        customer_page = CustomersPage(driver)
        customer_names = customer_page.get_names()
        assert customer.first_name in customer_names, "Добавленный клиент присутствует в таблице"
        delete_customers.append(customer.first_name)
