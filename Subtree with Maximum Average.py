'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    import sys
    average = 1-sys.maxint
    result = None

    def findSubtree2(self, root):
        # Write your code here
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0, 0
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        sum = left_sum + right_sum + root.val
        size = left_size + right_size + 1
        if self.result is None or sum*1.0/size > self.average:
            self.result = root
            self.average = sum*1.0/size
        return sum, size