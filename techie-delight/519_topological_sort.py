'''

Given a list of edges of a directed acyclic graph (DAG), return its topological order using topological sort algorithm. If the graph has more than one topological ordering, return any of them.

Input: edges = [(0, 1), (0, 2)]
Output: [0, 1, 2] or [0, 2, 1]

Input: edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
Output: [3, 5, 7, 0, 1, 2, 4, 6], or any other valid topological ordering like,

[3, 5, 7, 0, 1, 2, 6, 4]
[3, 5, 7, 0, 1, 4, 2, 6]
[3, 5, 7, 0, 1, 4, 6, 2]
[3, 5, 7, 0, 1, 6, 2, 4]
[3, 5, 7, 0, 1, 6, 4, 2]
[3, 5, 7, 1, 0, 2, 4, 6]
[3, 5, 7, 1, 0, 2, 6, 4]
…

Constraints:

• The maximum number of nodes in the graph is 100.
• There are no cycles in the graph.

'''
from typing import Set, Tuple, List

class Graph:
    def __init__(self, edges=None, n=0):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def build_graph(edges: List[Tuple[int, int]]):
    vertex = set()
    for (src, dest) in edges:
        vertex.add(src)
        vertex.add(dest)
    n = len(vertex)
    return Graph(edges=edges, n=n)

def dfs(start_vertex: int, graph: Graph, visited: Set[int], stack: List[int]):
    if start_vertex in visited:
        return
    
    visited.add(start_vertex)
    neighbors = graph.adjList[start_vertex]
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, stack)
    stack.append(start_vertex)

def topological_sort(edges: List[Tuple[int, int]]):
    graph = build_graph(edges)
    visited = set()
    stack = []
    order = []
    for v in range(graph.n):
        if v not in visited:
            dfs(v, graph, visited, stack)
    
    while stack:
        order.append(stack.pop())

    return order

if __name__=="__main__":
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
    ans = topological_sort(edges)
    print(ans)