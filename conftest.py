import pytest
from selenium import webdriver
from urls import home_page_url


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(home_page_url)
    yield driver
    driver.quit()

