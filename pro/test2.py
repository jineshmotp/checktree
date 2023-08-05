import numpy as np

i = 0
a = []
n = 1
output = 1

with open('tree3.txt') as f:
    for line in f:
        a.append([int(v) for v in line.split()])
print(a)
nnode = a[0][0]
print(nnode)
print('\n#############################################\n')

def f(n):
    if n == 1:
        return 1
 
    else:
        return (g(n-1))
 
def g(n):
    if n == 1:
        return 1
 
    else:
        return (f(n-1)+g(n-1))

#######################################################################        

def mainf(n):
    if n == 1:
        return 1
 
    else:
        subn = len(a[0][n])
        if subn == 1:
            return (subf(n-1))

def subf(n):
    if n == 1:
        return 1
 
    else:
        if (a[n+1] in a[n]):
            subn = len(a[n][0])
            if subn != 1:
                return (subf(n-1))

#######################################################################
    

output = output + nnode
n = int(a[0][0])



print ("Number of items in the list = ", len(a))
print ("Number of nodes in tree  = ", a[0][0])
print ("Number of items in the list 0 = ", len(a[0]))
print ("Number of items in the list 1 = ", len(a[1]))
print ("Number of items in the list 2 = ", len(a[2]))
print ("Number of items in the list 3 = ", len(a[3]))


def tree_creation(): 

    print("Number of independent sets : ",f(n) + g(n))  
    print(output)     
tree_creation()