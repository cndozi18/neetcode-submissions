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
        dummy = Node(0)
        newNodes = {}
        curr = head
        new = dummy
        while curr != None:
            node = Node(curr.val, curr.next)
            newNodes[curr] = node
            new.next = node
            new = new.next
            curr = curr.next
        curr = head
        while curr != None:
            node = newNodes[curr]
            if curr.random != None:
                node.random = newNodes[curr.random]
            curr = curr.next
        return dummy.next
        