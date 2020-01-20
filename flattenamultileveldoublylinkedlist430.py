"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution1:
    def flatten(self, head: 'Node') -> 'Node':
        # recursion 
        # this is like a tree, 
        # traverse the linked list, 
        # when bump into a node with child, hold on to the next node, connect to the child, then connect the child to next.
        def flattenlist(node,prev):
            if node == None:
                return prev
            node.prev = prev
            prev.next = node
            tempNext = node.next
            tail = flattenlist(node.child, node)
            node.child = None
            return flattenlist(tempNext,tail)

        if head == None:
            return None
        else:
            fakehead = Node(None, None, head, None)
            flattenlist(head,fakehead)
            fakehead.next.prev = None
            return fakehead.next


class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        # result: put child nodes linked list to next and put next right after the end of that child node linked list. 
        #treat child node as left and next node as right
        # attached left and then attach right.
        # next == None then return None'
        
            