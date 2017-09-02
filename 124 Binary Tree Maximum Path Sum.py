'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = None
        def search(root):
            if root is None:
                return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            self.res = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.res)
            return max(leftMax, rightMax, 0) + root.val
        search(root)
        return self.res