"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None:None}
        curr = head
        while curr:
            node = Node(curr.val)
            hmap[curr] = node
            curr = curr.next

        curr = head
        while curr:
            node = hmap[curr]
            node.next = hmap[curr.next]
            node.random = hmap[curr.random]
            curr = curr.next
        return hmap[head] 
