'''
Given a sorted (increasing order) array, Convert it to create a binary tree with minimal height.

 Notice

There may exist multiple valid solutions, return any of them.

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4,5,6,7], return

     4
   /   \
  2     6
 / \    / \
1   3  5   7
'''
class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        return self.convert(A, 0, len(A) - 1)
        
    def convert(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        
        mid = (start + end) / 2
        root = TreeNode(A[mid])
        root.left = self.convert(A, start, mid - 1)
        root.right = self.convert(A, mid + 1, end)
        return root