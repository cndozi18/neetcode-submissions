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
        newNodes = {None:None}
        curr = head
        while curr != None:
            node = Node(curr.val)
            newNodes[curr] = node
            curr = curr.next
        curr = head
        while curr != None:
            node = newNodes[curr]
            node.next = newNodes[curr.next]
            node.random = newNodes[curr.random]
            curr = curr.next
        return newNodes[head]
        