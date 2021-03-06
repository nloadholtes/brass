from nose import SkipTest
from nose.tools import assert_equals, assert_is_not_none, assert_equal
from unittest.mock import MagicMock as Mock

from tileengine import TileEngine

eventmanager = Mock()
eventmanager.registerObserver = Mock()
gamedata = {'playerlocation': (0, 0), 'maplist': ["mockmap"],
            'playerimage': "something", 'startingmap': 0}
gtk = Mock()
gtk.getImage = Mock(return_value="something")


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
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine.encounterHandler(None)

    def test_getImageNone(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        assert_equal(None, tile_engine.getImage(None))

    def test_getImage(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine.gtk = gtk
        assert_equal("something", tile_engine.getImage("Something.png"))

    def test_initTE(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine.loadMap = Mock()
        tile_engine.paint = Mock()
        tile_engine.initTE(gtk)
        # gtk.assert_called()

    def test_loadMap(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.loadMap(mapname))
        raise SkipTest # TODO: implement your test here

    def test_loadSprites(self):
        # tile_engine = TileEngine(eventmanager, gamedata)
        # assert_equal(expected, tile_engine.loadSprites(spritelist))
        raise SkipTest # TODO: implement your test here

    def test_move(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine.ego = Mock()
        tile_engine.ego.position = (0,0)
        tile_engine.moveOk = Mock(return_value=None)
        assert_equal(None, tile_engine.move((0,1)))

    def test_moveOkFalse(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine._map = ([[],[]], [[],[]])
        tile_engine.passable = []
        assert_equal(False, tile_engine.moveOk(0, 0))

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
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine._tilewidth = 32
        tile_engine._tileheight = 32
        tile_engine._offset = (0,0)
        sprite = Mock()
        sprite.position = (10,10)
        sprite.image = Mock()
        sprite.image.blit = Mock()
        tile_engine.paintSprite(sprite)
        # sprite.image.blit.assert_called_once()

    def test_removeSpriteInvalid(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        sprite = [(0,0), "b", "image", {}]
        tile_engine.loadSprites([])
        tile_engine.removeSprite(sprite)
        assert_equal(0, len(tile_engine._sprites))

    def test_removeSprite(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        sprite = [(0,0), "b", "image", {}]
        tile_engine.images = {"image": 0}
        tile_engine.gtk = gtk
        tile_engine.loadSprites([sprite])
        s = tile_engine._sprites[0]
        tile_engine.removeSprite(s)
        assert_equal(0, len(tile_engine._sprites))

    def test_setMessage(self):
        tile_engine = TileEngine(eventmanager, gamedata)
        tile_engine.setMessage("test str")
        assert_equal("test str", tile_engine._msgstr)

