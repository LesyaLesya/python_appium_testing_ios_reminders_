"""Модуль с тестами для экрана информации о напоминании."""

import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Экран информации о напоминании')
@pytest.mark.reminder_list_info_page
class TestRemindersListInfoPage(BaseTest):
    """Тесты для экрана информации о напоминании."""

    @allure.story('Редактирование листа напоминаний')
    @allure.title('Изменение названия листа')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name_1, color, name_2', [('First_name', 'Green', 'New_name')])
    def test_change_list_name_from_reminders_list_page(self, fixture_create_delete_list, name_1, color, name_2):
        fixture_create_delete_list(name_1, color, name2=name_2)
        self.main_page.go_to_list(name_1, color)
        self.reminder_list_page.open_context_menu()
        self.reminder_list_page.press_show_info_from_context_menu()
        self.reminder_list_info_page.enter_list_name(name_2)
        self.reminder_list_info_page.click_done_button()
        self.reminder_list_page.check_list_name(name_2)
        self.reminder_list_page.back_to_lists()
        self.main_page.check_list_by_name_on_page(name_2, color)

    @allure.story('Редактирование листа напоминаний')
    @allure.title('Изменение цвета листа')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name, color_1, color_2', [('Hello', 'Green', 'Red')])
    def test_change_color_list_from_main_page(self, fixture_create_delete_list, name, color_1, color_2):
        fixture_create_delete_list(name, color_1, color_2)
        self.main_page.click_edit_button()
        self.main_page.click_more_info_button(name, color_1)
        self.reminder_list_info_page.choose_list_color(color_2)
        self.reminder_list_info_page.check_icon_color(color_2)
        self.reminder_list_info_page.click_done_button()
        self.main_page.click_done_button()
        self.main_page.check_list_by_name_on_page(name, color_2)

    @allure.story('Редактирование листа напоминаний')
    @allure.title('Отмена сделанных изменений')
    @allure.link('#', name='User story')
    @pytest.mark.parametrize('name_1, name_2, color_1, color_2', [('First', 'Second', 'Green', 'Red')])
    def test_cancel_and_discard_changes(self, fixture_create_delete_list, name_1, name_2, color_1, color_2):
        fixture_create_delete_list(name_1, color_1)
        self.main_page.go_to_list(name_1, color_1)
        self.reminder_list_page.open_context_menu()
        self.reminder_list_page.press_show_info_from_context_menu()
        self.reminder_list_info_page.enter_list_name(name_2)
        self.reminder_list_info_page.choose_list_color(color_2)
        self.reminder_list_info_page.click_cancel_button()
        self.reminder_list_info_page.click_discard_changes_button()
        self.reminder_list_page.check_list_name(name_1)
        self.reminder_list_page.back_to_lists()
        self.main_page.check_list_by_name_on_page(name_1, color_1)
