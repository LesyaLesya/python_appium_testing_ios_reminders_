"""Модуль с тестами для главного экрана."""

import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Главный экран')
@pytest.mark.main_page
class TestMainPage(BaseTest):
    """Тесты для главного экрана."""

    @allure.story('Элементы экрана')
    @allure.title('Проверка видимости элементов на экране')
    @allure.link('#', name='User story')
    def test_check_elements_visibility(self):
        self.main_page.check_elements_visibility()

    @allure.story('Блок со списками напоминаний')
    @allure.title('Проверка удаления списка')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, color', [('Hello', 'Green'), ('List', 'Yellow')])
    def test_delete_empty_list_from_main_page(self, create_list, name, color):
        create_list(name, color)
        self.main_page.click_edit_button()
        self.main_page.click_remove_button_for_list(name)
        self.main_page.click_delete_button_for_list()
        self.main_page.click_done_button()
        self.main_page.check_list_by_name_not_displayed_on_page(name, color)
