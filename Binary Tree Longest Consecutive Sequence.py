'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Have you met this question in a real interview? Yes
Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

'''

class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.longest = 0
        self.helper(root)
        return self.longest
        
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        subtreeLongest = 1
        if root.left and root.left.val-root.val == 1:
            subtreeLongest = max(subtreeLongest, left+1)
        if root.right and root.right.val-root.val == 1:
            subtreeLongest = max(subtreeLongest, right+1)
        if subtreeLongest > self.longest:
            self.longest = subtreeLongest
        return subtreeLongest