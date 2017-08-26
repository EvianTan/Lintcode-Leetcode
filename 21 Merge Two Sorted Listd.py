'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        curt = dummy
        temp1, temp2 = l1, l2
        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                curt.next = temp1
                curt = curt.next
                temp1 = temp1.next
            else:
                curt.next = temp2
                curt = curt.next
                temp2 = temp2.next
        if temp1 is None:
            curt.next = temp2
        else:
            curt.next = temp1
        return dummy.next
