#from tilesprite import TileSprite
from Character import Character
import copy


class Group:
    '''This class represents a collection of characters that are all in one location
    on the map (i.e. a pack of dogs, etc.)'''
    location = []
    characters = []

    def __init__(self, manager, name, position, imageFileName):
        #TileSprite.__init__(self, imageFileName, manager, position[0], position[1], group)
        pass

    def populateClones(self, who, numberof):
        '''Bulk adds clones of who to the group'''
        for x in range(numberof):
            print "Adding x"
            self.characters.append(copy.deepcopy(who))

    def addSingle(self, who):
        '''Adds a single Character to the group'''
        self.characters.append(who)
