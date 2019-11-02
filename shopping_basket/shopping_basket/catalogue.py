class DuplicateProductException(Exception):
    pass

class InvalidPriceException(Exception):
    pass

class ProductDoesNotExistException(Exception):
    pass

class Catalogue:
    def __init__(self):
        # Initialise empty catalogue
        self.products = {}
        self.product_count = 0

    def add_new_product(self, product_name, price):
        product_name = product_name.strip()
        if product_name.lower() in [x.lower() for x in self.products.keys()]:
            # This product name already exists
            raise DuplicateProductException(
                f'{product_name} already exists in catalogue'
            )
        if not isinstance(price, float):
            # This price is in invalid format 
            raise InvalidPriceException(
                f'Price for {product_name} must be a numeric decimal value'
            )
        # This product is valid so store in catalogue
        self.products[product_name] = round(price, 2)
        self.product_count += 1

    def remove_existing_product(self, product_name):
        product_name = product_name.strip()
        if not product_name.lower() in [x.lower() for x in self.products.keys()]:
            # This product name does not exist
            raise ProductDoesNotExistException(
                f'{product_name} does not exist in catalogue'
            )
        # This product is valid and can be removed from catalogue
        del self.products[product_name]
        self.product_count -= 1