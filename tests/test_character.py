#
# Series of tests to exercise Characters

from nose.tools import raises
from Character import Character as C
from Entity import Item
from EventMngr import *
from Item import *

@raises(Exception)
def testBadInit():
    c = C()

def getChar():
    return  C(None, "test", (0,0), None, None, None)

def getItem():
    mngr = EventManager()
    i = Item(mngr)
    return i

def testInit():
    c = getChar()
    assert c

def testpickup():
    c = getChar()
    assert len(c.inventory) == 0
    c.pickup(getItem())
    assert len(c.inventory) == 1

def testdrop():
    c = getChar()
    assert len(c.inventory) == 0
    i = getItem()
    c.pickup(i)
    c.drop(i)
    assert len(c.inventory) == 0

def testreload():
    c = getChar()
    mngr = EventManager()
    i = Gun(mngr)
    c.pickup(i)
    c.equipWeapon(i)
    ammo = Ammo(mngr)
    ammo.amt = 10
    c.pickup(ammo)
    assert len(c.inventory) == 2
    assert c.inventory[0].amt == 1
    c.reload()
    assert len(c.inventory) == 1
    assert c.inventory[0].amt == 11 #Weapon ammo
