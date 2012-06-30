#
# itemloader.py
#
# A loader for the items
from xml.dom import *
import xml.dom.minidom as dom
import json

ITEM_FILE = 'data/items.json'

def loadItemsFromJson(filename):
    return json.loads(filename)

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

def addItem():
    i = {}
    i['name'] = raw_input("Name:")
    i['damage'] = raw_input("damage:")
    return i

def saveItems(data):
    f = open(ITEM_FILE, 'w')
    json.dump(data, f)
    f.close()

if __name__ == '__main__':
    try:
        f = open(ITEM_FILE)
        data = f.read()
        f.close()
    except:
        exit(1)
    output = loadItemsFromJson(data)
    for blah in output:
        print blah
    k = None
    while k is not "q":
        k = raw_input("(a)dd, (l)ist, (s)ave, or (q)uit: ")
        if k is "a":
            output.append(addItem())
        if k is "l":
            for i in output:
                print i
        if k is "s":
            saveItems(output)
