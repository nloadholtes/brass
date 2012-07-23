from nose import SkipTest
from nose.tools import assert_equals, assert_is_not_none
from mock import MagicMock as Mock

from tileengine import TileEngine

eventmanager = Mock()
gamedata = Mock()
eventmanager.registerObserver = Mock()
gamedata.get = Mock(return_value=(0,0))

class TestTileEngine:
    def test___init__(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        assert_is_not_none(tile_engine)

    def test_addPlayer(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.addPlayer(image, startpos, stats))
        raise SkipTest # TODO: implement your test here

    def test_centerOn(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.centerOn(sprite))
        raise SkipTest # TODO: implement your test here

    def test_encounterHandler(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.encounterHandler(evt))
        raise SkipTest # TODO: implement your test here

    def test_getImage(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.getImage(imagename))
        raise SkipTest # TODO: implement your test here

    def test_initTE(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.initTE(gtk))
        raise SkipTest # TODO: implement your test here

    def test_loadMap(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.loadMap(mapname))
        raise SkipTest # TODO: implement your test here

    def test_loadSprites(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.loadSprites(spritelist))
        raise SkipTest # TODO: implement your test here

    def test_move(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.move(direction))
        raise SkipTest # TODO: implement your test here

    def test_moveOk(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.moveOk(newx, newy))
        raise SkipTest # TODO: implement your test here

    def test_moveToNewRoom(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.moveToNewRoom(door))
        raise SkipTest # TODO: implement your test here

    def test_notify(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.notify(evt))
        raise SkipTest # TODO: implement your test here

    def test_paint(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.paint())
        raise SkipTest # TODO: implement your test here

    def test_paintSprite(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.paintSprite(sprite))
        raise SkipTest # TODO: implement your test here

    def test_removeSprite(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.removeSprite(sprite))
        raise SkipTest # TODO: implement your test here

    def test_setMessage(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.setMessage(messagestr))
        raise SkipTest # TODO: implement your test here

