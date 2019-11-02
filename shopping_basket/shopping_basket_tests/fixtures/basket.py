import pytest
from shopping_basket import Basket

@pytest.fixture
def empty_basket():
    """ Returns an empty basket """
    return Basket()