"""Модуль c общими методами для всех страниц."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from utils.allure_helper import attach


class BasePage:
    """Класс, описывающий базовую страницу."""

    def __init__(self, appium_driver):
        self.appium_driver = appium_driver

    @allure.step('Найти элемент с локатором {locator}')
    def element(self, locator, all=None):
        if all:
            return self.appium_driver.find_elements(by=AppiumBy.XPATH, value=locator)
        return self.appium_driver.find_element(by=AppiumBy.XPATH, value=locator)

    @allure.step('Проверить что элемент {locator} виден на странице')
    def is_element_visible(self, locator, idx=None):
        if idx is not None:
            element = self.element(locator, all=True)[idx]
        else:
            element = self.element(locator)
        try:
            assert element.is_displayed()
        except NoSuchElementException:
            attach(self.appium_driver)
            raise AssertionError(f'Элемент {locator} не отображается на странице')

    @allure.step('Проверить что элемент {locator} с индексом не виден на странице')
    def is_element_not_visible(self, locator, idx=None):
        try:
            if idx is not None:
                self.element(locator, all=True)[idx].is_displayed()
            else:
                self.element(locator).is_displayed()
            raise AssertionError(f'Элемент {locator} отображается на странице')
        except NoSuchElementException:
            attach(self.appium_driver)
            assert True

    @allure.step('Кликнуть по элементу с локатором {locator}')
    def click_on_element(self, locator, idx=None):
        if idx is not None:
            element = self.element(locator, all=True)[idx]
        else:
            element = self.element(locator)
        try:
            if element and element.is_enabled():
                return element.click()
        except ElementClickInterceptedException:
            attach(self.appium_driver)
            raise AssertionError(f'Не получается кликнуть по элементу {locator}')

    @allure.step('Ввести текст {value} в инпут {locator}')
    def input_text(self, locator, value, idx=None):
        if idx is not None:
            element = self.element(locator, all=True)[idx]
        else:
            element = self.element(locator)
        try:
            element.click()
            element.clear()
            return element.send_keys(value)
        except Exception:
            attach(self.appium_driver)
            raise AssertionError(f'Не получается ввести текст {value} в элемент {locator}')

    @allure.step('Нажать на клавишу {value}')
    def press(self, value):
        self.appium_driver.hide_keyboard(value)
