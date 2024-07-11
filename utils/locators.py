"""Модуль с локаторами элементов."""


class MainPageLocators:
    """Локаторы алертов."""

    BUTTON_ADD_LIST = '//XCUIElementTypeButton[@name="Add List"]'
    EDIT_BUTTON = '//XCUIElementTypeButton[@name="Edit"]'
    SEARCH_FIELD = '//XCUIElementTypeSearchField[@name="Search"]'
    TODAY_REMINDERS = '//XCUIElementTypeButton[contains(@name, "Today")]'
    SCHEDULED_REMINDERS = '//XCUIElementTypeButton[contains(@name, "Scheduled")]'
    ALL_REMINDERS = '//XCUIElementTypeButton[contains(@name, "All")]'
    COMPLETED_REMINDERS = '//XCUIElementTypeButton[@name="Completed"]'
    HEADER_MY_LISTS = '//XCUIElementTypeOther[@label="My Lists"]'
    BUTTON_NEW_REMINDER = '//XCUIElementTypeButton[@name="New Reminder"]'
    LIST_NAME_COLOR = lambda name, color: f'//XCUIElementTypeCell[contains(@label,"{name}") and contains(@value, "{color}")]'
    LIST_NAME_WITH_REMINDERS = lambda name, nums: f'//XCUIElementTypeCell[@label="{name}, {nums} reminder"]'
    REMOVE_LIST_BUTTON_BY_NAME = lambda name: f'//XCUIElementTypeButton[@name="Remove {name}"]'
    DONE_EDIT_BUTTON = '//XCUIElementTypeButton[@name="Done"]'
    DELETE_LIST_BUTTON = '//XCUIElementTypeButton[@name="Delete"]'
    INFO_BUTTON_FOR_LIST = lambda name, color: f'//XCUIElementTypeCell[contains(@label,"{name}") and contains(@value, "{color}")]/XCUIElementTypeButton[@name="More Info"]'


class ReminderListInfoPageLocators:
    LIST_NAME_FIELD = '//XCUIElementTypeTextField[@name="List Name"]'
    LIST_COLOR = lambda color: f'//XCUIElementTypeOther[@name="{color}"]'
    DONE_BUTTON = '//XCUIElementTypeButton[@name="Done"]'
    LIST_ICON = lambda color: f'//XCUIElementTypeOther[@name="List Badge Preview, List badge, {color}"]'
    CANCEL_BUTTON = '//XCUIElementTypeButton[@name="Cancel"]'
    DISCARD_CHANGES_BUTTON = '//XCUIElementTypeButton[@name="Discard Changes"]'


class RemindersListPageLocators:
    LIST_NAME = lambda name: f'//XCUIElementTypeStaticText[@name="{name}"]'
    BACK_TO_LISTS_BUTTON = '//XCUIElementTypeButton[@name="Lists"]'
    CONTEXT_MENU = '//XCUIElementTypeButton[@name="More"]'
    CONTEXT_MENU_DELETE_LIST = '//XCUIElementTypeButton[@name="Delete List"]'
    CONTEXT_MENU_SHOW_LIST_INFO_BUTTON = '//XCUIElementTypeButton[@name="Show List Info"]'
    ADD_REMINDER_BUTTON = '//XCUIElementTypeButton[@name="New Reminder"]'
    REMINDER_FIELD = '//XCUIElementTypeTextField[@name="Title"]'
    DONE_BUTTON = '//XCUIElementTypeButton[@name="Done"]'
    REMINDERS_IN_LIST = '//XCUIElementTypeTextField[@name="Title"]'
    REMINDER_IN_LIST = lambda value: f'//XCUIElementTypeTextField[@name="Title" and @value="{value}"]'


class AlertsLocators:
    LOCATION_NOT_NOW = '//XCUIElementTypeButton[@name="Not Now"]'
    DELETE_BUTTON = '//XCUIElementTypeButton[@name="Delete"]'


class ReminderPageLocators:
    TITLE_FIELD = '//XCUIElementTypeTextField[@name="Quick Entry Title Field"]'
    NOTE_FIELD = '//XCUIElementTypeTextField[@name="Quick Entry Note Field"]'
    DETAILS = '//XCUIElementTypeStaticText[@name="Details"]'
    LIST_BLOCK = '//XCUIElementTypeCell[@name="List"]'
    ADD_BUTTON = '//XCUIElementTypeButton[@name="Add"]'
    CANCEL_BUTTON = '//XCUIElementTypeButton[@name="Cancel"]'
    LIST_FOR_CHOOSE_BY_NAME = lambda name: f'(//XCUIElementTypeStaticText[@name="{name}"])[2]'
