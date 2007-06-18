#
# itemloader.py
#
# A loader for the items
from xml.dom import *
import xml.dom.minidom as dom

def loadItemsFromXML(filename):
    from Entity import Item
    doc = dom.parse(filename)
    itemlist = []
    print 'doc is ', doc
    for items in doc.childNodes:
        for itemx in items.childNodes:
            if itemx.nodeType == Node.ELEMENT_NODE:
                thing = Item()
                for item in itemx.childNodes:
                    if item.nodeName != '#text':
                        thing = createObjectFromXML(thing, item)
                print thing
                itemlist.append(thing)
    return itemlist
    
def createObjectFromXML(obj, nodes):
    '''Creates an object from a xml document'''
    name = nodes.localName
    for node in nodes.childNodes:
        #print name, " - ", node.nodeValue
        setattr(obj, str(node.parentNode.localName), node.nodeValue)
    return obj

if __name__ == '__main__':
    output = loadItemsFromXML('data/items.xml')
    for blah in output:
        print blah
    