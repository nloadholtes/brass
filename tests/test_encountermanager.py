#
# test_encountermanager.py
#

from nose import SkipTest
from nose.tools import assert_equal
from mock import MagicMock as Mock

from nose.tools import *
import EncounterManager as em

class TestEncounterEngine:
    def test___init__(self):
        e = em.EncounterEngine()
        assert e is not None

    def test_determineOrder(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.determineOrder())
        raise SkipTest # TODO: implement your test here

    def test_encounterLoop(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.encounterLoop(goodguys, badguys))
        raise SkipTest # TODO: implement your test here

    def test_getBadguyOrders(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.getBadguyOrders(agressivelevel))
        raise SkipTest # TODO: implement your test here

    def test_isPartyDead(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.isPartyDead(players))
        raise SkipTest # TODO: implement your test here

    def test_playRound(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.playRound())
        raise SkipTest # TODO: implement your test here

    def test_startCombatEncounter(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.startCombatEncounter())
        raise SkipTest # TODO: implement your test here

    def test_startSpeakingEncounter(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.startSpeakingEncounter(encounter))
        raise SkipTest # TODO: implement your test here

    def test_stillFighting(self):
        # encounter_engine = EncounterEngine()
        # assert_equal(expected, encounter_engine.stillFighting())
        raise SkipTest # TODO: implement your test here

class TestInitativeSorter:
    def test_initative_sorter(self):
        # assert_equal(expected, initativeSorter(x, y))
        raise SkipTest # TODO: implement your test here

class TestCreateBadGuys:
    def test_create_bad_guys(self):
        # assert_equal(expected, createBadGuys(amount, level, type))
        raise SkipTest # TODO: implement your test here

class TestActionOrder:
    def test___init__(self):
        action_order = em.ActionOrder("who", "what", "target")
        assert action_order is not None

class TestYesOrNo:
    def test_yes_or_no(self):
        import EncounterManager
        EncounterManager.raw_input = lambda _: 'y' #Mock(return_value='y')
        # import pdb; pdb.set_trace()
        val = EncounterManager.yes_or_no("a", "b")
        assert_equal("a", val)

class TestPause:
    def test_pause(self):
        # assert_equal(expected, pause(dest))
        raise SkipTest # TODO: implement your test here
