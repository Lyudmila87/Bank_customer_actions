import allure
import pytest

from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage


@allure.feature('XYZ Bank')
@allure.story('UI')
@allure.title('Сортировка клиентов по имени в обратном алфавитном порядке')
@allure.description("""
    Цель: Проверить сортировку имен в обратном алфавитном порядке

    Предусловие:
        - открыть браузер
        - добавить нового клиента 

    Шаги:
    1. Перейти на страницу XYZ Bank
    2. Нажать кнопку 'Customers'
    3. Нажать на гиперссылку 'First Name'
    4. Убедиться, что значения отсортированы в обратном алфавитном порядке
    
    Постусловие:
        - Удалить добавленного клиента
        - Закрыть браузер
    
    Ожидаемый результат:
        -  в колонке First Name значения сортируются в обратном алфавитном порядке
    """)
@pytest.mark.ui
def test_sort_customers_direct(driver, add_customer, delete_customers):

    with allure.step('Открытие страницы XYZ bank, добавление нового клиента, переход на страницу с клиентами'):
        page = ManagerPage(driver)
        page.go_to_customers()

    with allure.step('Сортировка клиентов по имени в обратном алфавитном порядке'):
        sort_customers = CustomersPage(driver)
        names_not_sorted = sort_customers.get_names()
        sort_customers.sort_customers_by_first_name()
        sorted_names = sort_customers.get_names()
        assert sorted(names_not_sorted, reverse=True) == sorted_names, 'Имена отсортированы неверно'
        delete_customers.append(add_customer.first_name)


@allure.feature('XYZ Bank')
@allure.story('UI')
@allure.title('Сортировка клиентов по имени в алфавитном порядке')
@allure.description("""
    Цель: Проверить сортировку имен в прямом алфавитном порядке

    Предусловие:
        - открыть браузер
        - добавить нового клиента 

    Шаги:
    1. Перейти на страницу XYZ Bank
    2. Нажать кнопку 'Customers'
    3. Нажать на гиперссылку 'First Name'
    4. Повторно нажать на гиперссылку 'First Name'
    5. Убедиться, что значения отсортированы в алфавитном порядке 

    Постусловие:
        - Удалить добавленного клиента
        - Закрыть браузер

    Ожидаемый результат:
        -  в колонке First Name значения сортируются в прямом алфавитном порядке
    """)
@pytest.mark.ui
def test_sort_customers_reverse(driver, add_customer, delete_customers):
    with allure.step('Открытие страницы XYZ bank, добавление нового клиента, переход на страницу с клиентами'):
        page = ManagerPage(driver)
        page.go_to_customers()

    with allure.step('Сортировка клиентов по имени в алфавитном порядке'):
        sort_customers = CustomersPage(driver)
        names_to_sort = sort_customers.get_names()
        sort_customers.sort_customers_by_first_name()
        sort_customers.sort_customers_by_first_name()
        sorted_names = sort_customers.get_names()
        assert sorted(names_to_sort) == sorted_names, 'Имена отсортированы неверно'
        delete_customers.append(add_customer.first_name)
