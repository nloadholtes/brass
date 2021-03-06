from Events import *
import time
import pyglet

timedelay = .3

class CPUSpinnerController(pyglet.event.EventDispatcher):
        """..."""
        def __init__(self, evManager):
                self.evManager = evManager
                self.evManager.registerObserver( self )

                self.keepGoing = 1
                CPUSpinnerController.register_event_type('key_pressed')

        def keyPress(self, pressed):
            self.dispatch_event('key_pressed', pressed)

        #----------------------------------------------------------------------
        def run(self):
                while self.keepGoing:
                        event = TickEvent()
                        time.sleep(timedelay)
                        self.evManager.notify( event )


        #----------------------------------------------------------------------
        def notify(self, event):
                if isinstance( event, QuitEvent ):
                        #this will stop the while loop from running
                        self.keepGoing = 0

