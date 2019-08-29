#
# itemloader.py
#
# A loader for the items
import json

ITEM_FILE = 'data/items.json'

def loadItemsFromJson(filename):
    return json.loads(filename)

def addItem():
    i = {}
    i['name'] = raw_input("Name: ")
    i['damage'] = int(raw_input("Damage: "))
    i['critical'] = int(raw_input("Critical: "))
    i['weight'] = int(raw_input("Weight: "))
    i['size'] = raw_input("Size")
    i['ammotoype'] = raw_input("Ammo Type: ")
    return i

def saveItems(data):
    f = open(ITEM_FILE, 'w')
    json.dump(data, f, indent=1)
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
        print(blah)
    k = None
    while k is not "q":
        k = raw_input("(a)dd, (l)ist, (s)ave, or (q)uit: ")
        if k is "a":
            output.append(addItem())
        if k is "l":
            for i in output:
                print(i)
        if k is "s":
            saveItems(output)
