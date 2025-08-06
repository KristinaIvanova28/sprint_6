
import pytest
from pages.main_page import MainPage
from data import FAQData
import allure


class TestFAQ:
    @allure.title("FAQ: Вопрос {index}")
    @allure.description("Проверка открытия ответа на вопрос FAQ")
    @pytest.mark.parametrize("index", list(FAQData.EXPECTED_ANSWERS.keys()))
    def test_faq_expand(self, driver, index):
        expected_text = FAQData.EXPECTED_ANSWERS[index]
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(index)
        actual_text = main_page.get_faq_answer_text(index)
        assert actual_text == expected_text, \
            f"Вопрос {index + 1}: Ожидался текст:\n'{expected_text}'\nНо получен:\n'{actual_text}'"