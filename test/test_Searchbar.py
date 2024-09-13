from Config.config import TestData
from features.Searchbar import Search
from test.test_base import BaseTest


class TestSearchbar(BaseTest):
    def test_get_search_text_item(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.get_search_text_item() == "shoes men"


    def test_sort_button(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.sort_button_check()



    def test_sort_options(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.sort_options() == TestData.SORT_OPTIONS



    def test_buying_format_options(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.buying_format_options() == TestData.BUYING_FORMAT



    def test_condition_options(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.condition_options() == TestData.CONDITION_OPTIONS



    def test_category_options(self):
        self.searchbar = Search(self.driver)
        assert  self.searchbar.category_options() == TestData.CATAGORY_OPTIONS



    def test_filtered_item(self):
        self.searchbar = Search(self.driver)
        assert self.searchbar.filtered_items()



    def test_search_success(self):
        self.searchbar = Search(self.driver)
        assert  self.searchbar.search_success()