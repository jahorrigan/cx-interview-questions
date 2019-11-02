import pytest
from shopping_basket import Catalogue, DuplicateProductException, InvalidPriceException

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

@pytest.mark.parametrize('product_name,price,exception', [
    ('Sardines', 1.90, DuplicateProductException(
        'Sardines already exists in catalogue')),
    ('White Bread', '0.90', InvalidPriceException(
        'Price for White Bread must be a numeric decimal value')),
    ('Deodorant', 0.99, None)
])
def test_add_new_catalogue_product(base_products_catalogue, product_name, price, exception):

    """ Tests the addition of a new catalogue product """

    assert base_products_catalogue.product_count == 6

    try:
        base_products_catalogue.add_new_product(product_name, price)
    except (DuplicateProductException, InvalidPriceException) as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that product has been added
        assert base_products_catalogue.products[product_name] == price
        assert base_products_catalogue.product_count == 7