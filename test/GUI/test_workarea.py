from unittest import TestCase
from harpia.GUI.workarea import WorkArea

class TestWorkArea(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        win = MainWindow()
        self.work_area = MainControl(win)

    # ----------------------------------------------------------------------x
    def add_diagram(self):
        self.work_area.add_diagram()

    # ----------------------------------------------------------------------x
    def close_tab(self):
        self.work_area.close_tab()

    # ----------------------------------------------------------------------x
    def get_current_diagram(self):
        self.work_area.get_current_diagram()

    # ----------------------------------------------------------------------x
    def rename_diagram(self):
        self.work_area.rename_diagram()

    # ----------------------------------------------------------------------x
    def resize(self):
        self.work_area.resize()

    # ----------------------------------------------------------------------x
    def close_tabs(self):
        self.work_area.close_tabs()

    