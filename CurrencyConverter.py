# This converter will convert between one world currency to another world currency
# choosing. The exchange rates are variable but they will be fixed from a certain
# source and date as noted on the converter; the converter provides an estimate.

# Structural Pattern Matching Sources
# ^[https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python]
# ^[https://docs.python.org/3/whatsnew/3.10.html]

# Library flag emojis
# ^[https://flag.readthedocs.io/en/latest/]
from graphics import *
import flag

# to import everyting defined in the module
from Button import Button
from EasyRectangle import EasyRectangle

# Exachange Rates and Converter Function API
#  ^[https://forex-python.readthedocs.io/en/latest/index.html]
from forex_python.converter import CurrencyRates

# Create object of CurrencyRates class from forex-python
currencyRates = CurrencyRates()


class Converter:
    def __init__(self):
        # Create Buttons and set graphics window
        self.convrect = EasyRectangle(0, 0, 176, 176)
        self.convrect.setFill('LightBlue')

        self.input_text = Entry(Point(-50, 50), 14)

        self.quit_button = Button(82, 82, 8, 8, 'Red', 'X')
        self.clear_button = Button(0, 30, 18, 7, 'Ivory', 'Clear')

        self.convert_button = Button(0, 50, 24, 7, 'YellowGreen', 'Convert')

        self.result = EasyRectangle(50, 50, 28, 7)
        self.result.setOutline('GhostWhite')
        self.result.setFill('Gray')
        self.result_text = Text(Point(50, 50), '')

        self.instruct1 = Text(Point(-50, 20), 'Pick starting currency')
        self.instruct1.setSize(18)

        self.disclaimer = Text(
            Point(-35, 80), 'Currency Exchange Rates obtained from forex-python library')

        self.instruct2 = Text(Point(55, 20), 'Pick ending currency')
        self.instruct2.setSize(18)

        self.mxn_1_button = Button(-50, 10, 60, 7,
                                   'DarkSalmon', flag.flagize("Mexico MXN :MX:"))
        self.cad_1_button = Button(-50, 1, 60, 7,
                                   'DarkSalmon', flag.flagize("Canada CAD :CA:"))
        self.eur_1_button = Button(-50, -8, 60, 7,
                                   'DarkSalmon', flag.flagize("Eur. Union EUR :EU:"))
        self.gbp_1_button = Button(-50, -17, 60, 7,
                                   'DarkSalmon', flag.flagize("Great Britain GBP :GB:"))
        self.jpy_1_button = Button(-50, -26, 60, 7,
                                   'DarkSalmon', flag.flagize("Japan JPY :JP:"))
        self.aud_1_button = Button(-50, -35, 60, 7,
                                   'DarkSalmon', flag.flagize("Australia AUD :AU:"))
        self.brl_1_button = Button(-50, -44, 60, 7,
                                   'DarkSalmon', flag.flagize("Brazil BRL :BR:"))
        self.nzd_1_button = Button(-50, -53, 60, 7,
                                   'DarkSalmon', flag.flagize("New Zealand NZD :NZ:"))
        self.hkd_1_button = Button(-50, -62, 60, 7,
                                   'DarkSalmon', flag.flagize("Hong Kong HKD :HK:"))
        self.usd_1_button = Button(-50, -71, 60, 7,
                                   'DarkSalmon', flag.flagize("United States USD :US:"))

        self.mxn_2_button = Button(50, 10, 60, 7,
                                   'DarkSalmon', flag.flagize("Mexico MXN :MX:"))
        self.cad_2_button = Button(
            50, 1, 60, 7, 'DarkSalmon', flag.flagize("Canada CAD :CA:"))
        self.eur_2_button = Button(50, -8, 60, 7,
                                   'DarkSalmon', flag.flagize("Eur. Union EUR :EU:"))
        self.gbp_2_button = Button(50, -17, 60, 7,
                                   'DarkSalmon', flag.flagize("Great Britain GBP :GB:"))
        self.jpy_2_button = Button(
            50, -26, 60, 7, 'DarkSalmon', flag.flagize("Japan JPY :JP:"))
        self.aud_2_button = Button(50, -35, 60, 7,
                                   'DarkSalmon', flag.flagize("Australia AUD :AU:"))
        self.brl_2_button = Button(50, -44, 60, 7,
                                   'DarkSalmon', flag.flagize("Brazil BRL :BR:"))
        self.nzd_2_button = Button(50, -53, 60, 7,
                                   'DarkSalmon', 'New Zealand NZD')
        self.hkd_2_button = Button(
            50, -62, 60, 7, 'DarkSalmon', flag.flagize("Hong Kong HKD :HK:"))
        self.usd_2_button = Button(50, -71, 60, 7,
                                   'DarkSalmon', flag.flagize("United States USD :US:"))

    # Draw Buttons and Graphics Window

    def draw(self, win):
        self.convrect.draw(win)
        self.input_text.draw(win)
        self.quit_button.draw(win)
        self.clear_button.draw(win)
        self.result.draw(win)
        self.result_text.draw(win)
        self.convert_button.draw(win)
        self.instruct1.draw(win)
        self.instruct2.draw(win)
        self.mxn_1_button.draw(win)
        self.cad_1_button.draw(win)
        self.eur_1_button.draw(win)
        self.gbp_1_button.draw(win)
        self.jpy_1_button.draw(win)
        self.aud_1_button.draw(win)
        self.brl_1_button.draw(win)
        self.nzd_1_button.draw(win)
        self.hkd_1_button.draw(win)
        self.usd_1_button.draw(win)
        self.mxn_2_button.draw(win)
        self.cad_2_button.draw(win)
        self.eur_2_button.draw(win)
        self.gbp_2_button.draw(win)
        self.jpy_2_button.draw(win)
        self.aud_2_button.draw(win)
        self.brl_2_button.draw(win)
        self.nzd_2_button.draw(win)
        self.hkd_2_button.draw(win)
        self.usd_2_button.draw(win)
        self.disclaimer.draw(win)

    # Return input as Float otherwise statement about inputting numbers only
    def get_entry_value(self, entry):
        try:
            x = float(entry.getText())
            print(type(x))
        except:
            x = None
            print("Must be a number ")
        return x

    # Function that converts (amount) using exchange rate
    def convert_function(self, x, exchange_rate):
        converted_amount = x * exchange_rate
        return converted_amount

    # Display Result
    def display_result(self, result):
        self.result_text.setText(str(result))

    # Clears the display of all text and unhilights buttons
    def clear(self):
        self.input_text.setText('')
        self.result_text.setText('')

    # Method to get exchange rate from CurrencyRates object
    def get_exchange_rate(self, country1, country2):
        return currencyRates.get_rate(country1, country2)

    # Method to get input amount from user
    def get_input_amount(self):
        return self.get_entry_value(self.input_text)

    # Rounding the number to two decimal places
    def round_two_places(self, num):
        return round(num, 2)

    # Loop which runs the converter
    # Checks to see if the click was on a button

    def run(self, win):
        is_country1_set = False
        is_country2_set = False

        country1 = ""
        country2 = ""
        while True:

            p = win.getMouse()  # Waits for mouse click

            # Input starting amount
            input_amount = self.get_input_amount()

            if self.clear_button.clicked(p):
                self.clear()
                is_country1_set = False
                is_country2_set = False
                self.mxn_1_button.changeFill('DarkSalmon')
                self.cad_1_button.changeFill('DarkSalmon')
                self.eur_1_button.changeFill('DarkSalmon')
                self.gbp_1_button.changeFill('DarkSalmon')
                self.jpy_1_button.changeFill('DarkSalmon')
                self.aud_1_button.changeFill('DarkSalmon')
                self.brl_1_button.changeFill('DarkSalmon')
                self.nzd_1_button.changeFill('DarkSalmon')
                self.hkd_1_button.changeFill('DarkSalmon')
                self.usd_1_button.changeFill('DarkSalmon')
                self.mxn_2_button.changeFill('DarkSalmon')
                self.cad_2_button.changeFill('DarkSalmon')
                self.eur_2_button.changeFill('DarkSalmon')
                self.gbp_2_button.changeFill('DarkSalmon')
                self.jpy_2_button.changeFill('DarkSalmon')
                self.aud_2_button.changeFill('DarkSalmon')
                self.brl_2_button.changeFill('DarkSalmon')
                self.nzd_2_button.changeFill('DarkSalmon')
                self.hkd_2_button.changeFill('DarkSalmon')
                self.usd_2_button.changeFill('DarkSalmon')
            elif self.quit_button.clicked(p):
                break
            elif self.usd_1_button.clicked(p):
                country1 = 'USD'
                is_country1_set = True
                self.usd_1_button.changeFill('Gold')
            elif self.nzd_1_button.clicked(p):
                country1 = 'NZD'
                is_country1_set = True
                self.nzd_1_button.changeFill('Gold')
            elif self.cad_1_button.clicked(p):
                country1 = 'CAD'
                is_country1_set = True
                self.cad_1_button.changeFill('Gold')
            elif self.eur_1_button.clicked(p):
                country1 = 'EUR'
                is_country1_set = True
                self.eur_1_button.changeFill('Gold')
            elif self.gbp_1_button.clicked(p):
                country1 = 'GBP'
                is_country1_set = True
                self.gbp_1_button.changeFill('Gold')
            elif self.jpy_1_button.clicked(p):
                country1 = 'JPY'
                is_country1_set = True
                self.jpy_1_button.changeFill('Gold')
            elif self.aud_1_button.clicked(p):
                country1 = 'AUD'
                is_country1_set = True
                self.aud_1_button.changeFill('Gold')
            elif self.mxn_1_button.clicked(p):
                country1 = 'MXN'
                is_country1_set = True
                self.mxn_1_button.changeFill('Gold')
            elif self.hkd_1_button.clicked(p):
                country1 = 'HKD'
                is_country1_set = True
                self.hkd_1_button.changeFill('Gold')
            elif self.brl_1_button.clicked(p):
                country1 = 'BRL'
                is_country1_set = True
                self.brl_1_button.changeFill('Gold')
            elif self.usd_2_button.clicked(p):
                country2 = 'USD'
                is_country2_set = True
                self.usd_2_button.changeFill('Gold')
            elif self.nzd_2_button.clicked(p):
                country2 = 'NZD'
                is_country2_set = True
                self.nzd_2_button.changeFill('Gold')
            elif self.cad_2_button.clicked(p):
                country2 = 'CAD'
                is_country2_set = True
                self.cad_2_button.changeFill('Gold')
            elif self.eur_2_button.clicked(p):
                country2 = 'EUR'
                is_country2_set = True
                self.eur_2_button.changeFill('Gold')
            elif self.gbp_2_button.clicked(p):
                country2 = 'GBP'
                is_country2_set = True
                self.gbp_2_button.changeFill('Gold')
            elif self.jpy_2_button.clicked(p):
                country2 = 'JPY'
                is_country2_set = True
                self.jpy_2_button.changeFill('Gold')
            elif self.aud_2_button.clicked(p):
                country2 = 'AUD'
                is_country2_set = True
                self.aud_2_button.changeFill('Gold')
            elif self.mxn_2_button.clicked(p):
                country2 = 'MXN'
                is_country2_set = True
                self.mxn_2_button.changeFill('Gold')
            elif self.hkd_2_button.clicked(p):
                country2 = 'HKD'
                is_country2_set = True
                self.hkd_2_button.changeFill('Gold')
            elif self.brl_2_button.clicked(p):
                country2 = 'BRL'
                is_country2_set = True
                self.brl_2_button.changeFill('Gold')
            elif self.convert_button.clicked(p):
                print("Button \"convert\" clicked")
                # Tests if starting and ending currencies have been selected before converted
                if is_country1_set == True and is_country2_set == True:
                    exchange_rate = self.get_Exchange_rate(
                        country1, country2)
                    # code to use exchange rate to convert and display final amount
                    final_amount = self.round_two_places(self.convert_function(
                        input_amount, exchange_rate), 2)
                    # print converted amount in display box
                    self.display_result(final_amount)
                else:
                    print("Make sure you have selected starting and ending currencies.")
            else:
                print("Button error")


def main():
    # Creates a window and puts the converter object in it
    win = GraphWin('Currency Converter', 700, 700)
    win.setBackground('cornsilk')
    win.setCoords(-100, -100, 100, 100)

    conv = Converter()
    conv.draw(win)

    conv.run(win)

    win.close()


main()
