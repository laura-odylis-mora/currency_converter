from CurrencyConverter import *
import pytest
# Using pytest to create testing suite for all essential functions of CurrencyConverter.py

conv = Converter()

currencyrates = CurrencyRates()


# I think it has something to do with the face that rate_of_currency is in a differenct function but idk .
# # I keep getting "AttributeError: 'Converter' object has no attribute 'rate_of_currency'"  for all three tests below

def test_type_exchangerate():
    exchangerate = currencyrates.get_rate(
        "MXN", "JPY")
    assert isinstance(exchangerate, float) == True


# The assertion exchangerate was obtained using
# ^[https://www.google.com/search?q=currency+converter&ei=VeNiYsuHMc2GptQPtramgAI&ved=0ahUKEwiLhvDKlqj3AhVNg4kEHTabCSAQ4dUDCA8&uact=5&oq=currency+converter&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEEMyBwgAELADEENKBAhBGABKBAhGGABQAFgAYJgEaAFwAXgAgAEAiAEAkgEAmAEAyAEKwAEB&sclient=gws-wiz]
# Tests exchangerate with +-2 error to account for the differences in daily and source based exchange rates
def test_convert_function_integer_lowerRange():
    exchangerate = currencyrates.get_rate(
        "MXN", "JPY")
    assert conv.convert_function(10, exchangerate) >= 62


def test_convert_function_integer_upperRange():
    exchangerate = currencyrates.get_rate(
        "MXN", "JPY")
    assert conv.convert_function(10, exchangerate) <= 65


def test_convert_function_float_lowerRange():
    exchangerate = currencyrates.get_rate(
        "MXN", "JPY")
    assert conv.convert_function(10.76, exchangerate) >= 67


def test_convert_function_float_upperRange():
    exchangerate = currencyrates.get_rate(
        "MXN", "JPY")
    assert conv.convert_function(10.76, exchangerate) <= 70


def test_convert_function_integer():
    assert conv.convert_function(10, 0.921) == 9.21


def test_convert_function_float():
    assert conv.convert_function(10.53, 0.921) == 9.698129999999999


def test_round_two_places_3dec():
    assert conv.round_two_places(0.921) == 0.92


def test_round_two_places_integer():
    assert conv.round_two_places(9) == 9.0


def test_round_two_places_0():
    assert conv.round_two_places(0.000967) == 0.0
