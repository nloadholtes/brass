#
# The list of all items in the world
#
# May 27, 2006
#

from Entity import Item
from tilesprite import TileSprite, ok_to_move, ask_to_move
import logging


#
# The values for these items should be change as
# they are instantiated (i.e. if it a big gun adjust the
# damage up, etc.)
#

class Gun(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Gun'
        self.stat = 'health'
        self.value = -10
        self.amt = 1
        self.range = 100
        self.fmtline = "@TARGET @ADJ @VALUE points"
        self.adj = ('gets blasted for', 'sucks it down for', 'eats hot lead and looses', 'gets shot up for', 'gets nailed for', 'isn\'t fast enough and gets hit for' ,
            'feels the kiss of hot lead and looses')

    def use(self, target):
        log = logging.getLogger(__name__ + ".use")
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
            log.debug(s)
            #setattr(target, target.amt, val)
            #target.amt = val
            #print '\tAmmo has ', target.amt, ' amt'
            #print '\tgun has ', self.amt, ' amt'
            self.amt += target.amt
            target.amt = 0
        else:
            Item.use(self, target)

class Ammo(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Ammo'
        self.stat = 'ammo'
        self.adj = 'reloads'
        self.value = 1
        self.amt = 10

    def use(self, target):
        val = getattr(target, self.stat, 0) + self.value
        s = self.fmtline
        s = s.replace('@NAME', self.name)
        s = s.replace('@TARGET', target.name)
        s = s.replace('@ADJ', self.adj)
        s = s.replace('@STAT', self.stat)
        s = s.replace('@VALUE', str(abs(self.amt)))
        print(s, self.amt)
        #setattr(target, target.amt, val)
        target.amt = val
        self.amt = 0

class Bomb(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Bomb'
        self.adj = 'blasts'
        self.empty = 'The %s has already been detonated!'
        self.value = -100
        self.amt = 1

class HealthPotion(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Health Potion'
        self.adj = 'heals'
        self.value = 10
        self.amt = 1

class Poison(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Belladonna'
        self.adj = 'poisons'
        self.value = -1
        self.amt = 1

class Food(Item):
    def __init__(self, manager):
        Item.__init__(self, manager)
        self.name = 'Food'
        self.fmtline = '@TARGET eats the @NAME '
        self.stat = 'health'
        self.empty = "The %s has already been eaten!"
        self.value = 1
        self.amt = 1

class Door(TileSprite):

    def __init__(self, manager, name, position, imageFileName, parent, gtk):
        TileSprite.__init__(self, manager, imageFileName, parent, position[0], position[1], gtk)
        self.name = 'Door'
        self.value = 100
        self.amt = 1


    def handle(self):
        d = self._parent._mapinfo['door'][self.getDoorData()]
        if d[2] == ok_to_move: #TODO: Crap, what is this?
            return self._parent.moveToNewRoom(d)
        elif d[2] == ask_to_move:
            self.printm("We gotta ask about this move")

    def setDoorData(self, dat):
        self._doordata = dat

    def getDoorData(self):
        return self._doordata
