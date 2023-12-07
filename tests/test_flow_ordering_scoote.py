import allure
import pytest
from pages.home_page import HomePageScooter
from pages.order_page import OrderPage
from data import order_details_1, order_details_2
from urls import *


class TestFlowOrderingScooter:
    @allure.title('Проверка заказа самоката с помощью кнопки вверху страницы.')
    @allure.description(' Проверяем весь флоу позитивного сценария')
    @pytest.mark.parametrize('buyer_name, buyer_surname, address, metro_station, input_phone, delivery_date, '
                             'rental_term, color, comment', order_details_1)
    def test_flow_ordering_scootert_by_button_header(self, driver, buyer_name, buyer_surname, address, metro_station
                                                     , input_phone, delivery_date, rental_term, color, comment):
        hp = HomePageScooter(driver)
        hp.wait_for_load_home_page()
        hp.click_on_order_button_header()

        op = OrderPage(driver)
        op.full_order_form(buyer_name, buyer_surname, address, metro_station, input_phone, delivery_date, rental_term
                           , color, comment)
        op.click_order_button()

        op.click_order_button_yes()
        assert 'Заказ оформлен' in op.get_success_order_message()

        op.click_view_status_button_yes()

        hp.click_on_logo_scooter()
        assert driver.current_url == home_page_url

        original_window = driver.current_window_handle
        hp.click_on_logo_yandex()
        hp.switch_on_new_window(original_window, dzen_page_url)
        assert driver.current_url == dzen_page_url
        driver.switch_to.window(original_window)

    @allure.title('Проверка заказа самоката с помощью кнопки внизу страницы.')
    @allure.description(' Проверяем весь флоу позитивного сценария')
    @pytest.mark.parametrize('buyer_name, buyer_surname, address, metro_station, input_phone, delivery_date,'
                             ' rental_term, color, comment', order_details_2)
    def test_flow_ordering_scootert_by_button_bottom(self, driver, buyer_name, buyer_surname, address, metro_station,
                                                     input_phone, delivery_date, rental_term, color, comment):
        hp = HomePageScooter(driver)
        hp.wait_for_load_home_page()
        hp.click_on_order_button_bottom()

        op = OrderPage(driver)
        op.full_order_form(buyer_name, buyer_surname, address, metro_station, input_phone, delivery_date, rental_term,
                           color, comment)
        op.click_order_button()

        op.click_order_button_yes()
        assert 'Заказ оформлен' in op.get_success_order_message()

        op.click_view_status_button_yes()

        hp.click_on_logo_scooter()
        assert driver.current_url == home_page_url

        original_window = driver.current_window_handle
        hp.click_on_logo_yandex()
        hp.switch_on_new_window(original_window, dzen_page_url)
        assert driver.current_url == dzen_page_url
        driver.switch_to.window(original_window)