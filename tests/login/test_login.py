import pytest
import time

@pytest.mark.parametrize("email,password,expected", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ("qa.ajax.app.autoыыmation@gmail.com", "qa_autoыыыmation_password", False),
])
def test_user_login(user_login_fixture, email, password, expected):
    time.sleep(5)
    login_page = user_login_fixture
    login_page.tap_auth_button()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.tap_login_button()

    assert login_page.is_logged_in() == expected
