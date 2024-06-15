'''

Given a directed graph, return its root vertex. A root vertex of a directed graph is a vertex u with a directed path from u to v for every pair of vertices (u, v) in the graph. In other words, all other vertices in the graph can be reached from the root vertex.

A graph can have multiple root vertices. For example, each vertex in a strongly connected component is a root vertex. In such cases, the solution should return anyone of them. If the graph has no root vertices, the solution should return -1.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)], n = 6]
Output: 4
Explanation: The root vertex is 4 since it has a path to every other vertex in the graph.

Input: Graph [edges = [(0, 1), (0, 5), (1, 2), (2, 3), (4, 5)], n = 6]
Output: -1
Explanation: The root vertex doesn't exist in the graph.

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.

'''
from typing import Set

class Graph:
    def __init__(self, edges=None, n=0):

        # Total number of nodes in the graph
        self.n = n

        # List of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)

def dfs(start_vertex: int, visited: Set[int], graph: Graph):
    if start_vertex in visited:
        return
    visited.add(start_vertex)
    
    neighbors = graph.adjList[start_vertex]
    
    for n in neighbors:
        if n not in visited:
            dfs(n, visited, graph)

def find_root_vertex(graph: Graph) -> int:
    # Write your code here...
    for n in range(graph.n):
        visited = set()
        dfs(n, visited, graph)
        if len(visited) == graph.n:
            return n
    return -1

if __name__=="__main__":
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]
    n = 6
    graph = Graph(edges=edges, n=n)
    ans = find_root_vertex(graph)
    print(ans)