'''
Created on Aug 1, 2009

@author: njl
'''
import pygame
from pygame.constants import *
from pygame.locals import *

class GUIToolkit:
	'''
	This is a wrapper for platform specific libraries like pygame.
	'''
	k_left = K_LEFT
	k_right = K_RIGHT
	k_up = K_UP
	k_down = K_DOWN
	k_space = K_SPACE
	k_quit = QUIT
	k_keydown = KEYDOWN
	k_escape = K_ESCAPE
	
	def __init__(self):
		pass
		
	def init(self):
		'''
		This is a library specific initializtion routine 
		'''
		pygame.init()
		
	def setDisplayMode(self, screensize, fullscreen):
		''' Set the mode (resolution, etc.) for the screen '''
		return pygame.display.set_mode(screensize, DOUBLEBUF | fullscreen)
	
	def getImage(self, imageFilename):
		'''Gets an image '''
		image = pygame.image.load(imageFilename)
		image.set_colorkey( (0, 0, 0, 0), RLEACCEL)
		return image.convert()
	
	def quit(self):
		'''Shutdown the platform specific stuff'''
		pygame.quit()
		
	def getEvent(self):
		return pygame.event.get()
	
	def flipScreen(self):
		'''Double buffering is nice...'''
		return pygame.display.flip()