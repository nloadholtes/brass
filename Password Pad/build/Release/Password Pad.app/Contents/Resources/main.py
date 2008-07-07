#
#  main.py
#  Password Pad
#
#  Created by Nick Loadholtes on 7/7/08.
#  Copyright Iron Bound Software 2008. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import Password_PadAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
