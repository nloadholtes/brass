#
# dice.py
#
# Functions for simulating dice
#
# July 2, 2006
#

from random import randint, seed

def reseed():
    return seed(None) #Seeds from system time

def d2():
    return randint(1,2)

def d3():
    return randint(1,3)

def d4():
    return randint(1,4)

def d6():
    return randint(1,6)

def d8():
    return randint(1,8)

def d10():
    return randint(1,10)

def d12():
    return randint(1, 12)

def d20():
    return randint(1, 20)