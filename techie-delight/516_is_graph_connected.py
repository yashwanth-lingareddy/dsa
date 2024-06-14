'''

Given an undirected graph, determine whether it is connected or not. A graph is said to be connected when a path exists between every pair of vertices in the graph.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)], n = 6]
Output: True

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)], n = 9]
Output: False

Input: Graph [edges = [(0, 1), (1, 3), (2, 3), (3, 5)], n = 6]
Output: False

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.

'''

from typing import List
from collections import deque

class Graph:
    def __init__(self, edges=None, n=0):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def bfs(start_vertex: int, graph: Graph):
    q = deque()
    q.append(start_vertex)
    visited = set()
    while len(q) > 0:
        this_vertex = q.popleft()
        if this_vertex not in visited:
            visited.add(this_vertex)
            neighbors = graph.adjList[this_vertex]
            
            for neighbor in neighbors:
                q.append(neighbor)
    return visited

def is_connected(graph: Graph):
    n = graph.n
    for v in range(n):
        visited = bfs(v, graph)
        if len(visited) != n:
            return False
        
    return True

if __name__=="__main__":
    edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]
    n = 9
    graph = Graph(n=n, edges=edges)
    ans = is_connected(graph=graph)
    print(ans)
