from unittest import TestCase
from harpia.GUI.components.checkfield import CheckField

class TestCheckField(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        win = MainWindow()
        self.check_field = MainControl(win)

    # ----------------------------------------------------------------------x
    def get_type(self):
        self.check_field.get_type()

    # ----------------------------------------------------------------------x
    def get_value(self):
        self.check_field.get_value()

    