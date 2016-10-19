from unittest import TestCase
from harpia.model.preferences import Preferences

class TestPlugin(TestCase):

    def setUp(self):
        """Do the test basic setup."""
        win = MainWindow()
        self.preferences = MainControl(win)

    # ----------------------------------------------------------------------x
    def get_recent_files(self):
        self.preferences.get_recent_files()

    # ----------------------------------------------------------------------x
    def get_recent_files_as_array(self):
        self.preferences.get_recent_files_as_array()

    # ----------------------------------------------------------------------x
    def add_recent_file(self):
        self.preferences.add_recent_file()

    # ----------------------------------------------------------------------x
    def get_default_directory(self):
        self.preferences.get_default_directory()

    # ----------------------------------------------------------------------x
    def set_default_directory(self):
        self.preferences.set_default_directory()

    # ----------------------------------------------------------------------x
    def get_default_filename(self):
        self.preferences.get_default_filename()

    # ----------------------------------------------------------------------x
    def set_default_filename(self):
        self.preferences.set_default_filename()

    # ----------------------------------------------------------------------x
    def get_error_log_file(self):
        self.preferences.get_error_log_file()

    # ----------------------------------------------------------------------x
    def set_error_log_file(self):
        self.preferences.set_error_log_file()

    # ----------------------------------------------------------------------x
    def get_width(self):
        self.preferences.get_width()

    # ----------------------------------------------------------------------x
    def set_width(self):
        self.preferences.set_width()

    # ----------------------------------------------------------------------x
    def get_height(self):
        self.preferences.get_height()

    # ----------------------------------------------------------------------x
    def set_height(self):
        self.preferences.set_height()

    # ----------------------------------------------------------------------x
    def get_hpaned_work_area(self):
        self.preferences.get_hpaned_work_area()

    # ----------------------------------------------------------------------x
    def set_hpaned_work_area(self):
        self.preferences.set_hpaned_work_area()

    # ----------------------------------------------------------------------x
    def get_vpaned_bottom(self):
        self.preferences.get_vpaned_bottom()

    # ----------------------------------------------------------------------x
    def set_vpaned_bottom(self):
        self.preferences.set_vpaned_bottom()

    # ----------------------------------------------------------------------x
    def get_vpaned_left(self):
        self.preferences.get_vpaned_left()

    # ----------------------------------------------------------------------x
    def set_vpaned_left(self):
        self.preferences.set_vpaned_left()

    