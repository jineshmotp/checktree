# Data structure to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to find the size of the maximum independent set
# for a binary tree
def findMIS(root, d):

    print('The size of a maximum independent set is', root)
    
    # base case: empty tree
    if root is None:
        return 0
 
    if root in d:
        return d[root]
 
    # Case 1: Exclude the current node from the maximum independent set and
    # recur for its left and right child
    excl = findMIS(root.left, d) + findMIS(root.right, d)
 
    # Case 2: Include the current node in the maximum independent set and
    # recur for its grandchildren
    incl = 1
 
    if root.left:
        incl += findMIS(root.left.left, d) + findMIS(root.left.right, d)
        print(incl)
 
    if root.right:
        incl += findMIS(root.right.left, d) + findMIS(root.right.right, d)
 
    # save and return the maximum number of nodes possible by either
    # including or excluding the current node
    d[root] = max(excl, incl)
    return d[root]


def f(root,n):
    if n == 1:
        return 1
 
    else:
        return (g(n-1))**2
 
 def g(root,n):
    if n == 1:
        return 1
 
    else:
        return (f(n-1)+g(n-1))**2
 
 
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    d = {}
   
    print('The size of a maximum independent set is', findMIS(root, d))# Data structure to store a binary tree node
