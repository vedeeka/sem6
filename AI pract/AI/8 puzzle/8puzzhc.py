goal = (1,2,3,4,5,6,7,8,0)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(state):
    d = 0
    for i, x in enumerate(state):
        if x != 0:
            r, c = divmod(i, 3)
            gr, gc = divmod(goal.index(x), 3)
            d += abs(r-gr) + abs(c-gc)
    return d

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    ans = []

    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            s = list(state)
            nz = nr*3 + nc
            s[z], s[nz] = s[nz], s[z]
            ans.append(tuple(s))

    return ans

def hill_climb(start):
    current = start
    path = [current]

    while current != goal:
        best = current
        best_h = heuristic(current)

        for nxt in neighbors(current):
            h = heuristic(nxt)
            if h < best_h:
                best = nxt
                best_h = h

        if best == current:
            break

        current = best
        path.append(current)

    return path

start = tuple(map(int, input("Enter start state: ").split()))

path = hill_climb(start)

for i, state in enumerate(path):
    print("Step", i)
    for j in range(0, 9, 3):
        print(state[j], state[j+1], state[j+2])
    print()

if path[-1] == goal:
    print("Goal Reached")
else:
    print("Stuck at Local Optimum")