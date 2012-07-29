from nose import SkipTest
from nose.tools import assert_equal, assert_true
from Item import *
from mock import MagicMock as Mock

manager = Mock()

class TestGun:
    def test___init__(self):
        # gun = Gun(manager)
        raise SkipTest # TODO: implement your test here

    def test_use(self):
        # gun = Gun(manager)
        # assert_equal(expected, gun.use(target))
        raise SkipTest # TODO: implement your test here

class TestAmmo:
    def test___init__(self):
        # ammo = Ammo(manager)
        raise SkipTest # TODO: implement your test here

    def test_use(self):
        # ammo = Ammo(manager)
        # assert_equal(expected, ammo.use(target))
        raise SkipTest # TODO: implement your test here

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
        # door = Door(manager, name, position, imageFileName, parent, gtk)
        raise SkipTest # TODO: implement your test here

    def test_getDoorData(self):
        # door = Door(manager, name, position, imageFileName, parent, gtk)
        # assert_equal(expected, door.getDoorData())
        raise SkipTest # TODO: implement your test here

    def test_handle(self):
        # door = Door(manager, name, position, imageFileName, parent, gtk)
        # assert_equal(expected, door.handle())
        raise SkipTest # TODO: implement your test here

    def test_setDoorData(self):
        # door = Door(manager, name, position, imageFileName, parent, gtk)
        # assert_equal(expected, door.setDoorData(dat))
        raise SkipTest # TODO: implement your test here

