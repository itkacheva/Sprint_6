import allure
import pytest
from data import questions_answers
from pages.home_page import HomePageScooter


class TestAnswersToQuestions:
    @allure.title('Проверка ответа на вопросy')
    @allure.description('На странице ищем конкретный вопрос, раcкрываем ответ и проверяем,'
                        ' что текст ответа соответствует ожидаемому')
    @pytest.mark.parametrize('text_question,text_answer', questions_answers)
    def test_get_answer_to_question_about_cost(self, driver, text_question, text_answer):
        hp = HomePageScooter(driver)
        hp.wait_for_load_home_page()
        hp.click_on_question(text_question)
        hp.wait_load_answer()
        assert hp.get_text_answer() == text_answer
