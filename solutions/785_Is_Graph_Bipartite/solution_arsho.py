"""
Title     : 785. Is Graph Bipartite?
Category  : Graph
URL       : https://leetcode.com/problems/is-graph-bipartite/
Author    : arsho
Created   : 08 March 2020
"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = []
        nodes_length = len(graph)
        colors = [0 for _ in range(nodes_length)]
        queue.append(0)
        while queue:
            current_node = queue.pop(0)
            if colors[current_node] == 0:
                colors[current_node] = 1
            for connected_node in graph[current_node]:
                if colors[connected_node] == 0:
                    queue.append(connected_node)
                    if colors[current_node] == 1:
                        colors[connected_node] = 2
                    elif colors[current_node] == 2:
                        colors[connected_node] = 1
                elif colors[connected_node] == colors[current_node]:
                    return False
            if len(queue) == 0:
                for i in range(nodes_length):
                    if colors[i] == 0:
                        queue.append(i)
        return True
