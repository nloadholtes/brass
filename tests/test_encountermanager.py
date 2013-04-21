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
        encounter_engine = em.EncounterEngine()
        player1 = Mock()
        player1.health = 0
        player2 = Mock()
        player2.health = 0
        players = [player1, player2]
        assert_equal(True, encounter_engine.isPartyDead(players))

    def test_isPartyDead_one_alive(self):
        encounter_engine = em.EncounterEngine()
        player1 = Mock()
        player1.health = 0
        player2 = Mock()
        player2.health = 1
        players = [player1, player2]
        assert_equal(False, encounter_engine.isPartyDead(players))

    def test_isPartyDead_all_alive(self):
        encounter_engine = em.EncounterEngine()
        player1 = Mock()
        player1.health = 10
        player2 = Mock()
        player2.health = 1
        players = [player1, player2]
        assert_equal(False, encounter_engine.isPartyDead(players))

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
        assert_true(em.createBadGuys(3, None, "blah") is not None)

class TestActionOrder:
    def test___init__(self):
        action_order = em.ActionOrder("who", "what", "target")
        assert action_order is not None

