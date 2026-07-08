class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

        self.next = self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right,self.left = Node(0,0),Node(0,0)

        self.right.prev,self.left.next = self.left,self.right

    def remove(self,node):
        prev, nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev

    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        prev.next,node.prev = node,prev
        node.next,nxt.prev = self.right,node
        

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
        
