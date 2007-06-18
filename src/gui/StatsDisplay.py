#
# StatsDisplay.py
# Nick Loadholtes
# May 25, 2007
#

import pygame

class StatsDisplay:
    size = (100, 200)
    location = (0, 0)
    backgroundcolor =  (48, 48, 48)
    white = (255, 255, 255)
    textcolor = white
    
    def __init__(self, screen, players):
        '''This class displays the stats for the player'''
        self.screen = screen

        #Getting the surface
        surface = pygame.Surface(self.size)
        surface.fill(self.backgroundcolor)

        #Loop through the players, write the stats to the surface
        accumulatedheight = 0
        for player in players:
            line = (player.name + "\t" + player.health)
            tmpsurface = font.render(line, 1, self.textcolor)
            surface.blit(tmpsurface, (0, accumulatedheight))

            accumulatedheight += font.size(line)[1]


        #draw surface to the screen
        screen.blit(surface, self.location)
