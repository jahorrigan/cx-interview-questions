import shopping_basket as sb

class Test():

    """ Example test class based on example test parameters in git repo """

    def __init__(self):
        # Initialise empty objects
        self.catalogue = sb.Catalogue()
        self.offers = sb.Offers()
        self.basket_1 = sb.Basket()
        self.basket_2 = sb.Basket()

    def fill_catalogue(self):
        """ Add products to catalogue, duplicate products should be rejected """
        print('Populating catalogue...')
        try:
            self.catalogue.add_new_product('Baked Beans', 0.99)
            self.catalogue.add_new_product('Biscuits', 1.20)
            self.catalogue.add_new_product('Sardines', 1.89)
            self.catalogue.add_new_product('Shampoo (Small)', 2.00)
            self.catalogue.add_new_product('Shampoo (Medium)', 2.50)
            self.catalogue.add_new_product('Shampoo (Large)', 3.50)
            self.catalogue.add_new_product('Ice Cream', -1.00)
            self.catalogue.add_new_product('Biscuits', 1.20)
        except Exception as e:
            print(f'Exception adding product to catalogue: {e}')
        print(f'{len(self.catalogue.products)} items added to catalogue')

    def fill_offers(self):
        """ Add offers to offers_list """
        print('Populating offers...')
        try:
            self.offers.add_new_offer('Offer1', 'Baked Beans', 3, 1)
            self.offers.add_new_offer('Offer2', 'Sardines', 1, 0.25)
            self.offers.add_new_offer('Offer2', 'Biscuits', 1, 0.25)
        except Exception as e:
            print(f'Exception adding offer to offer list: {e}')
        print(f'{len(self.offers.offers_list)} offers added to offers list')

    def fill_basket(self, basket: object, item_list: dict):
        """ Fill a specified basket with a list of items """
        for item_name, quantity in item_list.items():
            try:
                basket.add_new_basket_item(item_name, quantity)
            except Exception as e:
                print(f'Exception adding item to basket: {e}')
        print(f'{len(basket.items)} items added to basket')

    def get_basket_discount(self, basket: object):
        """ Get the sub-total, disocunt and total amount for specified basket """
        response = basket.calculate_basket_discount(self.catalogue, self.offers)
        return response

if __name__ == '__main__':

    test = Test()

    # Populate catalogue
    test.fill_catalogue()

    # Populate offers
    test.fill_offers()

    # Test basket 1 discount
    print(f'Testing basket 1...')
    test.fill_basket(test.basket_1, {
        'Baked Beans': 4,
        'Biscuits': 1,
        'Sardines': 0,
    })
    
    # Get and display basket 1 discount
    print('Requesting discount details for basket 1...')
    try:
        basket_1_discount = test.get_basket_discount(test.basket_1)
        print(basket_1_discount)
    except Exception as e:
        print(f'Exception getting basket discount details: {e}')

    # Test basket 2 discount
    print(f'Testing basket 2...')
    test.fill_basket(test.basket_2, {
        'Baked Beans': 2,
        'Biscuits': 1,
        'Sardines': 2,
    })

    # Get and display basket 2 discount
    print('Requesting discount details for basket 2...')
    try:
        basket_2_discount = test.get_basket_discount(test.basket_2)
        print(basket_2_discount)
    except Exception as e:
        print(f'Exception getting basket discount details: {e}')


