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
        oldtoCopy = {None:None}

        cur = head
        # pass 1 to copy
        while cur:
            copy = Node(cur.val)
            oldtoCopy[cur] = copy
            cur = cur.next
        
        # Pass 2 to link pointers
        cur = head
        while cur:
            copy = oldtoCopy[cur]
            copy.next = oldtoCopy[cur.next]
            copy.random = oldtoCopy[cur.random]
            cur = cur.next
        
        return oldtoCopy[head]
        