

class PracticeFormPageLocators:

    NAME = ('xpath', "//input[@id='firstName']")
    LASTNAME = ('xpath', "//input[@id='lastName']")
    EMAIL = ('xpath', "//input[@id='userEmail']")
    MOBILE = ('xpath', "//input[@id='userNumber']")
    GENDER_OTHER = ('xpath', "//input[@value='Other']/parent::div")
    GENDER_FEMALE = ('xpath', "//input[@value='Female']/parent::div")
    GENDER_MALE = ('xpath', "//input[@value='Male']/parent::div")
    HOBBY_SPORT = ('xpath', "//input[@id='hobbies-checkbox-1']/parent::div")
    HOBBY_READING = ('xpath', "//input[@id='hobbies-checkbox-2']/parent::div")
    HOBBY_MUSIC = ('xpath', "//input[@id='hobbies-checkbox-3']/parent::div")
    SUBJECT_INPUT = ('xpath', "//input[@id='subjectsInput']")
    DATE_OF_BIRTH = ('xpath', "//input[@id='dateOfBirthInput']")
    CURRENT_ADDRESS = ('xpath', "//textarea[@id='currentAddress']")
    STATE_INPUT = ('xpath', "//input[@id='react-select-3-input']")
    STATE_SELECT = ('xpath', "//div[@id='state']")
    CITY_INPUT = ('xpath', "//input[@id='react-select-4-input']")
    CITY_SELECT = ('xpath', "//div[@id='city']")
    UPLOAD_PICTURE = ('xpath', "//input[@id='uploadPicture']")
    SUBMIT_BUTTON = ('xpath', "//button[@id='submit']")
    RESULT_TABLE = ('xpath', "//table[@class='table table-dark table-striped table-bordered table-hover']//td[2]")

