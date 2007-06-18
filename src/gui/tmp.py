import copy

class tmp:
    me = 'me'
    def __init__(self):
        print "can you see ", self.me
        
#    def __init__(self, t):
#        print "or can you see me?"
        
def a():
    print "This is a"
    
def a(x):
    print "This is a(x)"


t = tmp()

a()

numberof = 10
group = []

for x in range(numberof):
    print x
    y = copy.deepcopy(t)
    group.append(y)
    

print group
