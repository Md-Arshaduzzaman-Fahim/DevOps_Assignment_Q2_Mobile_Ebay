from Config.config import TestData
from features.Homepage import Home
from test.test_base import BaseTest


class TestHomePage(BaseTest):
    def test_ebay_logo(self):
        self.home = Home(self.driver)
        assert self.home.ebay_icon_displayed()


    def test_cart(self):
        self.home = Home(self.driver)
        assert  self.home.cart()



    def test_register_button(self):
        self.home = Home(self.driver)
        assert  self.home.register_button()



    def test_login_button(self):
        self.home = Home(self.driver)
        assert self.home.login_button()



    def test_search_tags(self):
        self.home = Home(self.driver)
        assert self.home.search_tags() == TestData.HOME_PAGE_SEARCH_TAGS



    def test_search_tag_link(self):
        self.home = Home(self.driver)
        assert self.home.seach_tag_click()



    def test_brand_name(self):
        self.home = Home(self.driver)
        assert  self.home.brand_names() == TestData.BRAND_NAMES

