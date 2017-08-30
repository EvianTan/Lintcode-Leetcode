'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

 Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Have you met this question in a real interview? Yes
Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
return the node 1.
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
    # @return {TreeNode} the root of the minimum subtree
    import sys
    minimum = sys.maxint
    result = None

    def findSubtree(self, root):
        # Write your code here
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        sum = left_sum + right_sum + root.val
        if sum <= self.minimum:
            self.minimum = sum
            self.result = root
        return sum