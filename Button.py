from graphics import *
from EasyRectangle import EasyRectangle

# Buttons are labeled rectangles
# that can detect if they have been clicked
# created undraw function for button


class Button:
    # Creates a rectangular button of specified width, height, and color
    # centered on (x_center,y_center) with specified label
    def __init__(self, x_center, y_center, width, height, color, slabel):
        self.rect = EasyRectangle(x_center, y_center, width, height)
        self.rect.setFill(color)
        p = Point(x_center, y_center)
        self.slabel = slabel
        self.label = Text(p, slabel)
        self.label.setSize(20)
        print('Button created:', slabel)

    def draw(self, win):
        self.rect.draw(win)
        self.label.draw(win)

    # Undraw buttown (created for Calculator.py Program)
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    # Returns True if pointer is inside button
    def clicked(self, pointer):
        if self.rect.is_in(pointer):
            print('Button clicked:', self.slabel)
            return True
        else:
            return False

    # New Function: Change fill of rect
    def changeFill(self, color):
        self.rect.setFill(color)
