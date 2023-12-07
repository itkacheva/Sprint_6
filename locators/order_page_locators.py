from selenium.webdriver.common.by import By


class OrderPageLocators:
    SECTION_TEXT = [By.XPATH, ".//*[contains(@class,'Order_Header')]"] # текст "Для кого самокат"
    INPUT_NAME = [By.XPATH, ".//*[contains(@class, 'Input_Input') and (@placeholder='* Имя')]"] # Поле ввода имени покупателя
    INPUT_SURNAME = [By.XPATH, ".//*[contains(@class, 'Input_Input') and (@placeholder='* Фамилия')]"] # Поле ввода фамилии покупателя
    INPUT_ADDRESS = [By.XPATH, ".//*[contains(@class, 'Input_Input') and (@placeholder='* Адрес: куда привезти заказ')]"] # Поле ввода адреса
    INPUT_METRO_STATION = [By.XPATH, ".//*[@class='select-search__value']/input[@placeholder='* Станция метро']"]  # поле ввода станции метро
    LIST_METRO_STATIONS = [By.XPATH, ".//li//div[contains(@class,'Order_Text')]"]  # выпадающий список всех станций метро
    PHONE_NUMBER = [By.XPATH, ".//*[contains(@class, 'Input_Input') and (@placeholder='* Телефон: на него позвонит курьер')]"] # Поле ввода телефона
    NEXT_BUTTON = [By.XPATH, ".//div[contains(@class, 'Order_NextButton')]/button"] # Кнопка Далее
    DELIVERY_DATE = [By.XPATH, ".//*[contains(@class, 'Input_Input') and (@placeholder='* Когда привезти самокат')]"] # Поле ввода даты доставки
    INPUT_RENTAL_TERM = [By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"] # Поле ввода срока аренды
    LIST_RENTAL_TERMS = [By.XPATH, ".//div[@class='Dropdown-menu']/div"] # Список сроков аренды
    LIST_COLOR_SCOOTER = [By.XPATH, ".//label[contains(@class,'Checkbox_Label')]"]  # Список Цвет самоката
    COMMENT = [By.XPATH, ".//input[contains(@class,'Input_Responsibl')and @placeholder='Комментарий для курьера']"]  # Комментарий для курьера
    ORDER_BUTTON = [By.XPATH, ".//*[contains(@class,'Order_Buttons')]/button[text()='Заказать']"]  # Кнопка Заказать
    YES_BUTTON = [By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[text()='Да']"]  # Кнопка Да в сообщении подтверждения заказа
    SUCCESS_ORDER_MESSAGE = [By.XPATH, ".//*[contains(@class,'Order_ModalHeader')]"]  # Сообщение об успешном заказе
    VIEW_STATUS_BUTTON = [By.XPATH, ".//div[contains(@class,'Order_NextButton')]/button[text()='Посмотреть статус']"]  # Кнопка Просмотреть статус







