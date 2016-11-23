import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from harpia.GUI.fieldtypes import *
from harpia.GUI.components.field import Field


class ComboField(Field, Gtk.HBox):

    # ------------------------------------------------------------------------------

    def __init__(self, data, event):
        if not isinstance(data, dict):
            return

        self.check_value(data, "name", "")
        self.check_value(data, "value", "")
        self.check_value(data, "values", [])

        self.value = data["value"]
        Gtk.HBox.__init__(self, True)
        self.label = Gtk.Label(data["name"])
        self.label.set_property("halign", Gtk.Align.START)
        self.add(self.label)

        self.field = Gtk.ComboBoxText()
        self.field.set_entry_text_column(0)

        for value in data["values"]:
            self.field.append_text(value)
        if self.value in data["values"]:
            index = data["values"].index(self.value)
            self.field.set_active(index)
        if event is not None:
            self.field.connect("changed", event)
        self.add(self.field)
        self.show_all()

    # ------------------------------------------------------------------------------
    def get_type(self):
        return HARPIA_COMBO

    # ------------------------------------------------------------------------------
    def get_value(self):
        value = self.field.get_active_text()
        if value is not None:
            self.value = value
        return self.value

# ------------------------------------------------------------------------------
