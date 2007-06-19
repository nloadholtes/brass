import pygame
from pygame.constants import *
from Events import *

door = 1
npc = 0
group = 2
obj_no_msg = 3
obj_msg = 4
ok_to_move = 0
ask_to_move = 1

class TileSprite:
	def __init__(self, imageFilename, parent, x, y, type):
		if imageFilename:
			image = pygame.image.load(imageFilename)
			image.set_colorkey( (0, 0, 0, 0), RLEACCEL)
			self._image = image.convert()
		else: self._image = None
		self._parent = parent
		self._x = int(x)
		self._y = int(y)
		self._type = type
		self._doordata = None
	
	def handle(self):
		'''In the event of someone hitting this tile, we need to decide what to do.'''
		typ = self._type
		if typ == door:
			print 'Door'
			d = self._parent._mapinfo['door'][self.getDoorData()]
			if d[2] == ok_to_move:
				return self._parent.moveToNewRoom(d)
			elif d[2] == ask_to_move:
				print "We gotta ask about this move"
		elif typ == npc:
			print 'NPC standing there'
			ev = Encounter(self)
			self._parent.notify(ev)
		elif typ == obj_no_msg:
			print 'Object with no message'
			
		elif typ == obj_msg:
			print "An object with a message of:"
			
			
		
	def getXY(self):
		return (self._x, self._y)
	
##	def setDoorData(self, dat):
##		self._doordata = dat
		
##	def getDoorData(self):
##		return self._doordata

	def getType(self):
		return self._type
	
	def move(self, direction):
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
			screen.blit(self._image, location)

	def occupied(self, intruder):
		return 0
