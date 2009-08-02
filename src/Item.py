#
# The list of all items in the world
#
# May 27, 2006
#

from Entity import Item
from tilesprite import TileSprite


#
# The values for these items should be change as
# they are instantiated (i.e. if it a big gun adjust the
# damage up, etc.)
#

class Gun(Item):
    name = 'Gun'
    adj = 'shoots'
    stat = 'health'
    value = -10
    amt = 1
    range = 100 
    fmtline = "@TARGET @ADJ @VALUE points"
    adjs = ('gets blasted for', 'sucks it down for', 'eats hot lead and looses', 'gets shot up for', 'gets nailed for', 'isn\'t fast enough and gets hit for' ,
            'feels the kiss of hot lead and looses')
    
    def use(self, target):
        if target.__class__ == Ammo:
            #print "reload!"
            #print target.__class__
            #val = getattr(target, self.stat, 0) + self.value
            s = self.fmtline
            s = s.replace('@NAME', self.name)
            s = s.replace('@TARGET', target.name)
            s = s.replace('@ADJ', 'reloads with')
            s = s.replace('@STAT', self.stat)
            s = s.replace('@VALUE', str(abs(target.amt)))
            print s
            #setattr(target, target.amt, val)
            #target.amt = val
            #print '\tAmmo has ', target.amt, ' amt'
            #print '\tgun has ', self.amt, ' amt'  
            self.amt += target.amt
            target.amt = 0
        else:
            Item.use(self, target)

class Ammo(Item):
    name = 'Ammo'
    stat = 'ammo'
    adj = 'reloads'
    value = 1
    amt = 10

    def use(self, target):
        val = getattr(target, self.stat, 0) + self.value
        s = self.fmtline
        s = s.replace('@NAME', self.name)
        s = s.replace('@TARGET', target.name)
        s = s.replace('@ADJ', self.adj)
        s = s.replace('@STAT', self.stat)
        s = s.replace('@VALUE', str(abs(self.amt)))
        print s, self.amt
        #setattr(target, target.amt, val)
        target.amt = val
        self.amt -= 1
            
class Bomb(Item):
    name = 'Bomb'
    adj = 'blasts'
    empty = 'The %s has already been detonated!'
    value = -100
    amt = 1

class HealthPotion(Item):
    name = 'Health Potion'
    adj = 'heals'
    value = 10
    amt = 1

class Poison(Item):
    name = 'Belladonna'
    adj = 'poisons'
    value = -1
    amt = 1

class Food(Item):
    name = 'Food'
    fmtline = '@TARGET eats the @NAME '
    stat = 'health'
    empty = "The %s has already been eaten!"
    value = 1
    amt = 1
    
class Door(TileSprite):
    name = 'Door'    
    value = 100
    amt = 1
    
    def __init__(self, manager, name, position, imageFileName, parent, gtk):
        TileSprite.__init__(self, manager, imageFileName, parent, position[0], position[1], gtk)
        
    def handle(self):
        d = self._parent._mapinfo['door'][self.getDoorData()]
        from tilesprite import *
        if d[2] == ok_to_move:
            return self._parent.moveToNewRoom(d)
        elif d[2] == ask_to_move:
            self.printm("We gotta ask about this move")

    def setDoorData(self, dat):
        self._doordata = dat
        
    def getDoorData(self):
        return self._doordata