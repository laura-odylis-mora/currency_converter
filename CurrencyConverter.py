# This converter will convert between one world currency to another world currency
# choosing. The exchange rates are variable but they will be fixed from a certain
# source and date as noted on the converter; the converter provides an estimate.

# Structural Pattern Matching Sources
# ^[https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python]
# ^[https://docs.python.org/3/whatsnew/3.10.html]

# Library flag emojis
# ^[https://flag.readthedocs.io/en/latest/]
from signal import pause
from graphics import *
import flag

# import keyboard
from decimal import Decimal


# to import everyting defined in the module
from Button import Button
from EasyRectangle import EasyRectangle

# Exachange Rates and Converter Function API
#  ^[https://forex-python.readthedocs.io/en/latest/index.html]
from forex_python.converter import CurrencyRates


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
        # self.result_text.setText(float(result))

    # Clears the display of all text and unhilights buttons
    def clear(self):
        self.input_text.setText('')
        self.result_text.setText('')

    # Loop which runs the converter
    # Checks to see if the click was on a button

    def run(self, win):
        while True:
            country1 = ""
            country2 = ""
            p1 = win.getMouse()  # Waits for mouse click

            # Gets rate of currency
            rate_of_currency = CurrencyRates()

            # Input starting amount
            input_amount = self.get_entry_value(self.input_text)

            if self.clear_button.clicked(p1):
                self.clear()
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
            elif self.quit_button.clicked(p1):
                break
            elif self.usd_1_button.clicked(p1):
                country1 = 'USD'
                self.usd_1_button.changeFill('Gold')
            elif self.nzd_1_button.clicked(p1):
                country1 = 'NZD'
                self.nzd_1_button.changeFill('Gold')
            elif self.cad_1_button.clicked(p1):
                country1 = 'CAD'
                self.cad_1_button.changeFill('Gold')
            elif self.eur_1_button.clicked(p1):
                country1 = 'EUR'
                self.eur_1_button.changeFill('Gold')
            elif self.gbp_1_button.clicked(p1):
                country1 = 'GBP'
                self.gbp_1_button.changeFill('Gold')
            elif self.jpy_1_button.clicked(p1):
                country1 = 'JPY'
                self.jpy_1_button.changeFill('Gold')
            elif self.aud_1_button.clicked(p1):
                country1 = 'AUD'
                self.aud_1_button.changeFill('Gold')
            elif self.mxn_1_button.clicked(p1):
                country1 = 'MXN'
                self.mxn_1_button.changeFill('Gold')
            elif self.hkd_1_button.clicked(p1):
                country1 = 'HKD'
                self.hkd_1_button.changeFill('Gold')
            elif self.brl_1_button.clicked(p1):
                country1 = 'BRL'
                self.brl_1_button.changeFill('Gold')
            elif self.usd_2_button.clicked(p1):
                country2 = 'USD'
                self.usd_2_button.changeFill('Gold')
            elif self.nzd_2_button.clicked(p1):
                country2 = 'NZD'
                self.nzd_2_button.changeFill('Gold')
            elif self.cad_2_button.clicked(p1):
                country2 = 'CAD'
                self.cad_2_button.changeFill('Gold')
            elif self.eur_2_button.clicked(p1):
                country2 = 'EUR'
                self.eur_2_button.changeFill('Gold')
            elif self.gbp_2_button.clicked(p1):
                country2 = 'GBP'
                self.gbp_2_button.changeFill('Gold')
            elif self.jpy_2_button.clicked(p1):
                country2 = 'JPY'
                self.jpy_2_button.changeFill('Gold')
            elif self.aud_2_button.clicked(p1):
                country2 = 'AUD'
                self.aud_2_button.changeFill('Gold')
            elif self.mxn_2_button.clicked(p1):
                country2 = 'MXN'
                self.mxn_2_button.changeFill('Gold')
            elif self.hkd_2_button.clicked(p1):
                country2 = 'HKD'
                self.hkd_2_button.changeFill('Gold')
            elif self.brl_2_button.clicked(p1):
                country2 = 'BRL'
                self.brl_2_button.changeFill('Gold')
            elif self.convert_button.clicked(p1):
                # self.display_result(rate_of_currency.convert(
                #     country1, country2,  Decimal(input_amount)))
                # this displays the exchange rate, intermediary step
                exchange_rate = rate_of_currency.get_rate(country1, country2)

                self.display_result(exchange_rate)

                # code to use exchange rate to convert and display final amount
                final_amount = round(self.convert_function(
                    input_amount, exchange_rate), 2)

                self.display_result(final_amount)
            else:
                print("Convert/clear/quit button error")

                # FAKE STUFF
                # MORE FAKE STUFF


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
