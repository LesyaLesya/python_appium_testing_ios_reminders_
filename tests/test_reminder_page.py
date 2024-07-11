"""Модуль с тестами для экрана создания напоминания."""

import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Экран создания напоминания')
@pytest.mark.reminder_page
class TestReminderPage(BaseTest):
    """Тесты для экрана создания напоминания."""

    @allure.story('Элементы экрана')
    @allure.title('Проверка видимости элементов на экране')
    @allure.link('#', name='User story')
    def test_check_elements_visibility(self):
        self.main_page.click_new_reminder_button()
        self.reminder_page.check_elements_visibility()

    @allure.story('Создание напоминания')
    @allure.title('Создание напоминания и добавление его в лист')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, color, title', [('My List', 'Red', 'first remind')])
    def test_create_reminder_for_list(self, fixture_create_delete_list, name, color, title):
        fixture_create_delete_list(name, color)
        self.main_page.click_new_reminder_button()
        self.reminder_page.enter_reminder_title(title)
        self.reminder_page.click_to_choose_list()
        self.reminder_page.choose_list_by_name(name)
        self.reminder_page.click_add_button()
        self.main_page.check_nums_of_reminders_in_list(name, 1)
        self.main_page.go_to_list(name, color)
        self.reminder_list_page.check_numbers_of_reminders_in_list(1)
        self.reminder_list_page.check_reminder_in_list(title)
