from collections import deque


def bfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n

    q = deque()
    q.append(start)
    visited[start] = True

    print("BFS traversal:")
    while q:
        node = q.popleft()
        print(node, end=" ")

        for i in range(n):
            if adj_matrix[node][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)


def dfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n

    stack = [start]

    print("\nDFS traversal:")
    while stack:
        node = stack.pop()

        if not visited[node]:
            print(node, end=" ")
            visited[node] = True

       
            for i in range(n-1, -1, -1):
                if adj_matrix[node][i] == 1 and not visited[i]:
                    stack.append(i)


n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

start = int(input("Enter starting vertex: "))

bfs(adj_matrix, start)
dfs(adj_matrix, start)
