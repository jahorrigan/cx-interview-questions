# Shopping Basket Library Documentation

## Requirements

- python 3.7
- pytest 5.2.2
- pytest-cov 2.8.1
- [https://github.com/kennethreitz/pipenv](pipenv) for environment and dependency management

## Setup

pipenv install - to setup virtual environment with python 3.7
pipenv install --dev - to add testing and linting libraries to environment

## Usage

python shopping_example.py
View and run shopping_example.py to run a test to populate data and test discount response

To include the shopping_basket library in your script add:

import shopping basket as sd

The shopping basket library has three main entities which are:

## Catalogue

To create an empty catalogue object run:
catalogue = sd.Catalogue()

## Offers

To create an empty offers object run:
offers = sd.Offers()

## Basket

To create an empty shopping basket object run:
basket = sd.Basket()

