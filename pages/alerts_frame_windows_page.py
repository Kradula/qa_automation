import random
import time

from locators.alerts_frame_windows_page_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        return alert_window.text

    def check_timer_alert(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CHECK_CONFIRM_ALERT_TEXT).text
        return text_result

    def check_prompt_alert(self):
        text = f"Autotest {random.randint(1, 1000)}"
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CHECK_PROMPT_ALERT_TEXT).text
        return text, text_result
