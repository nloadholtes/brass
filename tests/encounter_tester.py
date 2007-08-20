#
# encounter_tester.py
# July 17, 2007
# Nick Loadholtes
#
# A tester to try out non-fighting encounters
#
from EncounterManager import *

#def startenc(encounter):
#    print "Starting encounter:"
#    print 'Preamble: ', encounter['preamble']
#    x = 1
#    while(x):
#        topic = encounter['conversation'][x]
#        print "\t",topic[0]
#        if(len(topic) > 1):
#            x = eval(topic[1])
        


if __name__ == "__main__":
    encounters = {}
    execfile('../src/encounter.py', globals(), encounters)
    print encounters['encounter']['title']
    encmgr = EncounterEngine(createBadGuys(1, 1, 0))
    encmgr.startEncounter(encounters['encounter'])
#    target = raw_input()
#    if target == '1':




