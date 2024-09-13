from Config.config import TestData
from features.Login import Login
from test.test_base import BaseTest


class TestLogin(BaseTest):
    def test_login(self):
        self.log_in = Login(self.driver)
        assert self.log_in.login(TestData.USER_EMAIL,TestData.PASSWORD) == TestData.USER_NAME


    def test_messege_button(self):
        self.log_in = Login(self.driver)
        assert self.log_in.is_messege_button()


    # def test_my_ebay_options(self):
    #     self.log_in = Login(self.driver)
    #     assert self.log_in.my_ebay_options() == TestData.MY_EBAY_OPTIONS