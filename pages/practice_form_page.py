import random
import time

from selenium.webdriver import Keys

from generator.generator import generated_person
from locators.practice_form_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):

    locators = PracticeFormPageLocators()

    def fill_out_all_fields(self, gender_key_word, hobby_key_words, subject_choices):
        person_info = next(generated_person())
        self.remove_footer()
        name = person_info.firstname
        lastname = person_info.lastname
        email = person_info.email
        phone = person_info.phone_number
        current_address = person_info.current_address
        file_to_upload = r'C:\Users\User\Desktop\Untitled.png'
        state = 'Rajasthan'
        city = 'Jaiselmer'
        gender_choice = {
            'male': self.locators.GENDER_MALE,
            'female': self.locators.GENDER_FEMALE,
            'other': self.locators.GENDER_OTHER,
        }

        hobby_choices = {
            'Sports': self.locators.HOBBY_SPORT,
            'Reading': self.locators.HOBBY_READING,
            'Music': self.locators.HOBBY_MUSIC,
        }

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        random_month = random.choice(months)
        random_date = random.randint(1, 28)
        random_year = random.randint(1900, 2100)

        self.element_is_visible(self.locators.NAME).send_keys(name)
        self.element_is_visible(self.locators.LASTNAME).send_keys(lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE).send_keys(phone)
        self.element_is_visible(gender_choice[gender_key_word]).click()
        for hobby in hobby_key_words:
            self.element_is_visible(hobby_choices[hobby]).click()
        for subject in subject_choices:
            self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys(subject)
            self.element_is_visible(self.locators.SUBJECT_INPUT).send_keys(Keys.ENTER)
        date_of_birth = self.element_is_visible(self.locators.DATE_OF_BIRTH)
        date_of_birth.send_keys(Keys.CONTROL + 'A')
        date_of_birth.send_keys(f'{random_date} {random_month} {random_year}')
        date_of_birth.send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.UPLOAD_PICTURE).send_keys(file_to_upload)
        self.element_is_present(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_present(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return (name, lastname, email, phone, gender_key_word, hobby_key_words, subject_choices,
                f'{random_date} {random_month} {random_year}', current_address, state, city)

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item)
        return data


