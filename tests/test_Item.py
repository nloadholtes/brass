from nose import SkipTest
from nose.tools import assert_equal, assert_true
from Item import *
from unittest.mock import MagicMock as Mock

manager = Mock()

class TestGun:
    def test___init__(self):
        gun = Gun(manager)
        assert_true(gun is not None)

    def test_use_ammo(self):
        target = Mock()
        target.amt = 10
        target.name = "9mm"
        target.__class__ = Ammo
        gun = Gun(manager)
        gun.use(target)
        assert_equal(0, target.amt)
        assert_equal(11, gun.amt)
    
    def test_use(self):
        target = Mock()
        target.amt = 10
        target.name = "9mm"
        target.__class__ = Gun
        gun = Gun(manager)
        gun.use(target)
        assert_equal(10, target.amt)
        assert_equal(0, gun.amt)

class TestAmmo:
    def test___init__(self):
        ammo = Ammo(manager)
        assert_equal(10, ammo.amt)

    def test_use(self):
        ammo = Ammo(manager)
        target = Mock()
        target.value = 10
        target.name = "mock"
        ammo.use(target)
        assert_equal(0, ammo.amt)

    def test_use_affect_target(self):
        ammo = Ammo(manager)
        target = Mock()
        target.stat = 10
        target.name = "mock"
        ammo.use(target)
        assert_equal(10, target.stat)

class TestBomb:
    def test___init__(self):
        bomb = Bomb(manager)
        assert_true(bomb is not None)

class TestHealthPotion:
    def test___init__(self):
        health_potion = HealthPotion(manager)
        assert_true(health_potion is not None)

class TestPoison:
    def test___init__(self):
        poison = Poison(manager)
        assert_true(poison is not None)

class TestFood:
    def test___init__(self):
        food = Food(manager)
        assert_true(food is not None)

class TestDoor:
    def test___init__(self):
        door = Door(manager, None, (1,1), None, None, None)
        assert_true("Door", door.name)

    def test_handle_ok_to_move(self):
        parent = Mock()
        parent.mapinfo = {'door': [(0,0,ok_to_move)]}
        door = Door(manager, None, (1,1), None, parent, None)
        door.getDoorData = Mock(return_value=(0,0,ok_to_move))
        door.handle()

    def test_handle_ask_to_move(self):
        parent = Mock()
        parent.mapinfo = {'door': []}
        door = Door(manager, None, (1,1), None, parent, None)
        door.getDoorData = Mock(return_value=(0,0,ask_to_move))
        door.handle()

    def test_setDoorData(self):
        door = Door(manager, None, (1,1), None, None, None)
        assert_equal(door._doordata, door.setDoorData("wow"))

    def test_setDoorData(self):
        door = Door(manager, None, (1,1), None, None, None)
        door.setDoorData("wow")
        assert_equal("wow", door.getDoorData())

