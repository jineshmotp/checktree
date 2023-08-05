i = 0
a = []


with open('tree.txt') as f:
    for line in f:
        a.append([int(v) for v in line.split()])

print(a)

nnode = a[0][0]



#######################################################################

def mainf(n):

    subc = 0
 
    subc = subf(n-1)
    return subc

def subf(n):

    # print('subfunstion')
    subnode = len(a[n])
    m = n + 1
    subcc = 0
    subv = 0


    
    # print('length of ',a[n],' is : ',subnode, ' n  val : ', n ,' m  val : ', m )
    
    for k in range(n,0,-1):
        print(k)
        if (a[m][0] not in a[k]):
            print('value : ',a[k][0])
            subcc = subcc + 1
        
                    
        # if (a[m][0] not in a[k]):
        #     print('value : ',a[k][0])
        #     subcc = subcc + 1
    subcc = subcc + subv
    # print('sum : ',subcc)       
    return subcc

#######################################################################


def tree_creation():
    output = nnode +1
    leaf = 0

    for i in range(nnode,0,-1):
        if(len(a[i])==1):
            leaf = leaf + 1
        v = mainf(i)
        print('output of ', a[i][0],' is ',v)
        output = output + v
    
    

    if(leaf > 2):
        leaf =leaf * 2
        output = output + leaf

    # v = mainf(4)
    # print('output of  is ',v)
    # output = output + (pow(2,v) - 1)
    print('Total count is ',output)




tree_creation()



