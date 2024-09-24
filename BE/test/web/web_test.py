import pytest
from .test_base import WebBase
from .pages.login_page import LoginPage


@pytest.fixture
def username():
    return 'user'


@pytest.fixture
def password():
    return 'test1234'


class TestWeb(WebBase):

    def test_login(self, username, password):
        LoginPage(self.driver).elements['username'].set(username)
        LoginPage(self.driver).elements['password'].set(password)
        LoginPage(self.driver).elements.login.click()
