'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = []
        cur = head
        while cur != None:
            res.append(cur.val)
            cur = cur.next
        res.sort()
        cur = head
        for i in res:
            cur.val = i
            cur = cur.next
        return head