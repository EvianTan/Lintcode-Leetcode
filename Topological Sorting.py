'''
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
'''

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        result, indegree = [], {}
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in indegree:
                    indegree[neighbor] += 1
                else:
                    indegree[neighbor] = 1
        queue = []
        for node in graph:
            if node not in indegree:
                queue.append(node)
                result.append(node)
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
        return result