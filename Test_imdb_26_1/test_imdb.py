import pytest
from Test_imdb_26_1.pom.combine_imdb_methods import All_method

class Test_Imdb:

    @pytest.mark.usefixtures("setup")
    def test_advance_name_search_fields(self):
        data = All_method(self.driver)
        data.validate_imdb_fields()
