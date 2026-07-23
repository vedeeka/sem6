from heapq import heappush,heappop


def valid(m,c,tm,tc):
    if m<0 or c<0 or c>tc or m>tm:
        return False
    elif m>0 and m<c:
        return False
    nm=tm-m
    nc=tc-c
    if nm>0 and nm<nc:
        return False
    return True
from collections import deque
def bfs(tm,tc,b):
    goal=(0,0,0)
    start=(tm,tc,1)

    steps=[]
    for i in range(b+1):
        for j in range(b+1):
            if 0<(i+j)<=b:
                steps.append((i,j))


    q = deque([(start, [start])])

    while q:
        (m,c,b),path=q.popleft()

        if (m,c,b)==goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for i,j in steps:
            if b==0:
                nm=m+i
                mc=c+j
                nb=1
                
            else:
                nm=m-i
                mc=c-j
                nb=0
            if valid(nm,mc,tm,tc) and (nm,mc,nb) not in path:
                new_state=(nm,mc,nb)
                q.append((new_state,path+[new_state]))
    print("No Solution")
            
m = int(input("Enter Missionaries: "))
c = int(input("Enter Cannibals: "))
boat = int(input("Enter Boat Capacity: "))

bfs(m, c, boat)


