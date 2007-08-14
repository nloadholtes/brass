#!/usr/bin/env python
#
# MessageBox.py
# May 17, 2007
# Nick Loadholtes
#
# This classwill display messages on the screen
#

import pygame
from Events import *

class BottomMessageBox:
    def __init__(self, screen, manager):
        '''The magical init fo rthe MessageBox
        
         justification - 0 (default) left-justified
            1 horizontally centered
            2 right-justified  
        '''
        self._screen = screen
        self.manager = manager
        self.manager.registerObserver(self)
        screenSize = self._screen.get_size()
        self._screenCenter = [ (screenSize[0]/2), (screenSize[1]/2) ]
        white = (225, 255, 255)
        backgrnd = (48, 48, 48)
        self._backgroundcolor = backgrnd
        self._textcolor = white
        self._rect = pygame.Rect(( 0, 0, 800, 200))
        self._textbuffer = []
        self._font = pygame.font.Font(None, 20)
        self._justification = 0
        self._boxvsize = self._screen.get_size()[1] - 200

    def notify(self, evt):
        '''This method allows anyone to post a message to be displayed on the
        BottomMessageBox.'''
        if isinstance( evt, PrintEvent):
            self.printtext(evt.text)
            self.render()            
        
    def printtext(self, string):
        """This method will take the string and add it to the textbuffer
        that will be drawn to the screen in the render() method. """
        requested_lines = string.splitlines()
    
        # Create a series of lines that will fit on the provided
        # rectangle.
        rect = self._rect    
        for requested_line in requested_lines:
            if self._font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if self._font.size(word)[0] >= rect.width:
                        raise TextRectException, "The word " + word + " is too long to fit in the rect passed."
                    # Start a new line
                    accumulated_line = ""
                    for word in words:
                        test_line = accumulated_line + word + " "
                        # Build the line while the words fit.
                        if self._font.size(test_line)[0] < rect.width:
                            accumulated_line = test_line
                        else:
                            self._textbuffer.append(accumulated_line)
                            accumulated_line = word + " "
                            self._textbuffer.append(accumulated_line)
            else:
                self._textbuffer.append(requested_line)
            self._textbuffer.append("")
    
    def render(self):
        '''This is where the drawing of the textbuffer takes place.'''
        rect = self._rect
        surface = pygame.Surface(rect.size)
        surface.fill(self._backgroundcolor)
        accumulated_height = 0
        for line in reverse(self._textbuffer):
#            if accumulated_height + self._font.size(line)[1] >= rect.height:
#                raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
            if line != "":
                tempsurface = self._font.render(line, 1, self._textcolor)
                if self._justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif self._justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif self._justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException, "Invalid justification argument: " + str(self._justification)
            accumulated_height += self._font.size(line)[1]
        
        self._screen.blit(surface, (0, self._boxvsize))
        
def reverse(data):
    '''A generator from the tutorial to reverse traverse'''
    for index in range(len(data)-1, -1, -1):
        yield data[index]
