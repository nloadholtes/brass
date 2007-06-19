from Character import *
from EncounterManager import EncounterEngine
from EventMngr import *
from Events import *
from gui import MessageBox, StatsDisplay
from pygame.constants import *
import pygame
from tilesprite import *

screensize = [800,600 ]
fs = 0

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

class TileEngine:
	test= "$"
	passable = []
	def __init__(self, eventmanager, gamedata):
		self.evtmngr = eventmanager
		self.evtmngr.registerObserver(self)
		
		pygame.init()
		screen = pygame.display.set_mode(screensize, DOUBLEBUF | fs)
   		self._tiles = {}
		self._nothing = pygame.image.load("img/nothing.png").convert()
		self._missing = pygame.image.load("img/missing.png").convert()
		self._screen = screen
		self._sprites = []
		self.sprites = [] # This is a temp var, the raw data is loaded here then moved to _sprites
		self._player = None 
		self._staff = None
		self._npc = []
		self._location = gamedata.get('playerlocation')
		self._map = []
		self._mapinfo = {}
		self._font = pygame.font.Font(None, 20);
		self._offset = [0, 0]
		self._display = True
		self._displaymsg = False
		self._msgbox = None
		self._messages = ()
		screenSize = self._screen.get_size()
		self._screenCenter = [ (screenSize[0]/2), (screenSize[1]/2) ]
		self.loadMap(gamedata.get('maplist')[gamedata.get('startingmap')])
		
		# this is temp I think, probably should be in the game object
		self.addPlayer(gamedata.get('playerimage'), gamedata.get('playerlocation'), gamedata.get('playerstats'))
		
	#
	# Used to update the screen	
	def notify(self, evt):
		if isinstance( evt, TickEvent ):
			self.paint()
		if isinstance(evt, CharMoveRequestEvent):
			direction = None
			if(evt.direction == "up"):
				direction = up
			elif(evt.direction == "down"):
				direction = down
			elif(evt.direction == "left"):
				direction = left
			elif(evt.direction == "right"):
				direction = right
			if(direction != None):
				self.move(direction)
		if isinstance(evt, Encounter):
			print "There's an encounter!"
			self.encounterHandler(evt)

	def encounterHandler(self, evt):
		"""An encounter might be happening, need to find out what
		kind it is, and how it should be handled"""
		print "In encounterHandler()"
		#Determine if we are even having this fight...

		#Ok, we are having the fight! (this is following the tests/combat_tester.py file)
		enceng = EncounterEngine(evt)
		# Get the orders for the good guys
		enceng.startEncounter([self.ego])
		while enceng.stillFighting():
			print "Next round!"
			#Display the stats
			#Get the orders for the good guys
			#Get the orders for the bad guys
			enceng.playRound()
		print "Encounter over"
	
	def addPlayer(self, image, startpos, stats):
		self.ego = Character( self, "ego", startpos, image)
		self.ego.image = self.getImage(image)

	def loadMap(self, mapname):
		values = {}
		execfile(mapname, globals(), values)
		self.__dict__.update(values)
		images = values['images']
		for tile in images:
			try:
				img = pygame.image.load(images.get(tile))
			except:
				img = self._missing
			img.set_colorkey((0,0,0,0), RLEACCEL)
			self._tiles[tile] = img.convert()
		self.passable = []
		for p in self._mapinfo['passable']:
			self.passable.append(p) #Set the passable tile
		self._tilewidth = self._tiles['.'].get_size()[0]
		self._tileheight = self._tiles['.'].get_size()[1]
		self.loadSprites(self.sprites)

	#
	# While this block works, it does duplicate work. It would be nice
	# if images were only loaded once....
	def loadSprites(self, spritelist):
		print "loading sprites"
		if(len(self._sprites) > 0):
			tmp = self._sprites[0]
			self._sprites = []
			self._sprites.append(tmp)
		for sprite in spritelist:
			img = self.images.get(sprite[2])
			image = self.getImage(img)
			s = TileSprite(img, self, sprite[0][0], sprite[0][1], sprite[1])
			if len(sprite) == 4:
				s.setDoorData(sprite[3])
			self.addSprite(s, sprite[1]) 

	def getImage(self, imagename):
		'''This loads up the image (via the magic of pygame'''
		if imagename:
			image = pygame.image.load(imagename)
			image.set_colorkey( (0, 0, 0, 0), RLEACCEL)
		return image.convert()
		
	def addSprite(self, sprite, npc = 0):
		self._sprites.append(sprite)
		
	def centerOn(self, sprite):
		'''convert sprite co-ords to screen co-ords'''
		screenSize = self._screen.get_size()
		spriteXY = sprite.position
		self._offset[0] = (screenSize[0]/2 - self._location[0] - (spriteXY[0] * self._tilewidth))
		self._offset[1] = (screenSize[1]/2 - self._location[1] - (spriteXY[1] * self._tileheight))

	#
	# This method checks to see if we can move and gets any messages
	# or events that are necessary.
	def moveOk(self, newx, newy):
		# Also need to check for out of range
		if not self._map[newy][newx] in self.passable:
			return False
		else:
			#New area is not passible, need to find out what to do
			result = None
			for sprite in self._sprites: 
				if sprite.getXY() == (newx, newy):
					#This means we are bumping into something
					print 'sprite...',sprite
					sprite.handle()
					return result
			return result

	def moveToNewRoom(self, door):
		self.loadMap(door[1][0])
		loc = door[1][1]
		print "Old location is: ", self.ego.position, " ", loc
		self.ego.position = [self._mapinfo['door'][loc][0][0], self._mapinfo['door'][loc][0][1]]
		print "New Location is: ", self.ego.position
		
	def paintSprite(self, sprite):
		x, y = sprite.position
		x *= self._tilewidth
		y *= self._tileheight
		left = self._location[0] + self._offset[0]
		top = self._location[1] + self._offset[1]
		self._screen.blit(sprite.image, (x+left, y+ top))
	
	def paint(self):
		"""The main paint method for the big screen."""
		screen = self._screen
		self._screen.fill( (0, 0, 0) )
		self.centerOn(self.ego)
	
		x = self._location[0] + self._offset[0]
		y = self._location[1] + self._offset[1]
		width = self._tilewidth
		height = self._tileheight
		for row in self._map:
			for col in row:
				try:
					tile = self._tiles[col]
					screen.blit(tile, (x, y))
				except KeyError:
					screen.blit(self._missing, (x, y))
				x += width
			x = self._location[0] + self._offset[0]
			y += height
		for sprite in self._sprites:
			x, y = sprite.getXY()
			left = self._location[0] + self._offset[0]
			top = self._location[1] + self._offset[1]
			x *= self._tilewidth
			y *= self._tileheight
			sprite.paint(screen, (x + left, y + top))
		if(self._display):
			pass #print 'Need a better paintMessages() method'
		else:
			self.paintStats(screen,self.ego)
		self.paintSprite(self.ego)
		if(self._displaymsg):
			self.messageBox(self._msgstr, screen)
			#screen.blit(self._msgbox, self._screenCenter)
			self._displaymsg = False
		pygame.display.flip()

	#
	# Sets the message to be displayed during the paint call
	def setMessage(self, messagestr):
		self._displaymsg = True
		self._msgstr = messagestr
		
	def removeSprite(self, sprite):
		self._sprites.remove(sprite)
		try:
			self._npc.remove(sprite)
		except ValueError:
			pass
		
	def move(self, direction):
		'''Updates the sprite on the screen'''
		dx,dy = direction
		newX = self.ego.position[0] + dx
		newY = self.ego.position[1] + dy
		result = self.moveOk(newX, newY)
		print "Old: ", self.ego.position, " New:",(newX,newY), " Direction: ", direction
		if result == None:
			self.ego.updatePosition(newX, newY) 
		return result
 			
	def messageBox(self, message, screen):
		msg_rect = pygame.Rect(( 0, 0, 500, 300))
		white = (225, 255, 255)
		backgrnd = (48, 48, 48)
		msgbox = MessageBox(screen)
		msgbox.render_textrect(message, self._font, msg_rect, white, backgrnd,  2)

	def flipMessagePane(self):
		self._display = not self._display
		
	

