#!/usr/bin/env python
#
# mapmaker.py
# Aug 15, 2007
# Nick Loadholtes
#
# This is a tool to create a quick and dirty map
#
import sys

def createMap(xsize, ysize, name):
    '''Gonna make a quick and dirty map'''
    f = open(name, "w")
    # The map
    f.write("_map = [")
    for x in range(int(xsize)):
        f.write("\"")
        for y in range(int(ysize)):
            f.write(" ")
        f.write("\",\n")
    f.write("]\n\n")

    #Map info
    f.write("_mapinfo = {\n\t 'passable' : ['.'], \n\t'door' : ()\n}\n\n")

    #Sprites
    f.write("sprites = [[]]\n\n")

    #Images
    f.write("images = {\n\t'?' : 'img/missing.png'\n}\n")
    f.close()
    
if __name__ == "__main__":
    if(len(sys.argv) == 4):
        createMap(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Error: Please supply an x size, y size, and a map name")
