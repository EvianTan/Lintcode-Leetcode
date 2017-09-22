'''
Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln

reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

Have you met this question in a real interview? Yes
Example
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.

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
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None or head.next.next is None: 
            return head

        slow = fast = head                              
        while fast and fast.next:                       
            slow = slow.next                            
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        dummy = ListNode(0)
        dummy.next = head2             
        prev =  None
        curt = head2
        while curt:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        head2 = prev

        p1 = head1
        p2 = head2
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2