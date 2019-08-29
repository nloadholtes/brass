#
# This test the Item class to make sure everything is ok
#
# May 27, 2006
#

from nose.tools import *
from Item import *
from Items import ak47, pistol
from Character import *
from EventMngr import *

def testsinglegunmain():
    print('------------------ Testing single gun ---------------------')
    mngr = EventManager()
    bob = Character(mngr, 'Bob', (0,0), None, None, None)
    gun = Gun(mngr)

    #Gun shoots man
    gun.use(bob)
    gun.use(bob)

    #Gun out of ammo. Reload
    ammo = Ammo(mngr)
    gun.use(ammo)
    ammo.use(gun)

    #Gun shoots again.
    assert gun.amt == 1
    gun.use(bob)
    assert gun.amt == 0

def testtwoguysshooting():
    print('------------------ Testing two guys shooting at each other ---------------------')
    mngr = EventManager()
    #Meet Joe and Bob
    bob = Character(mngr, 'Bob', (0,0), None, None, None)
    joe = Character(mngr, 'Joe', (0,0), None, None, None)
    #joe.adjustSkill('attack', 100) #Joe is now quite dangerous

    #Lets give them both guns
    bobgun = Gun(mngr)
    joegun = Gun(mngr)
    bobgun.name = 'Shotgun'

   #bobgun.updateData(pistol)
    joegun.updateData(ak47)
    bob.pickup(bobgun)
    joe.pickup(joegun)
    bob.equipWeapon(bobgun)
    joe.equipWeapon(joegun)

    #Let the shooting begin!
    joe.attack(bob)
    bob.attack(joe)
    joe.reload()
    joeammo = Ammo(mngr)
    joe.pickup(joeammo)
    joe.reload()
    # joe.reloadWeapon(joeammo)
    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)

@nottest
def testlongshot():
    print('------------------ Testing ranged weapons ---------------------')

