'''
Write a function bfs(graph, start_node) that takes in an adjacency list representation
of a graph and a starting node, and performs a Breadth-First Search traversal. The
function should return a list of nodes visited during the traversal.
'''
def bfs(graph, start_node, visited=None) -> list:
    if visited is None:
        visited = []
    queue = [start_node]

    visited.append(start_node)
    while len(queue) > 0:
        node = queue.pop(0)
        for nodes in graph[node]:
            if nodes not in visited:
                visited.append(nodes)
            queue.append(nodes)



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
result = bfs(graph, start_node)
print(result)
