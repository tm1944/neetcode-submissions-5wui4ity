class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next,self.prev = None,None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
        
    def remove(self,node):
        nxt,prev= node.next,node.prev
        prev.next = nxt
        nxt.prev = prev
        node.next = node.prev = None

    def insert(self,node):
        nxt,prev = self.right,self.right.prev
        nxt.prev = node
        node.next = nxt
        prev.next = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]