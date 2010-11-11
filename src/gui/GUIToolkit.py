'''
Created on Aug 1, 2009

@author: njl
'''
from pyglet import window
from pyglet import image
from pyglet import app

class GUIToolkit(window.Window):
        '''
        This is a wrapper for platform specific libraries like pygame.
        '''
        k_left = window.key.LSHIFT
        k_right = window.key.RIGHT
        k_up = window.key.UP
        k_down = window.key.DOWN
        k_space = window.key.SPACE
#        k_quit = QUIT
#        k_keydown = KEYDOWN
        k_escape = window.key.ESCAPE
        win = None
        te = None
        
        def __init__(self, tileengine):
                self.te = tileengine
        
        def on_draw(self):
            print("on_draw()")
            self.te.paint()
            
        def on_key_press(self, symbol, modifiers):
            print "on_key_press()",symbol
            if symbol == window.key.ESCAPE:
                app.exit()
            self.te.paint()
            
        def on_exit(self):
            print "on_exit() called"
            self.quit()
            
        def init(self, screensize):
                '''
                This is a library specific initializtion routine 
                '''
                self.win = window.Window(screensize[0], screensize[1], visible=True)
                self.win.clear()
                
        def setDisplayMode(self, screensize, fullscreen):
                ''' Set the mode (resolution, etc.) for the screen '''
                return self.win 
            
        def getImage(self, imageFilename):
                '''Gets an image '''
                return image.load(imageFilename)
        
        def quit(self):
                '''Shutdown the platform specific stuff'''
                print("GUIToolkit.quit() called")
                app.exit()
                
        def getEvent(self):
                return None #pygame.event.get()
        
        def flipScreen(self):
                '''Double buffering is nice...'''
                return None #self.win.flip()
            
def startGame():
    app.run()