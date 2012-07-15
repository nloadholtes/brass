#
# Series of tests to exercise Characters

from nose.tools import raises
from Character import Character as C
from Entity import Item
from EventMngr import *

@raises(Exception)
def testBadInit():
    c = C()

def testInit():
    c = C(None, "test", (0,0), None, None, None)
    assert c

def testpickup():
    c = C(None, "test", (0,0), None, None, None)
    assert len(c.inventory) == 0
    mngr = EventManager()
    i = Item(mngr)
    c.pickup(i)
    assert len(c.inventory) == 1
