import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == "What is Lorem Ipsum?" and len(first_content) > 0, ("The title or content hasn't "
                                                                                      "matched")
            assert second_title == "Where does it come from?" and len(second_content) > 0, ("The title or content"
                                                                                            " hasn't matched")
            assert third_title == "Why do we use it?" and len(third_content) > 0, "The title or content hasn't matched"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_multi_input()
            colors_result = autocomplete_page.check_color_in_multi_input()
            assert colors == colors_result, "The lists haven't matched"

        def test_remove_value_from_multi_input(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_multi_input()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi_input()
            assert count_value_before > count_value_after, "The number of colors haven't matched"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_single_input()
            color_result = autocomplete_page.check_color_in_single_input()
            assert color == color_result, "The colors haven't matched"

