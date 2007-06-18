#
# Test the dice functions
# July 2, 2006
#

from util import *

ONE_MILLION = 1000000

def testd6():
    #print '------------ Testing the d6 ---------------'
    counts = [0,0,0,0,0,0,0,0]
    for x in range(ONE_MILLION):
        counts[d6()] += 1
    for i in counts:
        print i, ',',
    print ''
    

if __name__ == '__main__':
    for x in range(6):
        testd6()