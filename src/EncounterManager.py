#
# EncounterManager.py
#
# This class will simulate encounters
#

from Character import *
from EventMngr import *
from Group import *
from random import randint
import logging
import logging.config

logging.config.fileConfig("logging.conf")
log = logging.getLogger(__name__)


class EncounterEngine:
    def __init__(self):
        log.debug('Starting Encounter Engine')
        self.goodguys = []
        self.fightorder = []
        self.orders = []
        self.badguys = []

    def playRound(self):
        '''This method will execute one round of combat'''
        log.debug('Staring a round')
        for person in self.fightorder:
            #print "---%s is executing" % person.name
            if person.health <= 0:
                continue
            orders = person.orders
            for order in orders:
                order.who.executeOrder(order)
        #After fight, reset players
        [person.resetAfterCombat() for person in self.fightorder]
        for guy in self.goodguys:
            if guy.health <= 0:
                self.goodguys.remove(guy)
        for badguy in self.badguys:
            if badguy.health <= 0:
                self.badguys.remove(badguy)

    def determineOrder(self):
        '''This method looks at each persons\'s initiative and uses that
        to determine the fight order.'''
        log = logging.getLogger(__name__+".determineOrder")
        [self.fightorder.append(guy) for guy in self.goodguys]
        [self.fightorder.append(guy) for guy in self.badguys]
        self.fightorder.sort(initativeSorter)
        log.debug("Fight order:")
        for person in self.fightorder:
            log.debug("\t%s" % person.name)

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
        playercount = len(players)
        for player in players:
            #print "Checking: ", player.name, player.health
            if player.health <= 0:
                playercount -= 1
        if 0 == playercount:
            return True
        else:
            return False

    def getBadguyOrders(self, agressivelevel):
        '''A first attempt at an AI system to control the bad guys
    and have them attack the goodguys.'''
        for dude in self.badguys:
            gsize = len(self.goodguys)
            t = randint(0, gsize-1)
            order = ActionOrder(dude, 'attack', self.goodguys[t])
            dude.orders.append(order)
            log.debug('->%s is thinking... %s' % (dude.name, order))

    def startCombatEncounter(self):
        '''This starts the encounter, determining the order and then playing
        a round.'''
        log.debug('startingCombatEncounter')
        stillgoing = True
        self.determineOrder()
        #Clear out the orders for everyone
        for person in self.fightorder:
            person.orders = []

    def startSpeakingEncounter(self, encounter):
        '''This method is where Speaking/interacting encounters start.'''
        log.debug("Starting Speaking encounter:")
        if isinstance(encounter, EncounterEvent):
            encounter = encounter.encounter
        log.debug('Preamble: %s' % encounter['preamble'])
        x = 1
        while(x):
            topic = encounter['conversation'][x]
            log.debug("\t %s" % topic[0])
            if(len(topic) > 1):
                x = eval(topic[1])
        return x

    def encounterLoop(self, goodguys, badguys):
        self.goodguys = goodguys
        self.badguys = badguys
        #TODO: Logic to determine the type of encoutner?
        self.startCombatEncounter()
        while self.stillFighting():
            self.getBadguyOrders(1)
            self.playRound()


#
# Helper functions for these classes
#
def initativeSorter(x, y):
    b = x.getInit()
    a = y.getInit()
    return (a > b) - (a < b)


def createBadGuys(amount, level, type):
    '''Create a list of bad guys'''
#    badguylist = []
    mngr = EventManager()
    group = Group(mngr, "Gangsters", (0, 0), "img/player.png")
    group.populateClones(Character(mngr, 'Bad Guy', (0, 0), "", None, None), amount)
    return group


class ActionOrder:
    '''This class is that data structure to describe the orders that a character
    should do during an Encounter round.'''
    WHAT = ('attack', 'EVADE', 'USE', 'TALK')

    def __init__(self, who, what, target):
        self.who = who
        self.what = what
        self.target = target


#
# These are the functions that get called from the
# encounter scripts.
#
def yes_or_no(dest1, dest2):
    print("Y)es\nN)o")
    ans = raw_input()
    if 'y' == ans.lower():
        return dest1
    else:
        return dest2


def pause(dest):
    print("Need to have the user press something to continue..")
    return dest
