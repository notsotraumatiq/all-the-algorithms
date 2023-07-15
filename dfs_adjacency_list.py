'''
Write a function dfs(graph, start_node) that takes in an adjacency list representation of
a graph and a starting node, and performs a Depth-First Search traversal. The function
should return a list of nodes visited during the traversal.
'''


def dfs(graph, start_node, visited=None) -> list:
    if visited is None:
        visited = []

    visited.append(start_node)
    for nodes in graph[start_node]:
        if nodes not in visited:
            dfs(graph, nodes, visited)
    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
result = dfs(graph, start_node)
print(result)
