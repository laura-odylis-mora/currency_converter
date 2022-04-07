# This converter will convert between one world currency to another world currency
# choosing. The exchange rates are variable but they will be fixed from a certain
# source and date as noted on the converter; the converter provides an estimate.

# to import everyting defined in the module
from graphics import *
from Button import Button
from EasyRectangle import EasyRectangle


class Converter:
    def __init__(self):
        self.convrect = EasyRectangle(0, 0, 176, 176)
        self.convrect.setFill('LightBlue')

        self.input_text1 = Entry(Point(-24, 26), 14)

        self.quit_button = Button(82, 82, 8, 8, 'Red', 'X')
        self.clear_button = Button(-23, 0, 30, 10, 'Light Green', 'Clear')

        #self.usd1_button = Button()

        self.result = EasyRectangle(0, -30, 60, 10)
        self.result.setFill('LightYellow')
        self.result_text = Text(Point(0, -24), '')

    def draw(self, win):
        self.convrect.draw(win)
        self.input_text1.draw(win)
        self.quit_button.draw(win)
        self.clear_button.draw(win)
        self.result_text.draw(win)

    # Loop which runs the converter
    # Checks to see if the click was on a button
    def run(self, win):
        while True:
            p = win.getMouse()  # Waits for mouse click

            x1 = self.get_entry_value(self.input_text1)


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
