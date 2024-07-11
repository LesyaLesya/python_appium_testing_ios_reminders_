"""Модуль c методами для Главного экрана приложения."""

import allure
from base.base_page import BasePage
from utils.locators import MainPageLocators


class MainPage(BasePage):
    """Класс с методами для Главного экрана приложения."""

    @allure.step('Проверить видимость элементов на экране')
    def check_elements_visibility(self):
        lst = [MainPageLocators.BUTTON_ADD_LIST,
               MainPageLocators.BUTTON_NEW_REMINDER,
               MainPageLocators.EDIT_BUTTON,
               MainPageLocators.SEARCH_FIELD,
               MainPageLocators.TODAY_REMINDERS,
               MainPageLocators.ALL_REMINDERS,
               MainPageLocators.COMPLETED_REMINDERS,
               MainPageLocators.SCHEDULED_REMINDERS,
               MainPageLocators.HEADER_MY_LISTS]
        for i in lst:
            with allure.step(f'Проверить, что виден элемент {i}'):
                self.is_element_visible(i)

    @allure.step('Кликнуть на кнопку создания списка напоминаний')
    def click_create_new_list_of_reminders_button(self):
        self.click_on_element(MainPageLocators.BUTTON_ADD_LIST)

    @allure.step('Проверить, что лист {name} {color} отображается на экране')
    def check_list_by_name_on_page(self, name, color):
        self.is_element_visible(MainPageLocators.LIST_NAME_COLOR(name, color))

    @allure.step('Перейти на экран листа с названием {name} {color}')
    def go_to_list(self, name, color):
        self.click_on_element(MainPageLocators.LIST_NAME_COLOR(name, color))

    @allure.step('Нажать на кнопку редактирования Edit')
    def click_edit_button(self):
        self.click_on_element(MainPageLocators.EDIT_BUTTON)

    @allure.step('Нажать на кнопку удаления списка {value}')
    def click_remove_button_for_list(self, value, idx=0):
        # example: idx=2
        self.click_on_element(MainPageLocators.REMOVE_LIST_BUTTON_BY_NAME(value), idx)

    @allure.step('Нажать на кнопку удаления списка')
    def click_delete_button_for_list(self):
        self.click_on_element(MainPageLocators.DELETE_LIST_BUTTON)

    @allure.step('Нажать на кнопку Done')
    def click_done_button(self):
        self.click_on_element(MainPageLocators.DONE_EDIT_BUTTON)

    @allure.step('Проверить, что лист {name} {color} не отображается на экране')
    def check_list_by_name_not_displayed_on_page(self, name, color):
        self.is_element_not_visible(MainPageLocators.LIST_NAME_COLOR(name, color))

    @allure.step('Кликнуть на кнопку More info листа {name} {color}')
    def click_more_info_button(self, name, color):
        self.click_on_element(MainPageLocators.INFO_BUTTON_FOR_LIST(name, color))

    @allure.step('Проверить, что в листе {name} количество напоминаний {num}')
    def check_nums_of_reminders_in_list(self, name, num):
        self.is_element_visible(MainPageLocators.LIST_NAME_WITH_REMINDERS(name, num))

    @allure.step('Кликнуть на кнопку New Reminder')
    def click_new_reminder_button(self):
        self.click_on_element(MainPageLocators.BUTTON_NEW_REMINDER)
