#
# This file is ment to test out encounter (combat) details
#
# June 25, 2006
#

from Item import *
from Items import *
from Character import *
from EventMngr import *
from EncounterManager import *

bob = None
joe = None
tom = None

def createPlayers():
    global bob, joe, tom
    mngr = EventManager()
    bob =  Character(mngr, 'Bob', (0,0), None, None, None)
    joe =  Character(mngr, 'Joe', (0,0), None, None, None)
    gun = Gun(mngr)
    ammo = Ammo(mngr)
    gun.updateData(ak47)
    joe.pickup(gun)
    joe.pickup(ammo)
    joe.equipWeapon(gun)
    joe.reload()
    tom = Character(mngr, 'Tom', (0,0), None, None, None)
    tom.initative = 12

def encounter():
    """This is an exploded version of the encounter loop to testing/tuning"""
    print 'Staring the Encounter'
    from EncounterManager import createBadGuys
    global bob, joe, tom
    goodguys = [joe, tom]
    badguys = createBadGuys(2, 2, 0)
    ee = EncounterEngine()
    ee.goodguys = goodguys
    ee.badguys = badguys.characters
    ee.startCombatEncounter()
    while ee.stillFighting():
        print 'Next round!'
        displayStats(ee.goodguys, ee.badguys)
        getOrders(ee.goodguys, ee.badguys)
        ee.getBadguyOrders(1)
        ee.playRound()
    print '\t\t***************Battle over!********************'

def displayStats(goodguys, badguys):
    print '\t------Good guys:------'
    for guy in goodguys:
        print '\t',guy.name, guy.health

    print '\t----Bad guys ------'
    for dude in badguys:
        if dude.health > 0:
            print '\t',dude.name, dude.health
    print '\t------------------------'

def getOrders(party, badguys):
    for x in party:
        order = None
        while not order:
            print 'Orders for: ', x.name
            print 'A)ttack'
            print 'E)vade'
            print 'R)eload'
            print 'T)alk'
            print 'I)neventory'
            print 'Q)uit'
            action = raw_input("Action: ").lower()
            if action == 'a':
                print 'Who do you want to attack?'
                y = 1
                for dude in badguys:
                    print '\t',y,')', dude.name
                    y += 1
                target = raw_input()
                #Shove this into the orders for X
                order = ActionOrder(x, 'attack', badguys[int(target)-1])
                x.orders.append(order)
            elif action == 'b':
                print 'Passing'
            elif action == 'c':
                print 'Reload'
            elif action == 'q':
                print 'Goodbye!'
                exit(0)
            elif action == 'i':
                stuff = x.getInventory()
                print "  Inventory for %s" %  x.name
                for thing in stuff:
                    print "\t%s" % thing.name


if __name__ == '__main__':
    createPlayers()
    encounter()


