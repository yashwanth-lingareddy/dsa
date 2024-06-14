'''

Given a directed graph, check if it is a DAG (Directed Acyclic Graph) or not. A DAG is a digraph (directed graph) that contains no cycles.

Input: Graph [edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)], n = 7]
Output: False
Explanation: The graph contains a cycle [0 -> 1 -> 3 -> 0].

If we remove edge [3 -> 0] from it, it will become a DAG.

Input: Graph [edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (5, 6), (6, 3)], n = 7]
Output: True

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.

Hint: A directed graph G is acyclic if and only if a depth-first search of G yields no back edges
- For the given graph, find back edges via dfs
- If back edges count is zero then the directed graph is acyclic

'''
from typing import Set, List, Tuple
class Graph:
    def __init__(self, edges=None, n=0):

        # Total number of nodes in the graph
        self.n = n

        # List of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)

def dfs(start_vertex: int, graph: Graph, visited: Set[int], back_edges: List[Tuple[int, int]], on_stack: List[int]):
    if start_vertex in visited:
        return
    visited.add(start_vertex)
    on_stack.append(start_vertex)
    
    neighbors = graph.adjList[start_vertex]
    
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, back_edges, on_stack)
        else:
            if neighbor in on_stack:
                back_edges.append(tuple([start_vertex, neighbor]))
    on_stack.pop()

def is_dag(graph: Graph):
    visited = set()
    back_edges = []
    on_stack = []
    for v in range(graph.n):
        dfs(v, graph, visited, back_edges, on_stack)
    return len(back_edges) == 0

if __name__=="__main__":
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (5, 6), (6, 3)]
    n = 7
    graph = Graph(edges=edges, n=n)
    ans = is_dag(graph=graph)
    print(ans)