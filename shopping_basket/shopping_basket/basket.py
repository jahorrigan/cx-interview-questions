from math import ceil

class ZeroQuantityException(Exception):
    pass

class ItemDoesNotExistException(Exception):
    pass

class InvalidBasketException(Exception):
    pass

class NegativeBasketException(Exception):
    pass

class Basket:
    def __init__(self):
        # Initialise empty basket
        self.items = {}
        self.item_count = 0
        # Pre and post discount totals
        self.sub_total = 0.00
        self.discount = 0.00
        self.total = 0.00

    def add_new_basket_item(self, item_name, quantity):
        item_name = item_name.strip()
        if quantity <= 0:
            # The quantity to be added must be greater than zero
            raise ZeroQuantityException(
                f'Item quantity cannot be zero'
            )
        if item_name.lower() in [x.lower() for x in self.items.keys()]:
            # This item name already exists so update quantity
            self.items[item_name] += quantity
        else:
            # This is a new basket item so store
            self.items[item_name] = quantity
        # Finally update item_count
        self.item_count += quantity

    def remove_basket_item(self, item_name):
        item_name = item_name.strip()
        if not item_name.lower() in [x.lower() for x in self.items.keys()]:
            # This item name does not exist
            raise ItemDoesNotExistException(
                f'{item_name} does not exist in basket'
            )
        # This item name exists so remove and update item count
        self.item_count -= self.items[item_name]
        del self.items[item_name]

    def calculate_basket_discount(self, catalogue, offers) -> dict:
        # Ensure we are starting from zero
        self.sub_total = 0.00
        self.discount = 0.00
        self.total = 0.00
        
        # Cycle through basket items, return zeroes if empty
        for item_name, quantity in self.items.items():
            # Is this product in the catalogue?
            if item_name in catalogue.products.keys():
                price = catalogue.products[item_name]
                self.sub_total += quantity * price
                # Is there an offer for this product
                for offer_name, offer_dict in offers.offers_list.items():
                    # Use first offer we find
                    # TODO: How do we handle multiple offers for same item?
                    if offer_dict['product_name'] == item_name:
                        # There is an offer for this item apply discount
                        for x in range(1, quantity + 1):
                            # Loop through quantity and apply discount at each trigger
                            if x % offer_dict['trigger_volume'] == 0:
                                self.discount += price * offer_dict['discount_units']
                        break
            else:
                # Handle missing catalogue product error
                raise InvalidBasketException(
                    f'Invalid basket items do not exist in catalogue'
                )

        # Now calculate final total
        self.sub_total = round(self.sub_total, 2)
        self.discount = ceil(self.discount * 100) / 100.0 # Maximum discount
        self.total = round(self.sub_total - self.discount, 2)

        # Basket total should not be negative
        if self.total < 0:
            raise NegativeBasketException(
                f'Basket total cannot be negative'
            )

        return {
            'sub-total': '£' + str(self.sub_total),
            'discount': '£' + str(self.discount),
            'total': '£' + str(self.total),
        }