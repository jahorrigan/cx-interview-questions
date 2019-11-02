class TriggerVolumeException(Exception):
    pass

class ChargeableUnitsException(Exception):
    pass

class DuplicateOfferException(Exception):
    pass

class Offers:
    def __init__(self):
        # Initialise empty offer list
        self.offers_list = {}
        self.offer_count = 0

    def add_new_offer(self, offer_name, product_name, trigger_volume,
        chargeable_units):
        offer_name = offer_name.strip()
        product_name = product_name.strip()
        if trigger_volume <= 0:
            # The trigger must be greater than zero
            raise TriggerVolumeException(
                f'The offer trigger volume cannot be zero'
            )
        if chargeable_units <= 0:
            # Chargeable units must be greater than zero
            raise ChargeableUnitsException(
                f'The offer chargeable units cannot be zero'
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
            'chargeable_units': round(chargeable_units, 2),
        }
        self.offer_count += 1