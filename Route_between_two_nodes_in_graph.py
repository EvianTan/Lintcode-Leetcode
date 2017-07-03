'''
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Have you met this question in a real interview? Yes
Example
Given graph:

A----->B----->C
 \     |
  \    |
   \   |
    \  v
     ->D----->E
for s = B and t = E, return true

for s = D and t = C, return false

'''
class Solution:
    def hasRoute(self, graph, s, t):
        visited = set()
        return self.dfs(s, t, visited)

    def dfs(self, s, t, visited):
        """pre-check"""
        if s == t:
            return True

        visited.add(s)
        for nbr in s.neighbors:
            if nbr not in visited:
                if self.dfs(nbr, t, visited):
                    return True

        return False