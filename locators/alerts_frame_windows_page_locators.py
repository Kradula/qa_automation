

class BrowserWindowsPageLocators:

    NEW_TAB_BUTTON = ('xpath', "//button[@id='tabButton']")
    NEW_WINDOW_BUTTON = ('xpath', "//button[@id='windowButton']")

    TITLE_NEW = ('xpath', "//h1[@id='sampleHeading']")


class AlertsPageLocators:

    SEE_ALERT_BUTTON = ('xpath', "//button[@id='alertButton']")
    TIMER_ALERT_BUTTON = ('xpath', "//button[@id='timerAlertButton']")
    CONFIRM_ALERT_BUTTON = ('xpath', "//button[@id='confirmButton']")
    CHECK_CONFIRM_ALERT_TEXT = ('xpath', "//span[@id='confirmResult']")
    PROMPT_ALERT_BUTTON = ('xpath', "//button[@id='promtButton']")
    CHECK_PROMPT_ALERT_TEXT = ('xpath', "//span[@id='promptResult']")

