import pytest
from shopping_basket import Catalogue

@pytest.fixture
def no_products_catalogue():
    """ Returns an empty catalogue """
    return Catalogue()
