#!/usr/bin/env python
# Game class. Holds all of the global vars
# and starts the game.

from CPUSpinnerController import *
from EventMngr import *
from Input import *
from tileengine import *
import gui.GUIToolkit
from gui.GUIToolkit import startGame
import pyglet
import sys



if __name__ == "__main__":
    #
    #Read in the game file how can you tell?
    values = {}
    print sys.argv
    if(len(sys.argv) > 1):
        print "Loading game file"
        execfile(sys.argv[1], globals(), values)
    else :
        raise Exception, "Can't run with out a game file"

    gamedata = values.get('gamedata')
    evtmngr = EventManager()

    #keybd = Input(evtmngr, gtk)
    #spinner = CPUSpinnerController(evtmngr)
    te = TileEngine(evtmngr, gamedata)
    gtk = GUIToolkit(te)
    te.initTE(gtk)
    #game = Game( evManager )

    #
    #Run the game
    #spinner.run()
    startGame()
