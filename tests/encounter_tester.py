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
from mock import MagicMock as Mock

def generateParty(num=2, playername='Player'):
    output = []
    for x in xrange(num):
        c = pc(None, "%s_%s" % (playername,x), [0,0], None, None, None)
        output.append(c)
    return output

def testEncounter():
    goodguys = generateParty(1, 'GoodGuy')
    badguys = generateParty(1, 'BadGuy')
    encmgr = em.EncounterEngine()
    enc = Encounter.test_encounter
    ymock = Mock(return_value=2)
    em.yes_or_no = ymock
    encmgr.startSpeakingEncounter(enc)



