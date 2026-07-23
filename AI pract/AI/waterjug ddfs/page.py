from math import gcd

def dldfs(cap1, cap2, target, limit):
    start = (0, 0)
    stack = [(start, [start], 0)]

    while stack:
        (j1, j2), path, depth = stack.pop()

        if j1 == target or j2 == target:
            print("Solution:")
            for s in path:
                print(s)
            return

        if depth >= limit:
            continue

        steps = [
            (cap1, j2),                                       # Fill Jug1
            (j1, cap2),                                       # Fill Jug2
            (0, j2),                                          # Empty Jug1
            (j1, 0),                                          # Empty Jug2
            (max(0, j1-(cap2-j2)), min(cap2, j1+j2)),         # Jug1 -> Jug2
            (min(cap1, j1+j2), max(0, j2-(cap1-j1)))          # Jug2 -> Jug1
        ]

        for state in reversed(steps):
            if state not in path:
                stack.append((state, path + [state], depth + 1))

    print("No Solution Within Depth Limit")


cap1 = int(input("Enter capacity of Jug 1: "))
cap2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))
limit = int(input("Enter depth limit: "))

if target > max(cap1, cap2) or target % gcd(cap1, cap2) != 0:
    print("No Solution")
else:
    dldfs(cap1, cap2, target, limit)

















from collections import deque

def ddfs(jug1_c,jug2_c,t,depth):
    v=set()
    q=deque()
    q.append((0,0,0))
    parent={(0,0):None}
    v.add((0,0))
    allp=[]
    while q:
        j1,j2,d=q.pop()
        
        if j1==t or j2==t:
            path=[]
            curr=(j1,j2)
            while curr!=None:
                path.append(curr)
                curr=parent[curr]
            allp.append(path)
            continue


        if d>=depth:
            continue

        state=(j1,j2)


        rules=[
            (0,j2),
            (j1,0),
            (jug1_c,j2),
            (j1,jug2_c),
            (max(0,j1-(jug2_c-j2)),min(jug2_c,j1+j2)),
            (min(jug1_c,j1+j2),max(0,j2-(jug1_c-j1)))
        ]

        for nxt in rules:
            if nxt not in v:
                v.add(nxt)
                nj1, nj2 = nxt
                q.append((nj1, nj2, d+1))
                parent[nxt]=state

    return allp


if __name__ == "__main__":
    jug1_cap = int(input("Enter capacity of Jug 1: "))
    jug2_cap = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount: "))
    limit=int(input("enter limit"))

    results = ddfs(jug1_cap, jug2_cap, target,limit)
    print(results)
