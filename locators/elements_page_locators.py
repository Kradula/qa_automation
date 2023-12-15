

class TextBoxPageLocators:

    # form fields
    FULL_NAME = ('xpath', '//input[@id="userName"]')
    EMAIL = ('xpath', '//input[@id="userEmail"]')
    CURRENT_ADDRESS = ('xpath', '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = ('xpath', '//textarea[@id="permanentAddress"]')
    SUBMIT = ('xpath', '//button[@id="submit"]')

    # created form
    CREATED_FULL_NAME = ('xpath', '//p[@id="name"]')
    CREATED_EMAIL = ('xpath', '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = ('xpath', '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = ('xpath', '//p[@id="permanentAddress"]')


class CheckBoxPageLocators:

    EXPAND_ALL = ('xpath', '//button[@title="Expand all"]')
    ITEM_LIST = ('xpath', '//span[@class="rct-title"]')
    CHECKED_ITEMS = ('css selector', 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ('xpath', ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ('xpath', '//span[@class="text-success"]')
