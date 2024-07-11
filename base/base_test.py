import pytest
from base.base_page import BasePage
from pages.main_page import MainPage
from pages.reminder_list_info_page import ReminderListInfoPage
from pages.reminders_list_page import RemindersListPage
from pages.reminder_page import ReminderPage


class BaseTest:
    base: BasePage
    main_page: MainPage
    reminder_list_info_page: ReminderListInfoPage
    reminder_list_page: RemindersListPage
    reminder_page: ReminderPage

    @pytest.fixture(autouse=True)
    def setup(self, request, appium_driver):
        request.cls.base = BasePage(appium_driver)
        request.cls.main_page = MainPage(appium_driver)
        request.cls.reminder_list_info_page = ReminderListInfoPage(appium_driver)
        request.cls.reminder_list_page = RemindersListPage(appium_driver)
        request.cls.reminder_page = ReminderPage(appium_driver)
