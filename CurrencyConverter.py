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
            Point(-35, 80), 'Currency Rate as of \" Insert Date \". Currency rates subject to change')

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
        except:
            x = None
            self.result_text.setText("Input must be a number")
        return x

    # Display Result

    def display_result(self, result):
        self.result_text.setText(str(result))
        # self.result_text.setText(float(result))

    # Clears the display of all text
    def clear(self):
        self.input_text.setText('')
        self.result_text.setText('')

    # Highlight chosen button when button clicked
    def highlightButton(self, country):
        self.country.setFill('DarkSalmon')

    # Unhighlight buttons when "clear" function runs
    def unhighlightButton(self, country):
        self.country.setFill('Gold')

    # Loop which runs the converter
    # Checks to see if the click was on a button

    def run(self, win):
        while True:
            rate_of_currency = CurrencyRates()
            x1 = self.get_entry_value(self.input_text1)
            input_amount = self.get_entry_value(self.input_text)
            print(type(input_amount))
            value = input_amount

            print(type(input_amount))
            country1 = ""
            country2 = ""
            p1 = win.getMouse()  # Waits for mouse click

            if self.clear_button.clicked(p1):
                self.clear()
            elif self.usd_1_button.clicked(p1):
                country1 = 'USD'
            elif self.nzd_1_button.clicked(p1):
                country1 = 'NZD'
            elif self.cad_1_button.clicked(p1):
                country1 = 'CAD'
            elif self.eur_1_button.clicked(p1):
                country1 = 'EUR'
            elif self.gbp_1_button.clicked(p1):
                country1 = 'GBP'
            elif self.jpy_1_button.clicked(p1):
                country1 = 'JPY'
            elif self.aud_1_button.clicked(p1):
                country1 = 'AUD'
            elif self.mxn_1_button.clicked(p1):
                country1 = 'MXN'
            elif self.hkd_1_button.clicked(p1):
                country1 = 'HKD'
            elif self.brl_1_button.clicked(p1):
                country1 = 'BRL'
            elif self.quit_button.clicked(p1):
                break
            else:  # write errror message saying pick what country's currency you starting with
                print('some error message')

            p2 = win.getMouse()

            if self.clear_button.clicked(p2):
                self.clear()
            elif self.quit_button.clicked(p2):
                break
            elif self.usd_2_button.clicked(p2):
                country2 = 'USD'
            elif self.nzd_2_button.clicked(p2):
                country2 = 'NZD'
            elif self.cad_2_button.clicked(p2):
                country2 = 'CAD'
            elif self.eur_2_button.clicked(p2):
                country2 = 'EUR'
            elif self.gbp_2_button.clicked(p2):
                country2 = 'GBP'
            elif self.jpy_2_button.clicked(p2):
                country2 = 'JPY'
            elif self.aud_2_button.clicked(p2):
                country2 = 'AUD'
            elif self.mxn_2_button.clicked(p2):
                country2 = 'MXN'
            elif self.hkd_2_button.clicked(p2):
                country2 = 'HKD'
            elif self.brl_2_button.clicked(p2):
                country2 = 'BRL'
            else:
                print("Change this to warning")

            p3 = win.getMouse()

            if self.clear_button.clicked(p3):
                self.clear()
            elif self.quit_button.clicked(p3):
                break
            elif self.convert_button.clicked(p3):
                check_float = isinstance(input_amount, float)
                if check_float == True:
                    print(rate_of_currency.convert(
                        country1, country2, value))

            else:
                print("Change this to warning")


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
