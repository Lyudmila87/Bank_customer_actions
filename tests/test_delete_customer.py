import allure
import pytest

from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage
from utils import filter_names_to_delete


@allure.feature("XYZ Bank")
@allure.story("UI")
@allure.title("Удаление клиента")
@allure.description("""
    Цель: Проверить удаление клиента из таблицы

    Предусловие:
        - открыть браузер
        - добавить нового клиента 

    Шаги:
    1. Открытие страницы XYZ bank
    2. Получение списка всех имен
    3. Удаление из таблицы записей по отфильтрованным именам
    
    Постусловие:
        - Закрыть браузер
    
    Ожидаемый результат:
        -  из таблицы удалена запись
    """)
@pytest.mark.ui
def test_delete_customer(driver, add_customer):

    with allure.step("Открытие страницы XYZ bank"):
        manager_page = ManagerPage(driver)
        manager_page.go_to_customers()

    with allure.step("Получение списка всех имен"):
        customer_page = CustomersPage(driver)
        all_names = customer_page.get_names()

    with allure.step("Удаление из таблицы записей по отфильтрованным именам"):
        deleted_names = filter_names_to_delete(all_names)
        customer_page.delete_customers(*deleted_names)
        non_delete = set(all_names).difference(deleted_names)
        assert sorted(customer_page.get_names()) == sorted(non_delete), "В таблице остались лишние записи"
