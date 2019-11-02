import pytest
from shopping_basket import Offers

@pytest.fixture
def base_offers_list():
    """ Returns a base offers list containing two offers """
    offers_list = Offers()
    offers_list.add_new_offer('Offer1', 'Baked Beans', 2, 1)
    offers_list.add_new_offer('Offer2', 'Sardines', 1, 0.75)
    return offers_list