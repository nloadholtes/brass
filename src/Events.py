#
# This is all of the events that can be fired off
#

class Event:
    def __init__(self):
        self.name = "Base Event Class"

class QuitEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Quit Event"
        
class TickEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Tick Event"

class CharMoveRequestEvent(Event):
    def __init__(self, direction):
        Event.__init__(self)
        self.name = "Char Move Request Event"
        self.direction = direction

class CharMoveEvent(Event):
    def __init__(self):
        Event.__init__(self)
        self.name = "Char Move Event"

class CharPlaceEvent(Event):
    def __init__(self):
        Event.__init__(self)        
        self.name = "Char Place Event"
            
class Encounter(Event):
    def __init__(self, entity):
        Event.__init__(self)
        self.name = "Encounter"
        self.entity = entity

class PrintEvent(Event):
    def __init__(self, text):
        Event.__init__(self)        
        self.name = "Print Event"
        self.text = text
            


