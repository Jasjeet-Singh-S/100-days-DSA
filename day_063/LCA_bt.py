# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# this was my code but didnt work , i had gemini fix it but idk how gemini code works but im too tired of this problem, il just folloow tutorials now
# pretty sure the solution can be much smaller and easier if you follow some popular approach.
'''import math

class Solution:
    def lca(self, root, n1, n2):
        order = self.level_order(root, n1, n2)
        parents_n1 = self.complete_arr(self.parent(order, n1))
        parents_n2 = self.complete_arr(self.parent(order, n2))
        i = 0
        for _ in range(min(len(parents_n1), len(parents_n2))):
            if parents_n1[-1-i]==parents_n2[-1-i]:
                i+=1
            else:
                break
        return Node(parents_n1[-i])  # last common parent

    def level_order(self, root, n1, n2):
        order = []
        queue = [root]
        while queue:
            top = queue.pop(0)
            if top!=None:
                queue.append(top.left)
                queue.append(top.right)
                order.append(top.data)
            else:
                # a none node must spawn its empty children as well 
                order.append(None)
                order.append(None)
                order.append(None)
            # STOPPING CONDITION: Once both targets are written into the array, 
            # we can safely stop expanding the tree.
            if n1 in order and n2 in order:
                break
        return order

    def parent(self, order, node):
        i = order.index(node)
        parents = []
        while i>0:
            i = (i-1)//2
            parents.append(order[i])
        parents.append(order[0])
        return parents

    def complete_arr(self, parents):
        actual_len = len(parents)
        levels = math.ceil(math.log2(actual_len+1))
        correct_len = 2**levels - 1
        return parents+[None]*(correct_len-actual_len)'''


class Solution:
    def lca(self, root, n1, n2):
        order = self.level_order(root, n1, n2)
        
        # Paths are generated from Leaf -> Root.
        # We reverse them so they read from Root -> Leaf.
        path_n1 = self.parent(order, n1)[::-1]
        path_n2 = self.parent(order, n2)[::-1]
        
        lca_val = None
        # Compare from the root downwards
        for i in range(min(len(path_n1), len(path_n2))):
            if path_n1[i] == path_n2[i]:
                lca_val = path_n1[i]
            else:
                break
                
        return Node(lca_val) if lca_val is not None else None
        

    def level_order(self, root, n1, n2):
        order = []
        queue = [root]
        
        while queue:
            top = queue.pop(0)
            if top is not None:
                queue.append(top.left)
                queue.append(top.right)
                order.append(top.data)
            else:
                # 1. FIX: Log this absence in 'order'
                order.append(None)
                # 2. FIX: Push its dummy children into 'queue' to preserve the 2i+1 math
                queue.append(None)
                queue.append(None)
            
            # Stop once both values are safely recorded in our array map
            if n1 in order and n2 in order:
                break
        return order


    def parent(self, order, node):
        i = order.index(node)
        parents = []
        # Keep tracking the node itself in the path
        parents.append(order[i])
        while i > 0:
            i = (i - 1) // 2
            parents.append(order[i])
        return parents