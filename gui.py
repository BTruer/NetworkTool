from logic import *
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyReconnaissance")

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.label = Gtk.Label()
        self.label.set_label("Please Enter A URL")
        self.label.set_halign(Gtk.Align.END)
    #    self.add(self.label)
        self.box.pack_start(self.label, True, True, 0)

        self.button = Gtk.Button(label="Enter")
        self.button.connect("clicked", self.button_clicked)
    #    self.add(self.button)
        self.box.pack_start(self.button, True, True, 0)

    def buttonClicked(self, widget):
        print()



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()