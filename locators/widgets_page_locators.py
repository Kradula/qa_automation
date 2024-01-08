

class AccordianPageLocators:

    FIRST_SECTION = ('xpath', "//div[@id='section1Heading']")
    FIRST_SECTION_CONTENT = ('xpath', "//div[@id='section1Content']/p")

    SECOND_SECTION = ('xpath', "//div[@id='section2Heading']")
    SECOND_SECTION_CONTENT = ('xpath', "//div[@id='section2Content']/p")

    THIRD_SECTION = ('xpath', "section3Heading")
    THIRD_SECTION_CONTENT = ('xpath', "//div[@id='section3Content']/p")


class AutoCompletePageLocators:

    MULTI_INPUT = ('xpath', "//input[@id='autoCompleteMultipleInput']")
    MULTI_VALUE = ('xpath', "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_REMOVE = ('css selector', "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
    SINGLE_INPUT = ('xpath', "//input[@id='autoCompleteSingleInput']")
    SINGLE_CONTAINER = ('xpath', "//div[@class='auto-complete__single-value css-1uccc91-singleValue']")


