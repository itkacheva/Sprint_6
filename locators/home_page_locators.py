from selenium.webdriver.common.by import By


class HomePageScooterLocators:
    QUESTIONS = [By.XPATH, ".//div[text()='Вопросы о важном']/..//div[contains(@id,'accordion__heading')]"] # Вопросы в блоке "Вопросы о важном" на главной странице
    ANSWER = [By.XPATH, ".//*[contains(@id, 'accordion__panel') and not(@hidden)]/p"] # Ответ на вопрос в блоке "Вопросы о важном" на главной странице
    CLOSE_BUTTON_COOKIE = [By.XPATH, ".//Button[text()='да все привыкли']"] # Кнопка "да все привыкли"
    IMG_SCOOTER = [By.XPATH, ".//img[@src='/assets/blueprint.png']"] # Заголовок блока "Вопросы о важном"
    ORDER_BUTTON_HEADER = [By.XPATH, ".//*[contains(@class,'Header_Nav')]/button[text()='Заказать']"] # Кнока "Заказать" в заголовке страницы
    ORDER_BUTTON_BOTTOM = [By.XPATH, ".//*[contains(@class,'Home_FinishButton')]/button[text()='Заказать']"] # Кнопка "Заказать" внизу страницы
    LOGO_SCOOTER = [By.XPATH, ".//a[contains(@class,'Header_LogoScooter')]/img"] # Логотип Самокат
    LOGO_YANDEX = [By.XPATH, ".//a[contains(@class,'Header_LogoYandex')]/img"] # Логотип Самокат




