from CurrencyConverter import *
import pytest
# Using pytest to create testing suite for all essential functions of CurrencyConverter.py


def test_get_entry_value_integer(self):
    assert self.get_entry_value(10) == 10.0


def test_get_entry_value_letter(self):
    assert self.get_entry_value("A") == None

# test type exchange_rate

#pytest -mc
# pytrst interactive mode

# Can use this To test instance of input
# def get_entry_value(self, entry):
    #     print("Input Starting Value (Whole Number): ")
    #     x = str(entry.getText())
    # # checking type
    # # ^[https://www.adamsmith.haus/python/answers/how-to-check-if-a-number-is-an-int-or-float-in-python#:~:text=Use%20isinstance()%20to%20check,of%20classinfo%20and%20False%20otherwise.]
    #     # check_int = isinstance(x, int)
    #     # while check_int == False:
    #     #     self.result_text.setText("Input must be a positive integer.")
    #     #     x = int(entry.getText())
