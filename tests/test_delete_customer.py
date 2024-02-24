import allure
import pytest

from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage
from utils import filter_names_to_delete


@allure.feature("XYZ Bank")
@allure.story('UI')
@allure.title('Удаление клиента')
@allure.description("""
    Цель: Проверить удаление клиента из таблицы

    Предусловие:
        - открыть браузер
        - добавить нового клиента 

    Шаги:
    1. Перейти на страницу XYZ Bank
    2. Нажать кнопку 'Customers'
    3. Определить имена для удаления, согласно алгоритма:
        - Получить из таблицы Customers список имен 
        - Узнать длину каждого имени
        - Найти среднее арифметическое получившихся длин 
        - Удалить клиента с тем именем, у которого длина будет ближе к среднему арифметическому
    4. Убедиться, что после удаления в таблице остались записи, которые не попали под условия алгоритма
    
    Постусловие:
        - Закрыть браузер
    
    Ожидаемый результат:
        -  из таблицы удалена запись
    """)
@pytest.mark.ui
def test_delete_customer(driver, add_customer):

    with allure.step('Открытие страницы XYZ bank, добавление нового клиента, переход на страницу с клиентами'):
        page = ManagerPage(driver)
        page.go_to_customers()

    with allure.step('Получение списка всех имен'):
        customer_page = CustomersPage(driver)
        all_names = customer_page.get_names()

    with allure.step('Удаление из таблицы записей по отфильтрованным именам'):
        deleted_names = filter_names_to_delete(all_names)
        customer_page.delete_customers(*deleted_names)
        non_delete = set(all_names).difference(deleted_names)
        assert sorted(customer_page.get_names()) == sorted(non_delete), 'В таблице остались лишние записи'


