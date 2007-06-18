#
# This class defines most everything needed to describe a player or
# and NPC
#

from Entity import *
from Item import *

MAX_ITEMS = 50
    
class Character(object):
    name = 'person'
    position = []
    orders = []

    #
    # Is it even possible that this constructor is
    #somehow calling the Entity constructor which
    #happens to expect a manager as its first argument?
    #The Entity init is already commented out, yet
    #when this class runs I see the player being moved
    #twice! Somehow the TileEngine's notify is being
    #called twice...
    #
    # Need to try commenting out the notify in this class
    #then test, followed by removing the Entity in the class
    #declaration.
    #
    def __init__(self, manager, name, position, imageFileName):
        #Entity.__init__(self, manager)
        #TileSprite.__init__(self, imageFileName, manager, position[0], position[1], 0)
        self.name = name
        self.position = position
        self.equipped = {'weapon' : None, 'armor' :None}
        self.health = 50
        self.inventory = []
        self.skills = { 'attack' : 0}
        self.value = -2
        self.initative = 10
        self.level = 1
    
    def __setattr__(self, key, val):
        if key == 'health':
            if val < 1:
                print "%s is dead!" % self.name
#            else:
#                print "%s has %d %s remaining" % (self.name, val, key)
        elif key == 'hunger':
            if val > 100:
                print "%s has starved to death!" % self.name
            else:
                print "%s is %d%% hungry" % (self.name, val)
        object.__setattr__(self, key, val)
    

    #
    # Map and movement related methods
    #
  
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

    #
    # Attack related methods
    #
    def attack(self, target):
        weapon = self.equipped['weapon']
        if weapon == None:
            print '****No weapon equipped!!! Punching and kicking our way out of this one!'
            self.equipWeapon(self)
            weapon = self.equipped['weapon']
        if weapon == self:
            weapon.modifier = self.skills['attack']
        else:
            if weapon.amt > 0:
                weapon.modifier = self.skills['attack']
        weapon.use(target)
                
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
    
#    def notify(self, evt):
#        self.manager.notify(evt)
#    
    def updatePosition(self, x, y):
        '''This method will update the Character's position (because we can't assign the tuple individually)'''
        self.position = [x,y]
        
