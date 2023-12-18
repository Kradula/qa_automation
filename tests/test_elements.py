import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestTextBox:

    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
        assert full_name == output_name, "The full name didn't match"
        assert email == output_email, "The email didn't match"
        assert current_address == output_current_address, "The current address didn't match"
        assert permanent_address == output_permanent_address, "The permanent address didn't match"


class TestCheckBox:

    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, "Input checkbox and output checkbox didn't match"


class TestRadioButton:

    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()

        radio_button_page.click_on_radio_button('yes')
        output_yes = radio_button_page.get_output_result()

        radio_button_page.click_on_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()

        radio_button_page.click_on_radio_button('no')
        output_no = radio_button_page.get_output_result()

        assert output_yes == 'Yes', 'Yes has not been selected'
        assert output_impressive == 'Impressive', 'Impressive has not been selected'
        assert output_no != 'No', 'No has been selected'


class TestWebTable:

    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_added_person()
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        webtable_search = WebTablePage(driver, 'https://demoqa.com/webtables')
        webtable_search.open()
        key_word = webtable_search.add_new_person()[random.randint(0, 5)]
        webtable_search.search_person(key_word)
        table_result = webtable_search.check_search_person()
        assert key_word in table_result, "The person wasn't found in the table"

