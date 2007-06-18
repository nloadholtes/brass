#
# This is the manager for events. It allows sections to communicate with each other
# without knowing about each other. (i.e. it helps to enforce the MVC)
#

#from weakref import WeakKeyDictionary #this isn't working on the Mac for some reason

class EventManager:
    def __init__(self):
        self.observers = {}

    def registerObserver(self, observer):
        if observer not in self.observers.keys():
            self.observers[observer]  = 1

    def removeObserver(self, observer):
        if observer in self.observers.keys():
            del self.observers[observer]
            
    def notify(self, event):
        for observer in self.observers.keys():
            #If the weakref has died, remove it and continue 
            #through the list
            if observer is None:
                del observer
                continue
            else:
                observer.notify(event)
