class Basket:
    def __init__(self):
        # Initialise empty basket
        self.items = {}
        self.item_count = 0
        # Pre and post discount totals
        self.sub_total = 0.00
        self.discount = 0.00
        self.total = 0.00