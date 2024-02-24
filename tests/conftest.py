import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from data.data import Customer
from pages.add_customer_page import AddNewCustomerPage
from pages.manager_page import ManagerPage
from pages.customers_page import CustomersPage


@pytest.fixture()
def driver() -> WebDriver:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.fixture()
def add_customer(driver) -> Customer:
    page = ManagerPage(driver)
    page.open()
    page.go_to_add_customer()
    add_customer_page = AddNewCustomerPage(driver)
    customer = Customer()
    add_customer_page.fill_customer_form(customer)
    page.switch_to_alert_and_accept()
    return customer


@pytest.fixture()
def delete_customers(driver) -> list:
    customers_to_delete = []
    yield customers_to_delete
    CustomersPage(driver).delete_customers(*customers_to_delete)
