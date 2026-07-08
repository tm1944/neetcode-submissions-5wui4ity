class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #1 -> [key,val]

        self.right,self.left = Node(0,0),Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
    
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self,node):
        nxt,prev = self.right,self.right.prev
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
