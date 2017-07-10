'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None       
        p1 = p2 = head        
        for i in range(n):
            p2 = p2.next       
        if not p2:
            return head.next        
        while p2 and p2.next != None:
            p2 = p2.next
            p1 = p1.next           
        if p1.next:
            p1.next = p1.next.next
            return head
        else:
            return None