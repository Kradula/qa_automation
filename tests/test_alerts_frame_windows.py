import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_open_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result = new_tab_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The texts hasn't matched"

        def test_open_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result = new_window_page.check_opened_new_window()
            assert text_result == "This is a sample page", "The texts hasn't matched"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert hasn't showed up"

        def test_timer_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_timer_alert()
            assert alert_text == "This alert appeared after 5 seconds", "Alert hasn't showed up"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok", "Alert hasn't showed up"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert alert_text == f'You entered {text}', "Alert hasn't showed up"

