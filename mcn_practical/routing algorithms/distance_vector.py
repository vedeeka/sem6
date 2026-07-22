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


graph = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 5),
    (2, 3, 8),
    (2, 4, 10),
    (3, 4, 2)
]

V = 5
source = 0

bellman_ford(graph, V, source)