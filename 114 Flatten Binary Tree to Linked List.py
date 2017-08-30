# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        last = TreeNode(0)
        stack = [root]
        while stack:
            node = stack.pop()
            last.right = node
            last.left = None
            if node and node.right:
                stack.append(node.right)
            if node and node.left:
                stack.append(node.left)
            last = node