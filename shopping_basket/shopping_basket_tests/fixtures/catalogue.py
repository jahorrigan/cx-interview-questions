import pytest
from shopping_basket import Catalogue

@pytest.fixture
def base_products_catalogue():
    """ Returns a base catalogue containing six products """
    catalogue = Catalogue()
    catalogue.add_new_product('Baked Beans', 0.99)
    catalogue.add_new_product('Biscuits', 1.20)
    catalogue.add_new_product('Sardines', 1.89)
    catalogue.add_new_product('Shampoo (Small)', 2.00)
    catalogue.add_new_product('Shampoo (Medium)', 2.50)
    catalogue.add_new_product('Shampoo (Large)', 3.50)    
    return catalogue

@pytest.fixture
def negative_products_catalogue():
    """ Returns a catalogue with negative priced products """
    catalogue = Catalogue()
    catalogue.add_new_product('Jam', -0.50)
    catalogue.add_new_product('Ice Cream', -1.79)
    catalogue.add_new_product('Sardines', 1.89)
    return catalogue