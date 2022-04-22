# currency_converter

# Calculate currency in different countries using Python.

This converter will convert between one world currency to another world currency choosing. The exchange rates are variable but they will be fixed from a certain source and date as noted on the converter; the converter provides an estimate.

The application should be accessed by first downloading all files, and then running ```python3 currencyconverter.py``` in the command line. The program will then open a window displaying the Currency Converter. The user should pick a starting and ending currency by clicking on the buttons in the window. THe user should then type into the text box on the top left, the starting amount of currency. This value should be a positive number (can be whole or decimal). Once two countries' currencies are chosen and the starting amount is inputted, the user should then click on the "convert" button. The converted currency amount will be displayed in the text box to the right of the input text box (top right).

## Instructions for Use (CurrencyConverter.py):
1. Change directory to folder you will keep all CurrencyConverter.py files:
    - EasyRectangle.py
    - Button.py
    - graphics.py
    - CurrencyConverter.py
    - test_CurrencyConverter.py
   All files will be included but are also included in the GitHub repository: https://github.com/laura-odylis-mora/currency_converter
2. Make sure all following libraries are installed in the command line:
      - flag
      - forex-python
   To do this run the follow commands:
      ```$ pip install emoji-country-flag```
      ```$ pip install forex-python```
3. In terminal run:
   ```$ python3 CurrencyConverter.py```
4. Pick (from the list on the left hand side) what country your starting currency is from. 
5. Pick (from the list on the right hand side) what country’s currency you would like to convert your currency amount to. 
6. Click, using your mouse, the button that reads “Convert”
7. On the top right text box, the output will be the Exchange Rate.
8. The formula for calculating exchange rate is: 
   Starting Currency Amount / Ending Currency Amount = Exchange Rate
9. This means that to convert starting currency to ending currency using Exchange Rate  would be:
		Starting Currency Amount / Exchange Rate = Ending Currency Amount


# Instructions to run test:
Note that one test will always fail. 
```FAILED test_CurrencyConverter.py::test - graphics.GraphicsError: getMouse in closed window```
This error is due to closing out of the graphics window in order to continue the other tests. Future goal would be to find new way to run tests using the ```graphics.py``` library.

1. Change directory to folder you will keep all CurrencyConverter.py files:
    - EasyRectangle.py
    - Button.py
    - graphics.py
    - CurrencyConverter.py
    - test_CurrencyConverter.py
   All files will be included but are also included in the GitHub repository: https://github.com/laura-odylis-mora/currency_converter
2. Make sure all following libraries are installed in the command line:
      - flag
      - forex-python
      - pytest
   To do this run the follow commands:
      ```$ pip install emoji-country-flag```
      ```$ pip install forex-python```
      ```$ pip install -U pytest```
3. In terminal run:
   ```$ pytest test_CurrencyConverter.py```
4. Exit out of Currency Converter Window using exit button (red "x" button on top right corner of window)
5. Exit out of graphics window using exit button (red "x" on top left side of graphics window)