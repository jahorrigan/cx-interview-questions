import pytest
from shopping_basket import ZeroQuantityException, ProductDoesNotExistException

def test_empty_basket(empty_basket):
    """ Tests the return values from an empty basket """
    assert len(empty_basket.items) == 0
    assert empty_basket.item_count == 0
    assert empty_basket.sub_total == 0.00
    assert empty_basket.discount == 0.00
    assert empty_basket.total == 0.00

@pytest.mark.parametrize('product_name,quantity,exception', [
    ('Biscuits', 0, ZeroQuantityException(
        'Item quantity cannot be zero')),
    ('Biscuits', 6, None),
    ('Sardines', 3, None)
])
def test_add_new_basket_item(base_basket_1, product_name, quantity, exception):

    """ Tests the addition of a new basket item x quantity """

    # The basket starts with 2 individual items and 5 quantity
    assert len(base_basket_1.items) == 2
    assert base_basket_1.item_count == 5

    # Get existing quantity for item if any so that we can update
    product_name = product_name.strip()
    start_quantity = base_basket_1.items[product_name] if product_name \
        in base_basket_1.items.keys() else 0

    try:
        base_basket_1.add_new_basket_item(product_name, quantity)
    except ZeroQuantityException as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that product has been added
        assert base_basket_1.items[product_name] == start_quantity + quantity
        assert base_basket_1.item_count == 5 + quantity
        assert len(base_basket_1.items) == 2