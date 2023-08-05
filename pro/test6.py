class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    def create(self, data, children=[]):
        self.data = data
        self.children = children

a = []
with open('tree2.txt') as f:
    # if len(f)>1:
    #     print(len(f))
    for line in f:
        a.append([int(v) for v in line.split()])
        # print(line)
        # Node(a.append([int(v) for v in line.split()]))

print(a)

nnode = a[0][0]
print(a[1])
vk = ''
for i in range(1,nnode+2):
    print('')
    
    for j in range(0,len(a[i])):
        if i == 1 and j == 0:
            if len(a[i]) == 1 :
                vk = vk + 'Node("'+str(a[i][j])+")" 
            else:
                vk = vk + 'Node("'+str(a[i][j])+'",children = ['
        elif i != 1 and j == 0:
            if len(a[i]) == 1 :
                vk = vk + 'Node("'+str(a[i][j])+")" 
            else:
                vk = vk + 'Node("'+str(a[i][j])+'",children = ['
        else:
            if len(a[i]) == 1 :
                vk = vk + 'Node("'+str(a[i][j])+")" 
            else:
                vk = vk + 'Node("'+str(a[i][j])+'",children = ['
                
        vk = vk + ","
    vk = vk + "]"
   
# tree1 =  Node(vk)    
print(vk)

        # Node(a[][])
    
# tree1 = Node(a[1][0])

# print('\n\n\n')
tree = Node(
    "A",
   children = [
        Node("B", children =  [Node("E"), Node("F")]),
        Node("C"),
        Node("D",  children =  [Node("G",  children =  [Node("H"), Node("I"), Node("J"), Node("K")])]),
    ],
)

def paths(root):
    x = []
    v=''
    # print(len(root.children))
    print(root.data[0])
    print('')
    if root.children:
        for c in root.children:
            for el in paths(c):
                x.append(v+c.data + el)
    else:
        x.append("")
    return x


# b = paths(tree)
# print(b)
# c = paths(tree1.data)
# print(c)