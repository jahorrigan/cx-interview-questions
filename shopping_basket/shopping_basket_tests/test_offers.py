import pytest
from shopping_basket import Offers

@pytest.fixture
def base_offers_list():
    """ Returns a base offers list containing two offers """
    offers_list = Offers()
    offers_list.add_new_offer('Offer1', 'Baked Beans', 2, 1)
    offers_list.add_new_offer('Offer2', 'Sardines', 1, 0.75)
    return offers_list

@pytest.mark.parametrize('offer_name,product_name,trigger_volume,\
    chargeable_units,exception', [
    ('Offer3', 'Biscuits', 0, 0.75, TriggerVolumeException(
        'The offer trigger volume cannot be zero')),
    ('Offer3', 'Biscuits', 3, 0, ChargeableUnitsException(
        'The offer chargeable units cannot be zero')),
    ('Offer2', 'Biscuits', 3, 2, DuplicateOfferException(
        'Offer2 already exists in the offer list')),
    ('Offer3', 'Biscuits', 3, 2, None)
])
def test_add_new_offer(base_offers_list, offer_name, product_name, 
    trigger_volume, chargeable_units, exception):

    """ Tests the addition of a new offer """

    assert base_offers_list.offer_count == 2

    try:
        base_offers_list.add_new_offer(product_name, trigger_volume,
            chargeable_units)
    except (TriggerVolumeException, ChargeableUnitsException, 
        DuplicateOfferException) as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that offer has been added
        assert base_offers_list.offers_list[offer_name.strip()] == {
            'trigger_volume': trigger_volume,
            'chargeable_units': round(chargeable_units, 2)
        }
        assert base_offers_list.offer_count == 3