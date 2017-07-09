'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head
        while True:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast is None or slow is None:
                    return False
                elif fast == slow:
                    return True
            else:
                return False
        return False