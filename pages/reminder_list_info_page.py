"""Модуль c методами для экрана создания нового списка."""
import time

import allure
from base.base_page import BasePage
from utils.locators import ReminderListInfoPageLocators


class ReminderListInfoPage(BasePage):
    """Класс с методами для экрана создания нового списка."""

    @allure.step('Ввести название списка {value}')
    def enter_list_name(self, value):
        self.input_text(ReminderListInfoPageLocators.LIST_NAME_FIELD, value)

    @allure.step('Выбрать цвет списка {value}')
    def choose_list_color(self, value):
        self.click_on_element(ReminderListInfoPageLocators.LIST_COLOR(value))

    @allure.step('Нажать на кнопку Done')
    def click_done_button(self):
        elements = self.element(ReminderListInfoPageLocators.DONE_BUTTON, all=True)
        if len(elements) > 1:
            self.click_on_element(ReminderListInfoPageLocators.DONE_BUTTON, idx=1)
        else:
            self.click_on_element(ReminderListInfoPageLocators.DONE_BUTTON)

    @allure.step('Проверить цвет иконки')
    def check_icon_color(self, color):
        self.is_element_visible(ReminderListInfoPageLocators.LIST_ICON(color))

    @allure.step('Нажать на кнопку Cancel')
    def click_cancel_button(self):
        self.click_on_element(ReminderListInfoPageLocators.CANCEL_BUTTON)

    @allure.step('Нажать на кнопку Discard')
    def click_discard_changes_button(self):
        self.click_on_element(ReminderListInfoPageLocators.DISCARD_CHANGES_BUTTON)
        time.sleep(2)
