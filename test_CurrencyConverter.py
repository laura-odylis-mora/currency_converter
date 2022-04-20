from CurrencyConverter import *
import pytest
# Using pytest to create testing suite for all essential functions of CurrencyConverter.py

c = Converter()


def test_get_entry_value_integer():
    assert c.get_entry_value(10) == 10.0


def test_get_entry_value_letter():
    assert c.get_entry_value("A") == None


def test_type_exchangerate():
    exchangerate = c.rate_of_currency.get_rate(
        "MXN", "JPY")
    assert isinstance(exchangerate, float) == True


#pytest -m
# pytest interactive mode
