'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head is not None:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        bTail.next = None
        aTail.next = bHead.next
        return aHead.next