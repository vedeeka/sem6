from collections import deque

def water_jug(m, n, d):

    if d > max(m, n):
        return -1

    q = deque()
    q.append((0, 0, 0))  

    visited = [[False for _ in range(n+1)] for _ in range(m+1)]
    visited[0][0] = True

    while q:

        jug1, jug2, count = q.popleft()

        if jug1 == d or jug2 == d:
            return count

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
                visited[new_j1][new_j2] = True
                q.append((new_j1, new_j2, count + 1))

    return -1



m = int(input("Enter capacity of Jug 1 (m): "))
n = int(input("Enter capacity of Jug 2 (n): "))
d = int(input("Enter target amount (d): "))

result = water_jug(m, n, d)

if result == -1:
    print("Target cannot be obtained")
else:
    print("Minimum operations required:", result)