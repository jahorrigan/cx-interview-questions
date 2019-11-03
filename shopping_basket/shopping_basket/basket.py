class ZeroQuantityException(Exception):
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