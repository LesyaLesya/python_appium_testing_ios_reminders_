"""Модуль с фикстурами."""


import os
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from utils.locators import (MainPageLocators, ReminderListInfoPageLocators, RemindersListPageLocators, AlertsLocators)
from appium.webdriver.common.appiumby import AppiumBy
from utils.allure_helper import attach_capabilities
from selenium.common.exceptions import NoSuchElementException

load_dotenv()


@pytest.fixture(autouse=True)
def appium_driver(request):
    """Фикстура для запуска драйвера в зависимости от параметров."""
    platform_name = os.getenv('PLATFORM_NAME')
    udid = os.getenv('UDID')
    bundle_id = os.getenv('BUNDLE_ID')
    appium_server_url = os.getenv('APPIUM_SERVER_URL')

    capabilities = dict(
        platformName=platform_name,
        udid=udid,
        automationName='XCUITest',
        bundleId=bundle_id,
        autoDismissAlerts=True
    )
    capabilities_options = XCUITestOptions().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    driver.implicitly_wait(2)
    request.cls.driver = driver
    attach_capabilities(driver)
    yield driver
    driver.quit()


@pytest.fixture
def create_list(appium_driver):
    def _create_list(name, color):
        appium_driver.find_element(by=AppiumBy.XPATH, value=MainPageLocators.BUTTON_ADD_LIST).click()
        appium_driver.find_element(by=AppiumBy.XPATH, value=ReminderListInfoPageLocators.LIST_NAME_FIELD).send_keys(name)
        appium_driver.find_element(by=AppiumBy.XPATH, value=ReminderListInfoPageLocators.LIST_COLOR(color)).click()
        appium_driver.find_element(by=AppiumBy.XPATH, value=ReminderListInfoPageLocators.DONE_BUTTON).click()
        appium_driver.find_element(by=AppiumBy.XPATH, value=RemindersListPageLocators.BACK_TO_LISTS_BUTTON).click()
        return name, color
    return _create_list


@pytest.fixture
def delete_list(appium_driver):
    def _delete_list(name, color):
        try:
            appium_driver.find_element(by=AppiumBy.XPATH, value=MainPageLocators.LIST_NAME_COLOR(name, color)).click()
        except NoSuchElementException:
            pass
        finally:
            appium_driver.find_element(by=AppiumBy.XPATH, value=RemindersListPageLocators.CONTEXT_MENU).click()
            appium_driver.find_element(by=AppiumBy.XPATH, value=RemindersListPageLocators.CONTEXT_MENU_DELETE_LIST).click()
        try:
            appium_driver.find_element(by=AppiumBy.XPATH, value=AlertsLocators.DELETE_BUTTON).click()
        except NoSuchElementException:
            pass
    return _delete_list


@pytest.fixture
def fixture_create_delete_list(create_list, delete_list, request):
    def _create_delete(name1, color1, color2=None, name2=None):
        create_list(name1, color1)

        def teardown():
            if color2 and name2:
                delete_list(name2, color2)
            elif color2 and not name2:
                delete_list(name1, color2)
            elif name2 and not color2:
                delete_list(name2, color1)
            else:
                delete_list(name1, color1)
        request.addfinalizer(teardown)
        return name1, color1, color2, name2
    return _create_delete
