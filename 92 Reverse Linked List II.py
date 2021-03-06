'''
everse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        for _ in xrange(m-1):
            node = node.next
        prev = node.next
        curt = prev.next
        for _ in xrange(n-m):
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        node.next.next = curt
        node.next = prev
        return dummy.next