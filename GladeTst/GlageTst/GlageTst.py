#!/usr/bin/env python
'''
Created on 31 мая 2021 г.

@author: grau
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Buglump:

    def on_window1_destroy(self, object, data=None):
        print( "quit with cancel")
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print ("quit from menu")
        Gtk.main_quit()

    def on_gtk_about_activate(self, menuitem, data=None):
        print ("help about selected")
        self.response = self.aboutdialog.run()
        self.aboutdialog.hide()
        
    def on_push_status_item_activate(self, menuitem, data=None):
        self.status_count += 1
        print(self.status_count)
        #self.statusbar.push(self.context_id, "Message number %s" % str(self.status_count))
        
    def on_pop_item_id_activate(self, menuitem, data=None):
        self.status_count -= 1
        print(self.status_count)
        
    
    def __init__(self):
        self.gladefile = "test2.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.aboutdialog = self.builder.get_object("MyAboutDialog")
        #self.context_id = self.statusbar.get_context_id("status")
        self.status_count = 0
        
        self.window = self.builder.get_object("window1")
        self.window.show()
    


if __name__ == '__main__':
    main = Buglump()
    Gtk.main()