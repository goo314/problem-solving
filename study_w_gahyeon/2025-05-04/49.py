import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solution(nodeinfo):
    ans = [[], []]
    
    d = dict()
    n = len(nodeinfo)
    for i in range(n):
        x, y = nodeinfo[i]
        d[(x, y)] = i+1
    
    nodeinfo.sort(key=lambda x: x[0])
    nodeinfo.sort(key=lambda x: -x[1])
    
    root = Node(nodeinfo[0])
    def insert(node, val):
        if val[0] < node.val[0]:
            if not node.left:
                node.left = Node(val)
            else:
                insert(node.left, val)
        elif node.val[0] < val[0]:
            if not node.right:
                node.right = Node(val)
            else:
                insert(node.right, val)
    
    for node in nodeinfo[1:]:
        insert(root, node)
    
    def preorder(x):
        if not x:
            return
        a, b = x.val
        ans[0].append(d[(a, b)])
        preorder(x.left)
        preorder(x.right)
    
    def postorder(x):
        if not x:
            return
        a, b = x.val
        postorder(x.left)
        postorder(x.right)
        ans[1].append(d[(a, b)])  
    
    preorder(root)
    postorder(root)
    
    return ans
