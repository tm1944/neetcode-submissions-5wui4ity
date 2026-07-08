class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value

        self.next,self.prev = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left

    def remove(self,node):
        nxt,prev = node.next,node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
