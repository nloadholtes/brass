#
# This test the Item class to make sure everything is ok
#
# May 27, 2006
#

from Item import *
from Items import ak47, pistol
from Character import *
from EventMngr import *

def singlegunmain():
    print '------------------ Testing single gun ---------------------'
    mngr = EventManager()
    bob = Character(mngr, 'Bob')
    gun = Gun()

    #Gun shoots man
    gun.use(bob)
    gun.use(bob)

    #Gun out of ammo. Reload
    ammo = Ammo()
    gun.use(ammo)
    ammo.use(gun)

    #Gun shoots again.
    gun.use(bob)

def twoguysshooting():
    print '------------------ Testing two guys shooting at each other ---------------------'
    mngr = EventManager()
    #Meet Joe and Bob
    bob = Character(mngr, 'Bob')
    joe = Character(mngr, 'Joe')
    #joe.adjustSkill('attack', 100) #Joe is now quite dangerous

    #Lets give them both guns
    bobgun = Gun()
    joegun = Gun()
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
    joeammo = Ammo()
    joe.pickup(joeammo)
    joe.reload()
    joe.reloadWeapon(joeammo)
    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)
#    joe.attack(bob)

def longshot():
    print '------------------ Testing ranged weapons ---------------------'

if __name__ == "__main__":
    singlegunmain()
    twoguysshooting()
    longshot()
