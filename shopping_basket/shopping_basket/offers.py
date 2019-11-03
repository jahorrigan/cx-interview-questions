class TriggerVolumeException(Exception):
    pass

class DiscountUnitsException(Exception):
    pass

class DuplicateOfferException(Exception):
    pass

class OfferDoesNotExistException(Exception):
    pass

class Offers:
    def __init__(self):
        # Initialise empty offer list
        self.offers_list = {}
        self.offer_count = 0

    def add_new_offer(self, offer_name, product_name, trigger_volume,
        discount_units):
        offer_name = offer_name.strip()
        product_name = product_name.strip()
        if trigger_volume <= 0:
            # The trigger must be greater than zero
            raise TriggerVolumeException(
                f'The offer trigger volume cannot be zero'
            )
        if discount_units <= 0:
            # Chargeable units must be greater than zero
            raise DiscountUnitsException(
                f'The offer discount units cannot be zero'
            )
        if offer_name.lower() in [x.lower() for x in self.offers_list.keys()]:
            # This offer name already exists
            raise DuplicateOfferException(
                f'{offer_name} already exists in the offer list'
            )
        # This offer is valid so store in offers list
        self.offers_list[offer_name] = {
            'product_name': product_name,
            'trigger_volume': trigger_volume,
            'discount_units': round(discount_units, 2),
        }
        self.offer_count += 1

    def remove_existing_offer(self, offer_name):
        offer_name = offer_name.strip()
        if not offer_name.lower() in [x.lower() for x in self.offers_list.keys()]:
            # This offer name does not exist
            raise OfferDoesNotExistException(
                f'{offer_name} does not exist in offer list'
            )
        # This offer is valid and can be removed from the offer list
        del self.offers_list[offer_name]
        self.offer_count -= 1