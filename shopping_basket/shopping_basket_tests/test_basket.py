import pytest
from shopping_basket import ZeroQuantityException, ItemDoesNotExistException

def test_empty_basket(empty_basket):
    """ Tests the return values from an empty basket """
    assert len(empty_basket.items) == 0
    assert empty_basket.item_count == 0
    assert empty_basket.sub_total == 0.00
    assert empty_basket.discount == 0.00
    assert empty_basket.total == 0.00

@pytest.mark.parametrize('item_name,quantity,exception', [
    ('Biscuits', 0, ZeroQuantityException(
        'Item quantity cannot be zero')),
    ('Biscuits', 6, None),
    ('Sardines', 3, None)
])
def test_add_new_basket_item(base_basket_1, item_name, quantity, exception):

    """ Tests the addition of a new basket item x quantity """

    # The basket starts with 5 total items
    assert base_basket_1.item_count == 5

    # Get existing quantity for item if any so that we can test update
    item_name = item_name.strip()
    start_quantity = base_basket_1.items[item_name] if item_name \
        in base_basket_1.items.keys() else 0

    try:
        base_basket_1.add_new_basket_item(item_name, quantity)
    except ZeroQuantityException as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that product has been added
        assert base_basket_1.items[item_name] == start_quantity + quantity
        assert base_basket_1.item_count == 5 + quantity

@pytest.mark.parametrize('item_name,exception', [
    ('Fish Fingers', ItemDoesNotExistException(
        'Fish Fingers does not exist in basket')),
    ('Biscuits', None)
])
def test_remove_basket_item(base_basket_1, item_name, exception):

    """ Tests the removal of an existing basket item """

    assert base_basket_1.item_count == 5

    # Get existing quantity for item if any so that we can test update
    item_name = item_name.strip()
    start_quantity = base_basket_1.items[item_name] if item_name \
        in base_basket_1.items.keys() else 0

    try:
        base_basket_1.remove_basket_item(item_name)
    except ItemDoesNotExistException as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that item has been removed
        assert item_name not in base_basket_1.items.keys()
        assert base_basket_1.item_count == 5 - start_quantity

def test_calculate_basket1_discount(base_basket_1, base_products_catalogue,
    base_offers_list):

    """ Tests the calculation of basket discount, referring to the catalogue
        and offer list for reference """

    base_basket_1.calculate_basket_discount(base_products_catalogue,
        base_offers_list)

    # Test that offers have been applied correctly
    # B2G1F on Baked Beans = discount 0.99 on 4 tins
    # No offers on Biscuits
    assert base_basket_1.sub_total == 5.16
    assert base_basket_1.discount == 0.99
    assert base_basket_1.total == 4.17