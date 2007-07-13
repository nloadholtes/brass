#
# EncounterManager.py
#
# This class will simulate encounters
#

from Character import *
from EventMngr import *
from Group import *
from random import randint

class EncounterEngine:
    def __init__(self, opponents):
        print 'Starting Encounter Engine'
        self.goodguys = []
        if isinstance(opponents, Group):
            self.badguys = opponents.characters
        else:
            self.badguys = [opponents.entity]
        self.fightorder = []
        self.orders = []
        
    def playRound(self):
        '''This method will execute one round of combat'''
        print 'Staring a round'
        for person in self.fightorder:
            orders = person.orders
            for order in orders:
                #print 'Executing: ', order
                who = order.who
                what = "who." + str(order.what) + "(order.target)" 
                #print "\tWho ->", person.name, "What ->", what
                eval(what)
            person.orders = []

        
    def determineOrder(self):
        '''This method looks at each persons\'s initiative and uses that
        to determine the fight order.'''
        [self.fightorder.append(guy) for guy in self.goodguys]
        [self.fightorder.append(guy) for guy in self.badguys]
        self.fightorder.sort(initativeSorter)
        for person in self.fightorder:
            print "fight order =>", person.name
                
    def stillFighting(self):
        '''Checks the good guys and bad guys (separeately) to see if
        either side is all dead. Eventually will need to check to see if they
        have fled, but for the time being its a fight to the death'''
        if self.isPartyDead(self.goodguys):
            return False
        if self.isPartyDead(self.badguys):
            return False
        return True
    
    def isPartyDead(self, players):
        '''Checks for vital signs. If someone is still kicking then return true'''
        for player in players:
            print "Checking: ", player.name, player.health
            if player.health <= 0:
                players.remove(player)
        if 0 == len(players):
            return True
        else:
            return False
    
    def setOrders(self, who, what, target):
        order = ActionOrder(who, what, target)
        self.orders.append(order)
        return None

    def getBadguyOrders(self, badguys, goodguys, agressivelevel):
        '''A first attempt at an AI system to control the bad guys
    and have them attack the goodguys.'''
        for dude in self.badguys:
            gsize = len(self.goodguys)
            t = randint(0, gsize-1)
            order = ActionOrder(dude, 'attack', goodguys[t])
            dude.orders.append(order)
            print '->',dude.name,'is thinking...', order


    def startEncounter(self, goodguys):
        '''This starts the encounter, determining the order and then playing
        a round.'''
        print 'Starting!'
        self.goodguys = goodguys
        stillgoing = True
        self.determineOrder()
        #Clear out the orders for everyone
        [ person.orders = [] for person in self.fightorder]
            
#
# Helper functions for these classes
#
def initativeSorter(x, y):
    return cmp(y.getInit(), x.getInit())

def createBadGuys(amount, level, type):
    '''Create a list of bad guys'''
#    badguylist = []
    mngr = EventManager()
    group = Group(mngr, "Gangsters", (0,0), "img/player.png")
    group.populateClones(Character(mngr, 'Bad Guy', (0,0), 'none'), amount)
    return group

class ActionOrder:
    '''This class is that data structure to describe the orders that a character
    should do during an Encounter round.'''
    WHAT = ('attack', 'EVADE', 'USE', 'TALK')
    def __init__(self, who, what, target):
        self.who = who
        self.what = what
        self.target = target
        
