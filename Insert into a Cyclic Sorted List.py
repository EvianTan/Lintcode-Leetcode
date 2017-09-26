'''
Given a node from a cyclic linked list which has been sorted, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be any single node in the list. Return the inserted new node.

 Notice

3->5->1 is a cyclic list, so 3 is next node of 1.
3->5->1 is same with 5->1->3

Have you met this question in a real interview? Yes
Example
Given a list, and insert a value 4:
3->5->1
Return 5->1->3->4
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        if node is None:
            node = ListNode(x)
            node.next = node
            return node
        p = node
        prev = None
        while True:
            prev = p
            p = p.next
            if x <= p.val and x >= prev.val:
                break
            if (prev.val > p.val) and (x < p.val or x > prev.val):
                break
            if p is node:
                break

        newNode = ListNode(x)
        newNode.next = p
        prev.next = newNode
        return newNode