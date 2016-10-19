from unittest import TestCase
from harpia.GUI.components.colorfield import ColorField

class TestColorField(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        win = MainWindow()
        self.color_field = MainControl(win)

    # ----------------------------------------------------------------------x
    def get_type(self):
        self.color_field.get_type()

    # ----------------------------------------------------------------------x
    def get_value(self):
        self.color_field.get_value()

    # ----------------------------------------------------------------------x
    def on_choose_color(self):
        self.color_field.on_choose_color()

    