'''
Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.

 Notice

You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.
Example
Given 1->2->3->4->null and v1 = 2, v2 = 4.

Return 1->4->3->2->null.
'''

class Solution:
    """
    @param: head: a ListNode
    @param: v1: An integer
    @param: v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curt = dummy
        p1 = None
        p2 = None
        while curt.next:
            if curt.next.val == v1 or curt.next.val == v2:
                if not p1:
                    p1 = curt.next
                    prev = curt
                else:
                    temp = curt.next.next
                    p2 = curt.next
                    prev.next = p2
                    if curt == p1:
                        p2.next = p1
                        p1.next = temp
                    else:
                        p2.next = p1.next
                        curt.next = p1
                        p1.next = temp
                    return dummy.next
            curt = curt.next
        return dummy.next