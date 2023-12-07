import allure
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import *


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Заполняем "Комментарий"')
    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(comment)

    @allure.step('Заполняем "Цвет самоката"')
    def input_color_scooter(self, color):
        elements = self.driver.find_elements(*OrderPageLocators().LIST_COLOR_SCOOTER)
        for element in elements:
            if element.text == color:
                element.click()
                break

    @allure.step('Заполняем "Срок аренды"')
    def input_rental_term(self, rental_term):
        self.driver.find_element(*OrderPageLocators().INPUT_RENTAL_TERM).click()
        elements = self.driver.find_elements(*OrderPageLocators().LIST_RENTAL_TERMS)
        for element in elements:
            if element.text == rental_term:
                element.click()
                break

    @allure.step('Заполняем "Дату доставки"')
    def input_delivery_date(self, date):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE))
        element = self.driver.find_element(*OrderPageLocators.DELIVERY_DATE)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    @allure.step('Заполняем "Имя"')
    def input_buyer_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step('Заполняем "Фамилию"')
    def input_buyer_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем "Адрес"')
    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Заполняем "Станция метро"')
    def input_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO_STATION).send_keys(metro_station)
        elements = self.driver.find_elements(*OrderPageLocators.LIST_METRO_STATIONS)
        assert elements
        for element in elements:
            if element.text == metro_station:
                element.click()
                break

    @allure.step('Нажимаем на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполняем "Телефон"')
    def input_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER).send_keys(phone)

    @allure.step('Ждем пока загрузится страница заказа')
    def wait_load_order_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.SECTION_TEXT))

    @allure.step('Заполняем поля формы заказа')
    def full_order_form(self, buyer_name, buyer_surname, address, metro_station, input_phone, delivery_date, rental_term, color, comment):
        self.wait_load_order_page()
        self.input_buyer_name(buyer_name)
        self.input_buyer_surname(buyer_surname)
        self.input_address(address)
        self.input_metro_station(metro_station)
        self.input_phone(input_phone)
        self.click_next_button()
        self.input_delivery_date(delivery_date)
        self.input_rental_term(rental_term)
        self.input_color_scooter(color)
        self.input_comment(comment)

    @allure.step('Получает текст сообщения об успешном оформлении заказ')
    def get_success_order_message(self):
        return(self.driver.find_element(*OrderPageLocators.SUCCESS_ORDER_MESSAGE).text)

    @allure.step('Нажимаем кнопку "Да" в форме подтверждения заказа')
    def click_order_button_yes(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    @allure.step('Нажимаем кнопку "Посмотреть статус"')
    def click_view_status_button_yes(self):
        self.driver.find_element(*OrderPageLocators.VIEW_STATUS_BUTTON).click()