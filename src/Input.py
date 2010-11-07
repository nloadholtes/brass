#
# This class handles the input from the user
#

from Events import *

class Input:
    def __init__(self, manager, gtk):
        self.manager = manager
        self.manager.registerObserver(self)
        self.gtk = gtk

    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in self.gtk.getEvent():
                ev = None
                if event.type == self.gtk.k_quit:
                    ev = QuitEvent()
                elif event.type == self.gtk.k_keydown: 
                    if event.key == self.gtk.k_escape:
                        ev = QuitEvent()
                    elif event.key == self.gtk.k_up:
                        ev = CharMoveRequestEvent("up")
                    elif event.key == self.gtk.k_left:
                        ev = CharMoveRequestEvent("left")
                    elif event.key == self.gtk.k_down:
                        ev = CharMoveRequestEvent("down")
                    elif event.key == self.gtk.k_right:
                        ev = CharMoveRequestEvent("right")
                    #Need other cases here to catch user input for battles, etc
                        
                if ev:
                    self.manager.notify(ev)
