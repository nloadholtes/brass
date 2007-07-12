#!/bin/evn python
#
# tester.py
# By Nick Loadholtes
#
# A tester program that simulates a Choose-
# Your-Own-Adventure book.
#
# The file story2.txt is the script for the
# exciting action packed epic: "The house of two rooms"
#
# Enjoy! No warranty on any of this.
#

import pickle

nodes = {}

def mainapp(filename):
    print "Starting!"
    f = open (filename, "r")
    nodes = pickle.load(f)
    f.close()
    print "There were ", len(nodes), " nodes loaded"
    nextnode = 1
    while nextnode != 0:
        node = nodes[nextnode]
        print ">",node[0]
        print "\t",node[1]
        i = 0
        if len(node[2]) == 1:
            nextnode = int(node[2][0])
        else:
            while i < len(node[2]):
                n = int(node[2][i])
                print str(i+1)+")"+nodes[n][0]
                i = i +1
            nextnode = int(raw_input("?"))-1
            nextnode = int(node[2][nextnode])





if __name__ == "__main__":
    mainapp("story2.txt")

