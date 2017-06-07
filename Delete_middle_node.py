'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
Given 1->2->3->4, and node 3. return 1->2->4
'''
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        if node is None or node.next is None:
            return
        next = node.next;
        node.val = next.val
        node.next = next.next
        return