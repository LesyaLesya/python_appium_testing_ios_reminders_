"""Модуль c методами для Главной страницы."""

import allure
from base.base_page import BasePage
from utils.locators import RemindersListPageLocators


class RemindersListPage(BasePage):
    """Класс с методами для Главной страницы."""

    @allure.step('Проверить, что название списка - {value}')
    def check_list_name(self, value):
        self.is_element_visible(RemindersListPageLocators.LIST_NAME(value))

    @allure.step('Нажать на кнопку возврата к спискам')
    def back_to_lists(self):
        self.click_on_element(RemindersListPageLocators.BACK_TO_LISTS_BUTTON)

    @allure.step('Кликнуть на кнопку контекстного меню списка')
    def open_context_menu(self):
        self.click_on_element(RemindersListPageLocators.CONTEXT_MENU)

    @allure.step('Нажать на кнопку удаления списка')
    def press_delete_list_from_context_menu(self):
        self.click_on_element(RemindersListPageLocators.CONTEXT_MENU_DELETE_LIST)

    @allure.step('Нажать на кнопку создания напоминания')
    def press_add_reminider_button(self):
        self.click_on_element(RemindersListPageLocators.ADD_REMINDER_BUTTON)

    @allure.step('Ввести текст напоминания')
    def input_text_of_reminder(self, value, idx=0):
        self.input_text(RemindersListPageLocators.REMINDER_FIELD, value, idx)

    @allure.step('Нажать кнопку Done')
    def click_done_button(self):
        self.click_on_element(RemindersListPageLocators.DONE_BUTTON)

    @allure.step('Проверить, что в списке количество напоминаний - {nums}')
    def check_numbers_of_reminders_in_list(self, nums):
        elements = self.element(RemindersListPageLocators.REMINDERS_IN_LIST, all=True)
        assert len(elements) == nums, f'Количество напоминаний {len(elements)}, ожидаем - {nums}'

    @allure.step('Проверить, что напоминание {value} в списке')
    def check_reminder_in_list(self, value):
        self.is_element_visible(RemindersListPageLocators.REMINDER_IN_LIST(value))

    @allure.step('Нажать на кнопку Show List Info')
    def press_show_info_from_context_menu(self):
        self.click_on_element(RemindersListPageLocators.CONTEXT_MENU_SHOW_LIST_INFO_BUTTON)
