'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        q = [root]
        layer = 0
        while q:
            new_q = []
            layer += 1
            if layer%2 == 1:
                res.append([n.val for n in q])
            else:
                res.append([n.val for n in q][::-1])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)  
            q = new_q
        return res