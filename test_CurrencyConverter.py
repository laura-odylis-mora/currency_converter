from CurrencyConverter import *
import pytest
# Using pytest to create testing suite for all essential functions of CurrencyConverter.py

c = Converter()
main()


# def test_get_entry_value_integer():
#     assert c.get_entry_value(10) == 10.0


# def test_get_entry_value_letter():
#     assert c.get_entry_value("A") == None


# I think it has something to do with the face that rate_of_currency is in a differenct function but idk .
# # I keep getting "AttributeError: 'Converter' object has no attribute 'rate_of_currency'"  for all three tests below

def test_type_exchangerate():
    exchangerate = c.rate_of_currency.get_rate(
        "MXN", "JPY")
    assert isinstance(exchangerate, float) == True


def test_convert_function_integer_lowerRange():
    exchangerate = c.rate_of_currency().get_rate(
        "MXN", "JPY")
    assert c.convert_function(10, exchangerate) >= 63


def test_convert_function_integer_upperRange():
    exchangerate = c.rate_of_currency().get_rate(
        "MXN", "JPY")
    assert c.convert_function(10, exchangerate) >= 64

#  convert_function(self, x, exchange_rate):
#         converted_amount = x * exchange_rate
#         return converted_amount

# def test_final_amount():

#     final_amount = c.
# final_amount = round(self.convert_function(
#                         input_amount, exchange_rate), 2)


#pytest -m
# pytest interactive mode
