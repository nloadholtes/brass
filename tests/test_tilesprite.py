import unittest
from nose import SkipTest
from nose.tools import assert_equal, assert_is_not_none
from unittest.mock import MagicMock as Mock

from tilesprite import TileSprite
from Events import PrintEvent

manager = Mock()
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
        parent = Mock()
        parent.moveOk = Mock(return_value=None)
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal((0,0), tile_sprite.getXY())
        assert_equal(None, tile_sprite.move((0,1)))
        assert_equal((0,1), tile_sprite.getXY())

    def test_moveNotOk(self):
        parent = Mock()
        parent.moveOk = Mock(return_value=False)
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal((0,0), tile_sprite.getXY())
        assert_equal(False, tile_sprite.move((0,1)))
        assert_equal((0,0), tile_sprite.getXY())

    def test_occupied(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal(0, tile_sprite.occupied((x,y + 1)))

    def test_occupiedBySelf(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal(1, tile_sprite.occupied((x,y)))

    def test_occupiedSomeoneElseNoOneThere(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        assert_equal(False, tile_sprite.occupied((x+1, y+1)))

    def test_paint(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        tile_sprite._image = None
        screen = None
        location = (x,y)
        tile_sprite.paint(screen, location)

    def test_paintImage(self):
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        tile_sprite._image = Mock()
        tile_sprite._image.blit = Mock()
        screen = None
        location = (x,y)
        tile_sprite.paint(screen, location)
        # tile_sprite._image.blit.assert_called_once()

    def test_printm(self):
        manager.notify = Mock()
        tile_sprite = TileSprite(manager, imageFilename, parent, x, y, gtk)
        tile_sprite.printm("test text")
        # manager.notify.assert_called_once()

