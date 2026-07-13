def bellman_ford(graph, vertices, source):
    dist = [float("inf")] * vertices
    dist[source] = 0

    print("\nInitial Routing Table")
    for i in range(vertices):
        print(f"Router {i} --> {dist[i]}")

    for i in range(vertices - 1):
        print(f"\nIteration {i + 1}")
        updated = False

        for u, v, w in graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print(f"Updating Router {v}: {dist[v]} -> {dist[u] + w}")
                dist[v] = dist[u] + w
                updated = True

        print("\nRouting Table")
        for j in range(vertices):
            print(f"Router {j} --> {dist[j]}")

        if not updated:
            print("\nNo further updates.")
            break

    print("\nFinal Routing Table")
    print("Destination\tDistance")
    for i in range(vertices):
        print(i, "\t\t", dist[i])


graph = []
v = int(input("Enter number of routers: "))
e = int(input("Enter number of edges: "))

print("Enter source destination cost:")
for i in range(e):
    u, v1, w = map(int, input().split())
    graph.append((u, v1, w))

source = int(input("Enter source router: "))
bellman_ford(graph, v, source)