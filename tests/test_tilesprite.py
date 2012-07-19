import unittest
from nose import SkipTest
from nose.tools import assert_equal, assert_is_not_none

from tilesprite import TileSprite

manager = None
imageFilename = ""
parent = None
x = 0
y = 0
gtk = None

class TestTileSprite:
    def test___init__(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_is_not_none(tile_sprite)

    def test_getXY(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal((x,y), tile_sprite.getXY())

    def test_handle(self):
        # tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        # assert_equal(expected, tile_sprite.handle())
        raise SkipTest # TODO: implement your test here

    def test_move(self):
        # tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        # assert_equal(expected, tile_sprite.move(direction))
        raise SkipTest # TODO: implement your test here

    def test_occupied(self):
        # tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        # assert_equal(expected, tile_sprite.occupied(intruder))
        raise SkipTest # TODO: implement your test here

    def test_paint(self):
        # tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        # assert_equal(expected, tile_sprite.paint(screen, location))
        raise SkipTest # TODO: implement your test here

    def test_printm(self):
        # tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        # assert_equal(expected, tile_sprite.printm(text))
        raise SkipTest # TODO: implement your test here

