def test_sort_price_low_to_high(logged_in, inventory_page):
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.get_item_prices()
    assert prices == sorted(prices)


def test_sort_name_z_to_a(logged_in, inventory_page):
    inventory_page.sort_by("Name (Z to A)")
    names = inventory_page.get_item_names()
    assert names == sorted(names, reverse=True)


def test_add_item_to_cart(logged_in, inventory_page, cart_page):
    inventory_page.add_backpack()
    assert inventory_page.get_cart_count() == 1
    inventory_page.open_cart()
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_add_two_items_and_remove_one(logged_in, inventory_page):
    inventory_page.add_backpack()
    inventory_page.add_bike_light()
    assert inventory_page.get_cart_count() == 2
    inventory_page.remove_backpack()
    assert inventory_page.get_cart_count() == 1
