import pytest


@pytest.mark.smoke
def test_login_valid(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.current_url()
    assert inventory_page.get_title() == "Products"


@pytest.mark.negative
def test_login_invalid_password(login_page):
    login_page.login("standard_user", "salah_password")
    assert "do not match" in login_page.get_error_message()


@pytest.mark.negative
def test_login_locked_out_user(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error_message()


@pytest.mark.negative
def test_login_empty_username(login_page):
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.get_error_message()


def test_logout(logged_in, inventory_page, login_page):
    inventory_page.logout()
    assert login_page.is_visible(login_page.LOGIN_BUTTON)
