#
# encounter_tester.py
# July 17, 2007
# Nick Loadholtes
#
# A tester to try out non-fighting encounters
#
import EncounterManager as em
from Character import Character as pc
from unittest.mock import MagicMock as Mock
import json

def generateParty(num=2, playername='Player'):
    output = []
    for x in range(num):
        c = pc(None, "%s_%s" % (playername,x), [0,0], None, None, None)
        output.append(c)
    return output

def testEncounter():
    goodguys = generateParty(1, 'GoodGuy')
    badguys = generateParty(1, 'BadGuy')
    encmgr = em.EncounterEngine()
    with open("src/encounter.json", "r") as f:
        enc = json.load(f)["test_encounter"]
    # enc = Encounter.test_encounter
    ymock = Mock(return_value=2)
    em.yes_or_no = ymock
    encmgr.startSpeakingEncounter(enc)



