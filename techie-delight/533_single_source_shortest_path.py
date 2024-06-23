'''

Given a weighted directed graph with non-negative edge weights and a source vertex, return the shortest path cost from the source vertex to every other reachable vertex in the graph.

Input: Graph [edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)], n = 5], source = 0
Here, tuple (x, y, w) represents an edge from x to y having weight w.

Output: {(0, 4, 4), (0, 4, 6), (0, 4, 5), (0, 4, 3)}
Here, tuple (s, d, c) indicates that the shortest path from source s to destination d has cost c.

Explanation:

• Shortest path from (0 —> 1) is [0 —> 4 —> 1] with cost 4.
• Shortest path from (0 —> 2) is [0 —> 4 —> 1 —> 2] with cost 6.
• Shortest path from (0 —> 3) is [0 —> 4 —> 3] with cost 5.
• Shortest path from (0 —> 4) is [0 —> 4] with cost 3.

Input: Graph [edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)], n = 5], source = 1
Output: {(1, 2, 2), (1, 3, 6), (1, 4, 4)}
Explanation:

• Shortest path from (1 —> 0) does not exist.
• Shortest path from (1 —> 2) is [1 —> 2] with cost 2.
• Shortest path from (1 —> 3) is [1 —> 4 —> 3] with cost 6.
• Shortest path from (1 —> 4) is [1 —> 4] with cost 4.

Constraints:

• The graph is implemented using an adjacency list.
• The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.
• The source vertex is among the set of vertices in the graph.


Hint: use Dijkstra's algorithm using a min-heap

'''
import heapq
from collections import deque, defaultdict
from typing import Set, List, Tuple

class Graph:
    def __init__(self, edges=None, n=0):

        # Total number of nodes in the graph
        self.n = n

        # List of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

def find_shortest_distances(graph: Graph, source: int):
    distances = {vertex: float('inf') for vertex in range(graph.n)}
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        
        # still works without this condition
        # If we've found a longer path, skip
        # if current_distance > distances[current_vertex]:
        #     continue
        
        # Check all neighboring vertices
        for neighbor, weight in graph.adjList[current_vertex]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    paths = set()
    for k, v in distances.items():
        if v == 0 or v == float('inf'):
            continue
        paths.add((source, k, v))
    return paths

if __name__=="__main__":
    edges = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)]
    n = 5
    source = 0
    ans = find_shortest_distances(graph=Graph(edges=edges, n=n), source=source)
    print(ans)
