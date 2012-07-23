from Events import *
from gui.GUIToolkit import GUIToolkit

door = 1
npc = 0
group = 2
obj_no_msg = 3
obj_msg = 4
ok_to_move = 0
ask_to_move = 1

class TileSprite:
        def __init__(self, manager,  imageFilename, parent, x, y, gtk):
                self.gtk = gtk
                if imageFilename:
                        self._image = self.gtk.getImage(imageFilename)
                else: self._image = None
                self._parent = parent
                self._x = int(x)
                self._y = int(y)
                self._doordata = None
                self.manager = manager

        def handle(self):
                '''In the event of someone hitting this tile, we need to decide what to do.'''
                self.printm("Default TileSprite handler: Need to replace this with a specific handler.")


        def printm(self, text):
                '''A helper method to print out messages'''
                self.manager.notify(PrintEvent(text))

        def getXY(self):
                return (self._x, self._y)

        def move(self, direction):
                print "TileSprite.move() was called, and this might probably shouldn't have happened..."
                dx,dy = direction
                newX = self._x + dx
                newY = self._y + dy
                result = self._parent.moveOk(newX, newY)
                if result == None:
                        self._x += dx
                        self._y += dy
                return result

        def paint(self, screen, location):
                if(self._image):
                        self._image.blit(location[0], location[1])

        def occupied(self, intruder):
                if (self._x, self._y) == intruder:
			return True
		return False
