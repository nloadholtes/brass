#
# This class defines most everything needed to describe a player or
# and NPC
#

from Entity import *
from Item import *
from tilesprite import *

import copy

MAX_ITEMS = 50

class Character(object, TileSprite):
    name = 'person'
    position = []
    orders = []
#    sprite = None

    def __init__(self, manager, name, position, imageFileName, parent, gtk, encounter=None):
        TileSprite.__init__(self, manager, imageFileName, parent, position[0], position[1], gtk)
        self.name = name
        self.position = position
        self.equipped = {'weapon' : None, 'armor' :None}
        self.health = 50
        self.inventory = []
        self.skills = { 'attack' : 0}
        self.value = -2
        self.initative = 10
        self.level = 1
        self.encoutner = encounter
        self.agility = 5
        self.orig_agility = self.agility

    def __setattr__(self, key, val):
        if key == 'health':
            if val < 1:
                print "%s is dead!" % self.name
#            else:
#                print "%s has %d %s remaining" % (self.name, val, key)
        object.__setattr__(self, key, val)

    def executeOrder(self, actionorder):
        """This is our replacement for eval() in the play round loop."""
        print " (Order seen: %s is %s->%s)" % (self.name, actionorder.what, actionorder.target.name)
        e = {'attack' : lambda x: self.attack(actionorder.target),
             'EVADE' : lambda x:self.evade(),
             # 'USE' : print("We'll use something someday.")
        }
        e.get(actionorder.what)(1)

    def resetAfterCombat(self):
        self.orders = []
        self.agility = self.orig_agility

    #
    # Map and movement related methods
    #

    def evade(self):
        """Evading basically temporarily sets your stats a little higher
to reflect the idea you are trying to avoid being hit"""
        self.orig_agility = self.agility
        self.agility += 10

    def place(self, location):
        pass

    #
    # Inventory related methods
    #
    def drop(self, item):
        pass

    def pickup(self, item):
        if len(self.inventory) < MAX_ITEMS:
            print self.name, " picks up " , item
            self.inventory.append(item)

    def equipWeapon(self, weapon):
        self.equipped['weapon'] = weapon

    def equipArmor(self, armor):
        self.equipped['armor'] = armor

    def reloadWeapon(self, ammo):
        '''Use this method if you want to reload a weapon'''
        weapon = self.equipped['weapon']
        if weapon != None:
            weapon.use(ammo)
            self.inventory.remove(ammo)

    #
    # Attack related methods
    #
    def attack(self, target):
        weapon = self.equipped['weapon']
        if weapon == None:
            print '\t****No weapon equipped!!! Punching and kicking our way out of this one!'
            self.equipWeapon(self)
            weapon = self.equipped['weapon']
        if weapon == self:
            weapon.modifier = self.skills['attack']
        else:
            if weapon.amt > 0:
                weapon.modifier = self.skills['attack']
        #Check to make sure target is alive first
        if(target.health > 0):
            weapon.use(target)
        else:
            print "\t", self.name," holds off because ", target.name, "is dead"

#        else:
#            print self.name,'-Needs to hit with the gun'
#            self.equipWeapon(weapon)
#            self.use(target)
            #Need to determine if attack is sucessful

            #Need to add in other modifiers to determine damage

    def use(self, target):
        from random import randint
        s = "@NAME @ADJ @TARGET for @VALUE"
        stat = 'health'
        adjs = ('pummels', 'beats the crap out of', 'slugs', 'gives the ol\' one-two to', 'punches')
        val = getattr(target, stat, 0) + self.value - self.skills['attack']
        s = s.replace('@NAME', self.name)
        s = s.replace('@TARGET', target.name)
        s = s.replace('@ADJ', adjs[randint(0, len(adjs) -1)])
        s = s.replace('@STAT', stat)
        s = s.replace('@VALUE', str(abs(self.value)))
        print s
        setattr(target, stat, val)


    def reload(self):
        '''Use this method to reload the currently equipped weapon'''
        # Need to look through the inventory to make sure they have ammo
        ammofound = False
        weaponname = self.equipped['weapon'].name
        for item in self.inventory:
            if item.__class__ == Ammo:
                print self.name, ' reloads the ', weaponname
                ammofound = True
                self.reloadWeapon(item)
        if not ammofound:
            print self.name, 'has no ammo to reload the', weaponname, '!'

    #
    # Skill related methods
    #
    def adjustSkill(self, name, value):
        self.skills[name] = value

    def getInit(self):
        return self.initative

    def notify(self, evt):
        '''The result of an encounter'''
        self.printm(self.name + ": What do you want?")

    def updatePosition(self, x, y):
        '''This method will update the Character\'s position (because we can\'t assign the tuple individually)'''
        self.position = [x,y]

    def getInventory(self):
        output = copy.deepcopy(self.inventory)
        return output


    #
    # Other methods
    #
    def handle(self):
    	'''If there is an encounter associated with this character, then notify
    	the manager and pass them the encounter event...'''
        self.printm("Default Character handler caught this...")
        if None != self.encoutner:
        	#Fire up the encounter handler!!!
        	return self.manager.notify(EncounterEvent(self.encoutner))
