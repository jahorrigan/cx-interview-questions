import pytest
from shopping_basket import Basket

@pytest.fixture
def empty_basket():
    """ Returns an empty basket """
    return Basket()

def test_empty_basket(empty_basket):
    """ Tests the return values from an empty basket """
    assert empty_basket.sub_total == 0.00
    assert empty_basket.discount == 0.00
    assert empty_basket.total == 0.00