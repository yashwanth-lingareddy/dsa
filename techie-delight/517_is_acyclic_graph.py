'''

Given an undirected graph, check if it is a tree or not. In other words, check if a given undirected graph is an Acyclic Connected Graph or not.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], n = 6]
Output: True
Explanation: Graph is connected and has no cycles.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], n = 6]
Output: False
Explanation: Graph contains cycle [0 —> 1 —> 2 —> 3 —> 4 —> 5 —> 0].

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.
• The graph is connected, i.e., every node can be reached starting from all other nodes.

'''
from collections import deque
from typing import Set

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
    visited = set()
    q = deque()
    q.append(start_vertex)

    while len(q) > 0:
        this_vertex = q.popleft()

        if this_vertex in visited:
            return False
        
        visited.add(this_vertex)
        neighbors = graph.adjList[this_vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                q.append(neighbor)
    
    return len(visited) == graph.n

def is_acyclic(graph: Graph):
    for v in range(graph.n):
        if not bfs(v, graph):
            return False
    return True

if __name__=="__main__":
    edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)]
    n = 6
    graph = Graph(n=n, edges=edges)
    ans = is_acyclic(graph=graph)
    print(ans)