i = 0
a = []


with open('tree.txt') as f:
    for line in f:
        a.append([int(v) for v in line.split()])

print(a)

nnode = a[0][0]



#######################################################################

def f(n):
    if n == 1:
        return 1
    else:
        return (g(n-1))

def g(n):
    if n == 1:
        return 1
    else:
        return (f(n-1) + g(n-1))

def mainf(n):

    subc = 0
 
    subc = subc + subf(n-1)
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
    output = 0
    leaf = 0
    flag = 0

    for i in range(nnode,0,-1):
        if(len(a[i])%2 == 0):
            flag = 1
        if(len(a[i])==1):
            leaf = leaf + 1
    # print('flag value : ', flag,' ',nnode)

    for i in range(nnode,0,-1):
        v = mainf(i)
        print('output of ', a[i][0],' is ',v)
        output = output + v
    print(output)
    output = output + nnode + 1
    print(leaf)
    if(leaf > 2):
        output = output + (leaf*2)
    print(output)


    # if flag == 1:

    #     for i in range(nnode,0,-1):
    #         v = mainf(i)
    #         print('output of ', a[i][0],' is ',v)
    #         output = output + v
    #     print(output)
    #     output = nnode +1

    #     if(leaf > 2):
    #         leaf =leaf * 2
    #         output = output + leaf

        
    #     print('Total count is ',output)

    # else:
    #     if leaf %2 == 0 :
    #         output = f(nnode)+g(nnode)
    #     else:
    #         output = 1+ f(nnode)+g(nnode)
    #     print('binary tree Total count is ',output)

tree_creation()



