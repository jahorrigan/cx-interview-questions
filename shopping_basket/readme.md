# Shopping Basket Library Documentation

## Requirements

- python 3.7
- pytest 5.2.2
- pytest-cov 2.8.1
- [https://github.com/kennethreitz/pipenv](pipenv) for environment and dependency management

## Setup

To create a virtual environment running Python 3.7:

`pipenv install`

To create a virtual environment with development support for testing:

`pipenv install --dev`

## Testing

To run tests and coverage results:

`pytest -v --cov=shopping_basket`

## Usage

View and run a test script to execute the main features of the library:

`python shopping_example.py`

To include the shopping basket library in your script:

`import shopping_basket as sd`

The shopping basket library has three main entities which are:

## Catalogue

To create an empty catalogue object run:

`catalogue = sd.Catalogue()`

To add a product and price to the catalogue:

*Parameters: product name, price*

`catalogue.add_new_product('Baked Beans', 0.99)`

To remove a product from the catalogue:

`catalogue.remove_existing_product('Baked Beans')`

***Exceptions***
- DuplicateProductException - If a product to be added already exists
- InvalidPriceException - If a price to be added is invalid
- ProductDoesNotExistException - If a product to be removed does not exist

## Offers

To create an empty offers object run:

`offers = sd.Offers()`

To add an offer to the offer list:

*Parameters: offer name, product name, trigger volume, discount_units*

`offers.add_new_offer('Offer1', 'Baked Beans', 3, 1)`

*For example: Buy 2 get 1 free would have a trigger volume of 3, and a discount unit of*
*1. Therefore every 3 items, 1 item is discounted*

To remove an offer from the offer list:

`offers.remove_existing_offer('Offer1')`

***Exceptions***
- TriggerVolumeException - If a trigger volume to be added is <= 0
- DiscountUnitsException - If a discount unit to be added is <= 0
- DuplicateOfferException - If an offer name to be added already exists
- OfferDoesNotExistException - If an offer to be removed does not exist

## Basket

To create an empty shopping basket object run:

`basket = sd.Basket()`

To add an item to the basket:

*Parameters: item name, quantity*

`basket.add_new_basket_item('Baked Beans', 4)`

To remove an item from the basket:

`basket.remove_basket_item('Baked Beans')`

To calculate and return the basket sub-total, discount and total:

*Parameters: catalogue, offers*

`basket.calculate_basket_discount(catalogue, offers)`

***Exceptions***
- ZeroQuantityException - If an item to be added has zero quantity
- ItemDoesNotExistException - If an item to be removed does not exist
- InvalidBasketException - If an item in the basket does not exist in the catalogue
- NegativeBasketException - If the basket total is a negative value