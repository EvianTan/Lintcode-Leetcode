'''
You have two every large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

 Notice

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

Have you met this question in a real interview? Yes
Example
T2 is a subtree of T1 in the following case:

       1                3
      / \              / 
T1 = 2   3      T2 =  4
        /
       4
T2 isn't a subtree of T1 in the following case:

       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4
'''

class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        rt = []
        self.get(T1, rt)
        t1 = ','.join(rt)

        rt = []
        self.get(T2, rt)
        t2 = ','.join(rt)
        return t1.find(t2) != -1
        
    def get(self, root, rt):
        if root is None:
            rt.append("#")
            return

        rt.append(str(root.val))
        self.get(root.left, rt)
        self.get(root.right, rt)
        