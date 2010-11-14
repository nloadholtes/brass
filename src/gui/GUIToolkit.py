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
        k_left = window.key.LEFT
        k_right = window.key.RIGHT
        k_up = window.key.UP
        k_down = window.key.DOWN
        k_space = window.key.SPACE
#        k_quit = QUIT
#        k_keydown = KEYDOWN
        k_escape = window.key.ESCAPE
        te = None
        
        def __init__(self, tileengine):
            super(GUIToolkit, self).__init__()
            self.te = tileengine
            self.clear()
        
        def on_draw(self):
            print("on_draw()")
            self.te.paint()
            
        def on_key_press(self, symbol, modifiers):
            print "on_key_press()",symbol
            if symbol == window.key.ESCAPE:
                self.on_exit()
            else:
                self.te.paint()
            
        def on_exit(self):
            print "on_exit() called"
            self.quit()
            
        def setDisplayMode(self, screensize, fullscreen):
                ''' Set the mode (resolution, etc.) for the screen '''
                return self
            
        def getImage(self, imageFilename):
                '''Gets an image '''
                img = image.load(imageFilename)
                return img
        
        def quit(self):
                '''Shutdown the platform specific stuff'''
                print("GUIToolkit.quit() called")
                app.exit()
                
        def getEvent(self):
                return None 
                    
        def flipScreen(self):
                '''Double buffering is nice...'''
                return self.flip() 
            
def startGame():
    app.run()