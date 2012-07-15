#
# test_encountermanager.py
#

from nose.tools import *
import EncounterManager as em

def testEncounterEngineInit():
    e = em.EncounterEngine()
    assert e is not None
