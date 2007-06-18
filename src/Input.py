#
# This class handles the input from the user
#

from Events import *
import pygame
from pygame.locals import *

left = K_LEFT
right = K_RIGHT
up = K_UP
down = K_DOWN
space = K_SPACE

class Input:
    def __init__(self, manager):
        self.manager = manager
        self.manager.registerObserver(self)

    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                ev = None
                if event.type == QUIT:
                    ev = QuitEvent()
                elif event.type == KEYDOWN: 
                    if event.key == K_ESCAPE:
                        ev = QuitEvent()
                    elif event.key == up:
                        ev = CharMoveRequestEvent("up")
                    elif event.key == left:
                        ev = CharMoveRequestEvent("left")
                    elif event.key == down:
                        ev = CharMoveRequestEvent("down")
                    elif event.key == right:
                        ev = CharMoveRequestEvent("right")
                    #Need other cases here to catch user input for battles, etc
                        
                if ev:
                    self.manager.notify(ev)
