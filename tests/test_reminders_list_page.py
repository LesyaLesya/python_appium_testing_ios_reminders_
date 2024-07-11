"""Модуль с тестами для экрана списка напоминаний."""

import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Экран списка напоминаний')
@pytest.mark.reminders_list_page
class TestRemindersListPage(BaseTest):
    """Тесты для экрана списка напоминаний."""

    @allure.story('Создание напоминаний')
    @allure.title('Проверка создания напоминания в списке')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, color', [('List of reminders', 'Green')])
    def test_create_reminder_in_list(self, fixture_create_delete_list, name, color):
        fixture_create_delete_list(name, color)
        self.main_page.go_to_list(name, color)
        self.reminder_list_page.press_add_reminider_button()
        self.reminder_list_page.input_text_of_reminder('Test1')
        self.reminder_list_page.click_done_button()
        self.reminder_list_page.check_numbers_of_reminders_in_list(1)
        self.reminder_list_page.check_reminder_in_list('Test1')
        self.reminder_list_page.back_to_lists()
        self.main_page.check_nums_of_reminders_in_list(name, 1)
