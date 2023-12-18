

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


class RadioButtonPageLocators:

    YES_RADIO_BUTTON = ('xpath', '//label[@for="yesRadio"]')
    NO_RADIO_BUTTON = ('xpath', '//label[@for="noRadio"]')
    IMPRESSIVE_RADIO_BUTTON = ('xpath', '//label[@for="impressiveRadio"]')
    OUTPUT_RESULT = ('xpath', '//span[@class="text-success"]')


class WebTablePageLocators:
    # add person form
    ADD_BUTTON = ('xpath', '//button[@id="addNewRecordButton"]')
    FIRSTNAME_INPUT = ('xpath', '//input[@id="firstName"]')
    LASTNAME_INPUT = ('xpath', '//input[@id="lastName"]')
    EMAIL_INPUT = ('xpath', '//input[@id="userEmail"]')
    AGE_INPUT = ('xpath', '//input[@id="age"]')
    SALARY_INPUT = ('xpath', '//input[@id="salary"]')
    DEPARTMENT_INPUT = ('xpath', '//input[@id="department"]')
    SUBMIT_BUTTON = ('xpath', '//button[@id="submit"]')

    # table
    FULL_PEOPLE_LIST = ('xpath', '//div[@class="rt-tr-group"]')

    SEARCH_INPUT = ('xpath', '//input[@id="searchBox"]')
    DELETE_BUTTON = ('xpath', '//span[@title="Delete"]')
    ROW_PARENT = ('xpath', ".//ancestor::div[@class='rt-tr-group']")
