from collections import deque

def dfs(graph, start):
    visited = set()   
    result = []
    stack = deque([start])
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))
    
    return result

if __name__ == "__main__":
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        node = input("Enter node name: ")
        neighbours = input(f"Enter neighbors of {node}: ").split()
        graph[node] = neighbours
    
    start_node = input("Enter the starting node: ")
    
    print("DFS traversal:", dfs(graph, start_node))











#     graph = {}

# n = int(input("Enter the number of nodes: "))

# for i in range(n):

#     graph[i] = list(map(int, input(f"Enter neighbours of node {i}: ").split()))

# from collections import deque

# q=deque()
# q.append(0)
# v = set()
# v.add(0)
# while q:
#     k=q.pop()
    
#     print(k)
#     for i in reversed(graph[k]):
#         if i not in v:
#             v.add(i)
#             q.append(i)


