import random
import time

import locators.elements_page_locators
from generator.generator import generated_person
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage
from locators.elements_page_locators import WebTablePageLocators


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
        print(key_word)
        print(table_result)
        assert key_word in table_result, "The person wasn't found in the table"

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, 'The person card has not been changed'

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == 'No rows found', "The table isn't empty"

    def test_webtable_change_amount_of_rows(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50, 100], f'{print(count)} must be equal to [5, 10, 20, 25, 50, 100]'


class TestButtonPage:

    def test_different_click_on_buttons(self, driver):
        button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        double = button_page.click_on_different_buttons('double')
        right = button_page.click_on_different_buttons('right')
        click = button_page.click_on_different_buttons('click')
        assert double == "You have done a double click", "The double click button was not pressed"
        assert right == "You have done a right click", "The right click button was not pressed"
        assert click == "You have done a dynamic click", "The dynamic click button was not pressed"


class TestLinksPage:

    def test_check_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "Links didn't match"

    def test_broken_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
        assert response_code == 400, "The response code didn't equal 400"


class TestUploadAndDownload:

    def test_upload_file(self, driver):
        upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        upload_page.open()
        file_name, result = upload_page.upload_file()
        assert file_name == result, "The file has not been uploaded"

    def test_download_file(self, driver):
        links_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        links_page.open()
        check = links_page.download_file()
        assert check is True, "The file has not been downloaded"


class TestDynamicProperties:

    def test_dynamic_properties(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_color()
        assert color_before != color_after, "The color has not been changed "

    def test_appear_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        appear_button = dynamic_properties_page.check_appear_button()
        assert appear_button is True, "The button hasn't appeared after 5 seconds"

    def test_enable_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        enable_button = dynamic_properties_page.check_enable_button()
        assert enable_button is True, "The button hasn't got clickable after 5 seconds"



