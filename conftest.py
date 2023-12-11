import pytest
from selenium import webdriver
from urls import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.home_page_url)
    yield driver
    driver.quit()

