#
# Sample code from the Pygame mailing list. This shows
# a simple RPG like data-driven simulation.
#
# May 26, 2006
#

class Person(object):
    name = 'Person'
    health = 50
    hunger = 10
    def __setattr__(self, key, val):
        if key == 'health':
            if val < 1:
                print("%s is dead!" % self.name)
            else:
                print("%s has %d %s remaining" % (self.name, val, key))
        elif key == 'hunger':
            if val > 100:
                print("%s has starved to death!" % self.name)
            else:
                print("%s is %d%% hungry" % (self.name, val))
        object.__setattr__(self, key, val)

class GameObject(object):
    name = 'GameObject'
    adj = 'affects'
    stat = 'health'
    empty = 'The %s is empty!'
    value = -1
    amt = 1
    fmtline = "@NAME @ADJ @TARGET for @VALUE"
    def Use(self, target):
        if self.amt < 1:
            print(self.empty % self.name)
        else:
            val = getattr(target, self.stat, 0) + self.value
            s = self.fmtline
            s = s.replace('@NAME', self.name)
            s = s.replace('@TARGET', target.name)
            s = s.replace('@ADJ', self.adj)
            s = s.replace('@STAT', self.stat)
            s = s.replace('@VALUE', str(self.value))
            print(s)
            setattr(target, self.stat, val)
            self.amt -= 1

class MachineGun(GameObject):
    name = 'Machine gun'
    adj = 'shoots'
    value = -10
    amt = 100

class Bomb(GameObject):
    name = 'Bomb'
    adj = 'blasts'
    empty = 'The %s has already been detonated!'
    value = -100
    amt = 1

class HealthPotion(GameObject):
    name = 'Health Potion'
    adj = 'heals'
    value = 10
    amt = 1

class Poison(GameObject):
    name = 'Belladonna'
    adj = 'poisons'
    value = -1
    amt = 1

class Food(GameObject):
    name = 'Banana'
    fmtline = '@TARGET eats the @NAME '
    stat = 'health'
    empty = "The %s has already been eaten!"
    value = 1
    amt = 1
        

def main():

    person = Person()
    machinegun = MachineGun()
    for i in range(5):
        machinegun.Use(person)

    person = Person()
    bomb = Bomb()
    bomb.Use(person)
    bomb.Use(person)

    person = Person()
    machinegun = MachineGun()
    for i in range(4):
        machinegun.Use(person)

    potion = HealthPotion()
    potion.Use(person)

    poison = Poison()
    poison.Use(person)

    banana = Food()
    banana.Use(person)
    banana.name = 'testing'
    banana.Use(person)
    
    #
    # test code by Nick
    

main()

''' Sample output follows:

Machine gun shoots Person for -10
Person has 40 health remaining
Machine gun shoots Person for -10
Person has 30 health remaining
Machine gun shoots Person for -10
Person has 20 health remaining
Machine gun shoots Person for -10
Person has 10 health remaining
Machine gun shoots Person for -10
Person is dead!
Bomb blasts Person for -100
Person is dead!
The Bomb has already been detonated!
Machine gun shoots Person for -10
Person has 40 health remaining
Machine gun shoots Person for -10
Person has 30 health remaining
Machine gun shoots Person for -10
Person has 20 health remaining
Machine gun shoots Person for -10
Person has 10 health remaining
Health Potion heals Person for 10
Person has 20 health remaining
Belladonna poisons Person for -1
Person has 19 health remaining
Person eats the Banana
Person is 9% hungry
The Banana has already been eaten!
'''
