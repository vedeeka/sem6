import heapq

goal = (1,2,3,4,5,6,7,8,0)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(state):
    d = 0
    for i, x in enumerate(state):
        if x != 0:
            r, c = divmod(i,3)
            gr, gc = divmod(goal.index(x),3)
            d += abs(r-gr) + abs(c-gc)
    return d

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z,3)
    ans = []

    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0<=nr<3 and 0<=nc<3:
            s = list(state)
            nz = nr*3+nc
            s[z], s[nz] = s[nz], s[z]
            ans.append(tuple(s))

    return ans

def best_first(start):
    pq = [(heuristic(start), start)]
    visited = set()
    parent = {start: None}

    while pq:
        h, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if current in visited:
            continue

        visited.add(current)

        for nxt in neighbors(current):
            if nxt not in visited:
                if nxt not in parent:
                    parent[nxt] = current
                heapq.heappush(pq, (heuristic(nxt), nxt))

    return None

start = tuple(map(int, input("Enter start state: ").split()))

path = best_first(start)

if path:
    for i, state in enumerate(path):
        print("Step", i)
        for j in range(0,9,3):
            print(state[j], state[j+1], state[j+2])
        print()
else:
    print("No Solution")