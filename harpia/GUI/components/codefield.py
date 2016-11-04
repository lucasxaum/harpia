import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GtkSource
from harpia.GUI.fieldtypes import *
from harpia.GUI.components.field import Field


class CodeField(Field, Gtk.VBox):

    # --------------------------------------------------------------------------

    def __init__(self, data, event):
        if not isinstance(data, dict):
            return
        Gtk.VBox.__init__(self)

        self.check_value(data, "label", "")
        self.check_value(data, "value", "")
        self.check_value(data, "height", 80)
        self.check_value(data, "width", 50)
        self.check_value(data, "language", "c")

        self.set_homogeneous(False)
        self.set_spacing(10)
        scrolled_window = Gtk.ScrolledWindow()

        scrolled_window.set_min_content_height(data["height"])
        scrolled_window.set_min_content_width(data["width"])

        scrolled_window.set_shadow_type(Gtk.ShadowType.ETCHED_IN)

        self.label = Gtk.Label(data["label"])
        self.label.set_property("halign", Gtk.Align.START)
        self.pack_start(self.label, False, False, 0)

        lang_manager = GtkSource.LanguageManager()
        self.text_buffer = GtkSource.Buffer.new_with_language(
                lang_manager.get_language(data["language"]))
        textview = GtkSource.View.new_with_buffer(self.text_buffer)
        textview.set_show_line_numbers(True)
        textview.set_left_margin(10)
        textview.set_right_margin(10)
        textview.get_buffer().set_text(data["value"])

        textview.set_wrap_mode(Gtk.WrapMode.WORD)
        if event is not None:
            self.field.connect("focus-out-event", event)

        scrolled_window.add(textview)

        self.pack_start(scrolled_window, True, True, 0)
        self.show_all()

    # --------------------------------------------------------------------------
    def get_type(self):
        return HARPIA_CODE

    # --------------------------------------------------------------------------
    def get_value(self):
        return self.text_buffer.get_text(
            self.text_buffer.get_start_iter(),
            self.text_buffer.get_end_iter(),
            True)

    # --------------------------------------------------------------------------
    def set_value(self, value):
        self.text_buffer.set_text(value)

# ------------------------------------------------------------------------------