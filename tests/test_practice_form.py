import time

from pages.practice_form_page import PracticeFormPage


class TestPracticeForm:

    def test_filling_form(self, driver):
        filling_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        filling_form_page.open()
        person_info = filling_form_page.fill_out_all_fields('male', ['Sports', 'Music'],
                                                            ['English', 'Computer Science'])

        result = filling_form_page.form_result()
        assert [person_info[0] + ' ' + person_info[1], person_info[2]] == [result[0], result[1]]
        