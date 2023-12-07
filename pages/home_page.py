import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import *


class HomePageScooter:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку "Заказать" в заголовке главной страницы')
    def click_on_order_button_header(self):
        element = self.driver.find_element(*HomePageScooterLocators.ORDER_BUTTON_HEADER)
        element.click()

    @allure.step('Нажимаем кнопку "Заказать" внизу главной страницы')
    def click_on_order_button_bottom(self):
        element = self.driver.find_element(*HomePageScooterLocators.ORDER_BUTTON_BOTTOM)
        element.location_once_scrolled_into_view
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(element))
        element.click()

    @allure.step('Нажимаем на вопрос')
    def click_on_question(self, question):
        self.driver.find_element(*HomePageScooterLocators.CLOSE_BUTTON_COOKIE).click()
        elements = self.driver.find_elements(*HomePageScooterLocators.QUESTIONS)
        for element in elements:
            if element.text == question:
                element.location_once_scrolled_into_view
                WebDriverWait(self.driver, 15).until(
                    expected_conditions.element_to_be_clickable(element))
                element.click()
                break

    @allure.step('Ждем пока загрузится ответ')
    def wait_load_answer(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(HomePageScooterLocators.ANSWER))

    @allure.step('Получаем текст ответа')
    def get_text_answer(self):
        return(self.driver.find_element(*HomePageScooterLocators.ANSWER).text)

    @allure.step('Ждем пока загрузится главная страница')
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(HomePageScooterLocators.IMG_SCOOTER))

    @allure.step('Нажимаем на логотим Самокат')
    def click_on_logo_scooter(self):
        self.driver.find_element(*HomePageScooterLocators.LOGO_SCOOTER).click()

    @allure.step('Нажимаем на логотип Яндекс')
    def click_on_logo_yandex(self):
        self.driver.find_element(*HomePageScooterLocators.LOGO_YANDEX).click()

    @allure.step('Переключается на новое окно')
    def switch_on_new_window(self, original_window, new_url):
        all_windows = self.driver.window_handles
        new_window = None
        for window in all_windows:
            if window != original_window:
                new_window = window
                break
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(new_url))