'''
Given a binary tree, return all root-to-leaf paths.

Have you met this question in a real interview? Yes
Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        ans = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        ans += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        return ans     