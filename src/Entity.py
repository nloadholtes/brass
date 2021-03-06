#
# The Entity class is the base class for all items in the world, characters, NPC's, items, etc.
#

from random import randint

class Entity:

    def __init__(self, manager):
        self.manager = manager
        self.manager.registerObserver(self)
        self.image = None

    def register(self, manager):
        self.manager = manager
        self.manager.registerObserver(self)

    def updateData(self, newdict):
        self.__dict__.update(newdict)


class Item(Entity):
    def __init__(self, manager):
        Entity.__init__(self, manager)
        self.name = 'ItemObject'
        self.adj = ('affects','uhhh')
        self.stat = 'health'
        self.empty = 'The %s is empty!'
        self.value = 0
        self.amt = 1
        self.fmtline = "@NAME @ADJ @TARGET for @VALUE"
        self.modifier = 0

    def use(self, target):
        if self.amt < 1:
            print(self.empty % self.name)
        else:
            #Determine the amount of damage done
            val = getattr(target, self.stat, 0) + self.value - self.modifier
            s = self.fmtline
            s = s.replace('@NAME', self.name)
            s = s.replace('@TARGET', target.name)
            if self.adj != None:
                s = s.replace('@ADJ', self.randomEntry(self.adj))
            else:
                s = s.replace('@ADJ', self.adj)
            s = s.replace('@STAT', self.stat)
            s = s.replace('@VALUE', str(abs(self.value)))
            print(s)
            setattr(target, self.stat, val)
            self.amt -= 1

    def randomEntry(self, list):
        size = len(list) - 1
        return list[randint(0,size)]

    def place(self):
        pass

    def equip(self):
        pass

    def unequip(self):
        pass

    def take(self):
        pass

    def takesdamage(self):
        pass

    def __str__(self):
        things = [self.name, str(self.amt)]
        output = "|".join(things)
        return "<Item: " + output + ">"
