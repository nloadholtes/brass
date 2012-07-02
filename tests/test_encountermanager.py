#
# test_encountermanager.py
#

import unittest
import EncounterManager as em

def testEncounterEngineInit():
    e = em.EncounterEngine()
    assert e is not None
