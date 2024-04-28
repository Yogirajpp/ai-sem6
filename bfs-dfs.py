def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbour in graph.get(node, []):
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def bfs(graph, node):
    visited = set()
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            queue.extend(neighbour for neighbour in graph.get(current, []) if neighbour not in visited)

def main():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        graph[i] = [int(input("Enter edge {} for node {}: ".format(j, i))) for j in range(1, edges + 1)]
    
    print("DFS:")
    dfs(graph, 1)
    print("\nBFS:")
    bfs(graph, 1)

if __name__ == "__main__":
    main()
