import pytest
from .test_base import WebBase
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.calculator_page import CalculatorPage


@pytest.fixture
def username():
    return 'user'


@pytest.fixture
def password():
    return 'test1234'


class TestWeb(WebBase):

    # tests registering a new user
    def test_register(self, username, password):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements['username'].set(username)
        RegisterPage(self.driver).elements['password1'].set(password)
        RegisterPage(self.driver).elements['password2'].set(password)
        RegisterPage(self.driver).elements.register.click()

    # tests logging in
    def test_login(self, username, password):
        LoginPage(self.driver).elements['username'].set(username)
        LoginPage(self.driver).elements['password'].set(password)
        LoginPage(self.driver).elements.login.click()

    def test_calculator(self):

        # # make sure we are logged out
        # CalculatorPage(self.driver).elements['logout_button'].click()

        # login
        # LoginPage(self.driver).elements['username'].set('admin')
        # LoginPage(self.driver).elements['password'].set('test1234')
        # LoginPage(self.driver).elements.login.click()

        CalculatorPage(self.driver).elements['key_2'].click()
        CalculatorPage(self.driver).elements['key_add'].click()
        CalculatorPage(self.driver).elements['key_3'].click()
        CalculatorPage(self.driver).elements['key_equals'].click()
        assert CalculatorPage(
            self.driver).elements['calculator-screen'].value == '5'
