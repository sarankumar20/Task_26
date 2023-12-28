from Test_imdb_26_1.method.verify_imdb_names import Advance_search_fields
from Test_imdb_26_1.data.test_source import Values
class All_method(Values):

    def __init__(self, driver):
        self.driver = driver

    def validate_imdb_fields(self):
        data = Advance_search_fields(self.driver)
        data.click_signin_popup()
        data.click_and_enter_value_name_field(self.name_text)
        data.click_and_enter_value_date_field(self.date_from, self.date_to)
        data.click_and_select_awards_dropdown()
        data.click_and_enter_value_nickname()
