def bellman_ford(graph, vertices, source):
    distance = [float('inf')] * (vertices + 1)
    distance[source] = 0
    print("\nInitial Routing Table\n------------------------------------------------")
    for i in range(1, vertices + 1):
        print(f"Router {i} --> {distance[i]}")
    for iteration in range(vertices - 1):
        print(f"\nIteration {iteration + 1}\n------------------------------------------------")
        updated = False
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                old_distance = distance[v]
                distance[v] = distance[u] + w
                updated = True
                print(f"Updating Router {v}")
                print(f"Path: Router {u} --> Router {v}")
                print(f"Edge Cost = {w}")
                print(f"Old Distance = {old_distance}")
                print(f"New Distance = {distance[v]}")
                print()
        print("Routing Table After Iteration\n------------------------------------------------")
        for i in range(1, vertices + 1):
            print(f"Router {i} --> {distance[i]}")
        if not updated:
            print("\nNo further updates possible.")
            print("Shortest paths already found.")
            break
    print("\nFinal Routing Table\n------------------------------------------------\nDestination Router\tMinimum Distance")
    for i in range(1, vertices + 1):
        print(f"{i}\t\t\t{distance[i]}")

graph = []
vertices = int(input("Enter number of routers(vertices): "))
edges = int(input("Enter number of edges: "))
print("\nEnter source destination cost:")
for i in range(edges):
    u, v, w = map(int, input(f"Edge {i+1}: ").split())
    graph.append((u, v, w))
source = int(input("\nEnter source router: "))
bellman_ford(graph, vertices, source)
