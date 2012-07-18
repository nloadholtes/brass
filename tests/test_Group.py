from nose import SkipTest
from nose.tools import assert_equal
from Group import Group

manager = None
name = None
position = None
imageFileName = None

class TestGroup:
    def test___init__(self):
        group = Group(None, None, None, None)
        assert group is not None

    def test_addSingle(self):
        group = Group(manager, name, position, imageFileName)
        assert_equal(0, len(group.characters))
        group.addSingle({})
        assert_equal(1, len(group.characters))

    def test_populateClones(self):
        group2 = Group(manager, name, position, imageFileName)
        assert_equal(0, len(group2.characters))
        group2.populateClones({}, 20)
        assert_equal(20, len(group2.characters))
