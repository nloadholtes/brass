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
    bob =  Character(mngr, 'Bob', (0,0), None)
    joe =  Character(mngr, 'Joe', (0,0), None)
    gun = Gun(mngr)
    ammo = Ammo(mngr)
    gun.updateData(ak47)
    joe.pickup(gun)
    joe.pickup(ammo)
    joe.equipWeapon(gun)
    joe.reload()
    tom = Character(mngr, 'Tom', (0,0), None)
    tom.initative = 12
    
def encounter():
    print 'Staring the Encounter'
    from EncounterManager import createBadGuys
    global bob, joe, tom
    goodguys = [joe, tom]
    badguys = createBadGuys(2, 2, 0)
    ee = EncounterEngine(badguys)
    ee.startEncounter(goodguys)
    while ee.stillFighting():
        print 'Next round!'
        displayStats(goodguys, badguys)
        getOrders(goodguys, badguys)
        ee.getBadguyOrders(badguys, goodguys, 1)
        ee.playRound()
    print '\t\t***************Battle over!********************'
   
def displayStats(goodguys, badguys):
    print '\t------Good guys:------'
    for guy in goodguys:
        print '\t',guy.name, guy.health
        
    print '\t----Bad guys ------'
    print badguys
    for dude in badguys.characters:
        print '\t',dude.name, dude.health
    print '\t------------------------'
   
def getOrders(party, badguys):
    for x in party:
        print 'Orders for: ', x.name
        print 'A)ttack'
        print 'E)vade'
        print 'R)eload'
        print 'T)alk'
        print 'Q)uit'
        action = raw_input()
        print action
        if action == 'a':
            print 'Who do you want to attack?'
            y = 1
            for dude in badguys.characters:
                print '\t',y,')', dude.name
                y += 1
            target = raw_input()
            #Shove this into the orders for X
            order = ActionOrder(x, 'attack', badguys.characters[int(target)-1])
            x.orders.append(order)
        elif action == 'b':
            print 'Passing'
        elif action == 'c':
            print 'Reload'
        elif action == 'q':
            print 'Goodbye!'
            exit()
    

if __name__ == '__main__':
    print '1 for combat, 2 for talking'
    createPlayers()
    encounter()
    

