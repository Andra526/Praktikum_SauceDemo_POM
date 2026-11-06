import pytest


@pytest.mark.smoke
def test_checkout_success(logged_in, inventory_page, cart_page, checkout_page):
    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.click_checkout()
    assert checkout_page.get_title() == "Checkout: Your Information"

    checkout_page.fill_information("Budi", "Santoso", "51111")
    checkout_page.click_continue()
    assert checkout_page.get_title() == "Checkout: Overview"

    checkout_page.click_finish()
    assert checkout_page.get_complete_message() == "Thank you for your order!"


@pytest.mark.negative
def test_checkout_missing_first_name(logged_in, inventory_page, cart_page, checkout_page):
    inventory_page.add_backpack()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.fill_information("", "Santoso", "51111")
    checkout_page.click_continue()
    assert "First Name is required" in checkout_page.get_error_message()
