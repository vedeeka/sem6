def bellman_ford(graph, vertices, source):
    dist = [999] * vertices
    parent = [-1] * vertices
    dist[source] = 0

    for i in range(vertices - 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    print("\nRouting Table")
    print("Destination\tDistance\tPath")

    for i in range(vertices):
        path = []
        curr = i

        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        path.reverse()
        print(f"{i}\t\t{dist[i]}\t\t{' -> '.join(map(str, path))}")


# Input number of vertices and edges
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

graph = []

print("Enter each edge as: source destination weight")
for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

source = int(input("Enter source vertex: "))

bellman_ford(graph, V, source)