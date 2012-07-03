#
# Test the dice functions
# July 2, 2006
#

from util import *

ONE_MILLION = 1000000

def manualtestd6():
    #print '------------ Testing the d6 ---------------'
    counts = [0,0,0,0,0,0,0,0]
    for x in xrange(ONE_MILLION):
        counts[d6()] += 1
    for i in counts:
        print i, ',',
    print ''


if __name__ == '__main__':
    for x in xrange(6):
        manualtestd6()
