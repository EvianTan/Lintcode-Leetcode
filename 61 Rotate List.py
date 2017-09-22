'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curt = dummy
        size = 0
        while curt.next != None:
            size += 1
            curt = curt.next
        k = k%size
        if k==0:
            return head
        curt = dummy
        for i in range(size-k):
            curt = curt.next
        newHead = curt.next
        curt.next = None
        curt = newHead
        while curt.next != None:
            curt = curt.next
        curt.next = head
        return newHead