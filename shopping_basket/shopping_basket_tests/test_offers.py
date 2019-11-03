import pytest
from shopping_basket import TriggerVolumeException, DiscountUnitsException 
from shopping_basket import DuplicateOfferException, OfferDoesNotExistException

@pytest.mark.parametrize('offer_name,product_name,trigger_volume,\
    discount_units,exception', [
    ('Offer3', 'Biscuits', 0, 0.75, TriggerVolumeException(
        'The offer trigger volume cannot be zero')),
    ('Offer3', 'Biscuits', 3, 0, DiscountUnitsException(
        'The offer discount units cannot be zero')),
    ('Offer2', 'Biscuits', 3, 2, DuplicateOfferException(
        'Offer2 already exists in the offer list')),
    ('Offer3', 'Biscuits', 3, 2, None)
])
def test_add_new_offer(base_offers_list, offer_name, product_name, 
    trigger_volume, discount_units, exception):

    """ Tests the addition of a new offer """

    assert base_offers_list.offer_count == 2

    try:
        base_offers_list.add_new_offer(offer_name, product_name, trigger_volume,
            discount_units)
    except (TriggerVolumeException, DiscountUnitsException, 
        DuplicateOfferException) as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that offer has been added
        assert base_offers_list.offers_list[offer_name.strip()] == {
            'product_name': product_name.strip(),
            'trigger_volume': trigger_volume,
            'discount_units': round(discount_units, 2)
        }
        assert base_offers_list.offer_count == 3

@pytest.mark.parametrize('offer_name,exception', [
    ('Offer10', OfferDoesNotExistException(
        'Offer10 does not exist in offer list')),
    ('Offer1', None)
])
def test_remove_offer(base_offers_list, offer_name, exception):

    """ Tests the removal of an existing offer """

    assert base_offers_list.offer_count == 2

    try:
        base_offers_list.remove_existing_offer(offer_name)
    except OfferDoesNotExistException as inst:
        # Ensure correct exception type and message
        assert isinstance(inst, type(exception))
        assert inst.args == exception.args
    else:
        # No exception so test that offer has been removed
        assert offer_name.strip() not in base_offers_list.offers_list.keys()
        assert base_offers_list.offer_count == 1