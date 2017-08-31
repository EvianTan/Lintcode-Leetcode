'''
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

 Notice

You can assume there is no duplicate values in this tree + node.

Have you met this question in a real interview? Yes
Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node
        curt = root
        while curt != node:
            if node.val < curt.val:
                if curt.left is None:
                    curt.left = node
                curt = curt.left
            else:
                if curt.right is None:
                    curt.right = node
                curt = curt.right
        return root
                