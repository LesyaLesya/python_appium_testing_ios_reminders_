"""Модуль c методами для экрана создания нового напоминания."""

import allure
from base.base_page import BasePage
from utils.locators import ReminderPageLocators


class ReminderPage(BasePage):
    """Класс с методами для экрана создания нового напоминания."""

    @allure.step('Проверить видимость элементов на экране')
    def check_elements_visibility(self):
        lst = [ReminderPageLocators.TITLE_FIELD,
               ReminderPageLocators.NOTE_FIELD,
               ReminderPageLocators.DETAILS,
               ReminderPageLocators.CANCEL_BUTTON,
               ReminderPageLocators.ADD_BUTTON,
               ReminderPageLocators.LIST_BLOCK]
        for i in lst:
            with allure.step(f'Проверить, что виден элемент {i}'):
                self.is_element_visible(i)

    @allure.step('Ввести текст напоминания - {value}')
    def enter_reminder_title(self, value):
        self.input_text(ReminderPageLocators.TITLE_FIELD, value)

    @allure.step('Кликнуть на поле для выбра списка')
    def click_to_choose_list(self):
        self.click_on_element(ReminderPageLocators.LIST_BLOCK)

    @allure.step('Выбрать список {name}')
    def choose_list_by_name(self, name):
        self.click_on_element(ReminderPageLocators.LIST_FOR_CHOOSE_BY_NAME(name))

    @allure.step('Кликнуть на кнопку Add')
    def click_add_button(self):
        self.click_on_element(ReminderPageLocators.ADD_BUTTON)

