#
#  Password_PadAppDelegate.py
#  Password Pad
#
#  Created by Nick Loadholtes on 7/7/08.
#  Copyright Iron Bound Software 2008. All rights reserved.
#

from Foundation import *
from AppKit import *

class Password_PadAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
