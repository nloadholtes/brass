#
# ItemMaker.py
# 
# A tool to create Items for the Brass engine.
#
# July 3, 2006
#

import  wx
import sys,os

FILENAME = '../Items.py'

def writeItemsOut(values):
    print('Not implemented: writeItemsOut()')

class ItemMaker(wx.App):
    def __init__(self):
        self.name = "blah"
        wx.App.__init__(self, redirect=False)
        f = MyFrame(None, 0, "Testing", (0,0))

    def startGUI():
        print('Starting ItemMaker.py')
        values = {}
        execfile(FILENAME, globals(), values)
        for item in values:
            print(item)
        wx.App.__init__(redirect=False)
        f = MyFrame(None, 0, "Testing", (0,0))
        # Start building the GUI
        
    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())

        self.SetAssertMode(wx.PYAPP_ASSERT_DIALOG)

        frame = wx.Frame(None, -1, "Item Maker: " + self.name, pos=(50,50), size=(200,100),
                        style=wx.DEFAULT_FRAME_STYLE)
        frame.CreateStatusBar()

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "E&xit\tAlt-X", "Exit demo")
        self.Bind(wx.EVT_MENU, self.OnButton, item)
        menuBar.Append(menu, "&File")

        ns = {}
        ns['wx'] = wx
        ns['app'] = self
        ns['frame'] = frame
        
        frame.SetMenuBar(menuBar)
        frame.Show(True)
        frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame)
        self.SetTopWindow(frame)
        self.frame = frame
        #wx.Log_SetActiveTarget(wx.LogStderr())
        #wx.Log_SetTraceMask(wx.TraceMessages)

        return True


    def OnButton(self, evt):
        self.frame.Close(True)


    def OnCloseFrame(self, evt):
        if hasattr(self, "window") and hasattr(self.window, "ShutdownDemo"):
            self.window.ShutdownDemo()
        self.frame.Destroy()
        self.ExitMainLoop()
        evt.Skip()
        

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(
            self, parent, ID, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE
            ):

        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        panel = wx.Panel(self, -1)

        button = wx.Button(panel, 1003, "Close Me")
        button.SetPosition((15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)


    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

#---------------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a Frame", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        win = MyFrame(self, -1, "This is a wx.Frame", size=(350, 200),
                  style = wx.DEFAULT_FRAME_STYLE)
        win.Show(True)

        


#---------------------------------------------------------------------------


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


#---------------------------------------------------------------------------


overview = """\
A Frame is a window whose size and position can (usually) be changed by 
the user. It usually has thick borders and a title bar, and can optionally 
contain a menu bar, toolbar and status bar. A frame can contain any window 
that is not a Frame or Dialog. It is one of the most fundamental of the 
wxWindows components. 

A Frame that has a status bar and toolbar created via the 
<code>CreateStatusBar</code> / <code>CreateToolBar</code> functions manages 
these windows, and adjusts the value returned by <code>GetClientSize</code>
to reflect the remaining size available to application windows.

By itself, a Frame is not too useful, but with the addition of Panels and
other child objects, it encompasses the framework around which most user
interfaces are constructed.

If you plan on using Sizers and auto-layout features, be aware that the Frame
class lacks the ability to handle these features unless it contains a Panel.
The Panel has all the necessary functionality to both control the size of
child components, and also communicate that information in a useful way to
the Frame itself.
"""
if __name__ == "__main__":
    im = ItemMaker()
    im.MainLoop()
