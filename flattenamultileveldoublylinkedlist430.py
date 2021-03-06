
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

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
        #result: return head
        headNode = head
        while headNode != None:
            if headNode.child != None:
                childNode = headNode.child
                nextNode = headNode.next
                headNode.next = self.flatten(childNode)
                childNode.prev = headNode
                TailNode = childNode
                while TailNode.next != None:
                    TailNode = TailNode.next
                TailNode.next = nextNode
                if nextNode != None:
                    nextNode.prev = TailNode
                headNode.child = None
            headNode = headNode.next
           
                
        return head
class Solution3:
    # Andy's solution
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        '''when dealing with recursion, think from the angle of the smaller problems. 
        think that the smaller problem is solved, how is it attached to the bigger problem
        layer to layer, how is it attached. in this one, node 7 is the beginning of the smaller problem, 
        think that this childnode and all its child and next are all already taken care of by the recursive function
        to combine it to the upper level, what needs to be done. 1. the upper level need to take it as next node, and its original next node as a floating node, 
        then find the tail of the node 7 cluster, that is the previous of its original next node's previous'''
        # recursive solution
        ptr = head
        while(ptr):
            if ptr.child==None:
                ptr = ptr.next
            else:
                H = self.flatten(ptr.child)
                T = H
                while(T.next):
                    T = T.next
                # connect T, H into ptr
                T.next = ptr.next
                if ptr.next: #remember when dealing with linkedlist, before making any statement about a node, always check if it's None. 
                    ptr.next.prev = T
                ptr.next = H
                H.prev = ptr
                ptr.child = None
                ptr = ptr.next
        return head
class Solution4:
    def flatten(self,head):
        def dfs(head, prev):
            if head == None:
                return prev
            head.prev = prev
            nodeN
        if head == None:
            return None
        else:
            fakehead = Node(0)
            fakehead.next = head
            head.prev = fakehead
            dfs(head,fakehead)
            return head
                

            

            