'''

Given an undirected graph, determine whether it is bipartite or not. A bipartite graph (or bigraph) is a graph whose vertices can be divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V.

Input: Graph [edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)], n = 9]
Output: True
Explanation: The graph is a bipartite as it can be divided it into two sets, U (0, 2, 4, 5, 7) and V (1, 3, 6, 8), with every edge having one endpoint in set U and the other in set V.

If we add edge 1 —> 3, the graph becomes non-bipartite.

Input: Graph [edges = [(0, 1), (1, 2), (1, 3), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)], n = 9]
Output: False

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.
• The graph is connected, i.e., every node can be reached starting from all other nodes.

Hint: A graph is bipartite if the graph can be colored with two colors in such a way that no two adjacent vertex has the same color

'''

from typing import List

class Graph:
    def __init__(self, edges=None, n=0):
        self.n = n
        self.edges = edges

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def dfs(v: int, c: int, color: List[int], adjList: List[List[int]]):
    # if the vertex is already colored and is not the same color as c
    if color[v] != -1 and color[v] != c:
        return False
    
    # color the vertex with c
    color[v] = c

    # for each neighbor check if they are not of same color
    for neighbor in adjList[v]:
        if (color[neighbor] == c)  or (color[neighbor] == -1 and not dfs(neighbor, 1 - c, color, adjList)):
            return False
    return True

def is_bipartite(graph: Graph):
    color = [-1] * graph.n

    for v in range(graph.n):
        if color[v] == -1 and not dfs(v, 0, color, graph.adjList):
            return False
    
    return True

if __name__=="__main__":
    edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]
    n = 9
    graph = Graph(edges=edges, n=n)
    ans = is_bipartite(graph)
    print(ans)
