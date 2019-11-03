import pytest
from shopping_basket import Basket

@pytest.fixture
def empty_basket():
    """ Returns an empty basket """
    return Basket()

@pytest.fixture
def base_basket_1(empty_basket):
    """ Returns an example base basket """
    empty_basket.add_new_basket_item('Baked Beans', 4)
    empty_basket.add_new_basket_item('Biscuits', 1)
    return empty_basket

@pytest.fixture
def base_basket_2(empty_basket):
    """ Returns an example base basket """
    empty_basket.add_new_basket_item('Baked Beans', 2)
    empty_basket.add_new_basket_item('Biscuits', 1)
    empty_basket.add_new_basket_item('Sardines', 2)
    return empty_basket

@pytest.fixture
def invalid_basket(empty_basket):
    """ Returns an invalid example base basket """
    empty_basket.add_new_basket_item('Biscuits', 1)
    empty_basket.add_new_basket_item('Flying Pig', 1)
    empty_basket.add_new_basket_item('Unicorn', 1)
    return empty_basket