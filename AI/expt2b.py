def dfs(jug1, jug2, m, n, d, visited, count, ans):

    if jug1 == d or jug2 == d:
        ans[0] = min(ans[0], count)
        return

    visited[jug1][jug2] = True

    states = []


    states.append((m, jug2))


    states.append((jug1, n))

    states.append((0, jug2))

    
    states.append((jug1, 0))


    pour = min(jug1, n - jug2)
    states.append((jug1 - pour, jug2 + pour))

    
    pour = min(jug2, m - jug1)
    states.append((jug1 + pour, jug2 - pour))

    for new_j1, new_j2 in states:
        if not visited[new_j1][new_j2]:
            dfs(new_j1, new_j2, m, n, d, visited, count + 1, ans)


def water_jug_dfs(m, n, d):

    if d > max(m, n):
        return -1

    visited = [[False for _ in range(n+1)] for _ in range(m+1)]

    ans = [float('inf')]

    dfs(0, 0, m, n, d, visited, 0, ans)

    if ans[0] == float('inf'):
        return -1
    return ans[0]



m = int(input("Enter capacity of Jug 1 (m): "))
n = int(input("Enter capacity of Jug 2 (n): "))
d = int(input("Enter target amount (d): "))

result = water_jug_dfs(m, n, d)

if result == -1:
    print("Target cannot be obtained")
else:
    print("Minimum operations required:", result)