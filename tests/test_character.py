#
# Series of tests to exercise Characters

from nose.tools import raises
from Character import Character as C

@raises(Exception)
def testBadInit():
    c = C()

def testInit():
    c = C(None, "test", (0,0), "none", None, None)
    assert c
