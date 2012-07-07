#
# encounter_tester.py
# July 17, 2007
# Nick Loadholtes
#
# A tester to try out non-fighting encounters
#
import EncounterManager as em
import Encounter
from Character import Character as pc

def generateParty(num=2, playername='Player'):
    output = []
    for x in xrange(num):
        c = pc(None, "%s_%s" % (playername,x), [0,0], None, None, None)
        output.append(c)
    return output


if __name__ == "__main__":
    goodguys = generateParty(1, 'GoodGuy')
    badguys = generateParty(1, 'BadGuy')
    encmgr = em.EncounterEngine()
    # encmgr.startEncounter(Encounter.encounter)
    encmgr.encounterLoop(goodguys, badguys)



