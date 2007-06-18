from Events import *
import time

timedelay = .3

class CPUSpinnerController:
        """..."""
        def __init__(self, evManager):
                self.evManager = evManager
                self.evManager.registerObserver( self )

                self.keepGoing = 1

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