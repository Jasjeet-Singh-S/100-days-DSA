# https://leetcode.com/problems/lru-cache/description/
# watch leetcode solution for this 

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map they key to node
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 
        # left is LRU and right is MRU

    def remove_node(self, node):
        # remove node from anywhere
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_node(self, node):
        # insert node at right
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next 
            self.remove_node(lru)
            del self.cache[lru.key]