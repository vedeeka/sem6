import heapq

def dijkstra(graph, start):
    dist = {}
    for node in graph:
        dist[node] = float("inf")
    dist[start] = 0

    pq = [(0, start)]
    visited = set()

    print("\nInitial Routing Table")
    for node in graph:
        print(f"Router {node} --> {dist[node]}")

    while pq:
        d, node = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        for neigh, cost in graph[node]:
            if d + cost < dist[neigh]:
                dist[neigh] = d + cost
                heapq.heappush(pq, (dist[neigh], neigh))

    print("\nFinal Routing Table")
    print("Destination\tDistance")
    for node in graph:
        print(f"{node}\t\t{dist[node]}")


# Main Program
vertices = int(input("Enter number of routers: "))
edges = int(input("Enter number of links: "))

graph = {}
for i in range(vertices):
    graph[i] = []

print("\nEnter source destination cost:")
for i in range(edges):
    u, v, w = map(int, input(f"Link {i+1}: ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))      # Remove this line if the graph is directed

start = int(input("\nEnter source router: "))

dijkstra(graph, start)