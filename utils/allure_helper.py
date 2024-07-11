"""Модуль c вспомогательными методами для allure."""

import allure
import json


def attach(appium_driver):
    return allure.attach(
            body=appium_driver.get_screenshot_as_png(),
            name="screenshot_image",
            attachment_type=allure.attachment_type.PNG)


def attach_capabilities(appium_driver):
    return allure.attach(
            body=appium_driver.session_id,
            name=json.dumps(appium_driver.capabilities),
            attachment_type=allure.attachment_type.JSON)
