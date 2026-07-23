# Artificial Intelligence Search Algorithms

## 1. Breadth-First Search (BFS)

```text
BreadthFirstSearch(start, goal)

1   open ← Queue()
2   closed ← {}

3   Enqueue(start, open)

4   while open is not empty
5       current ← Dequeue(open)

6       if GoalTest(current)
7           return ReconstructPath(current)

8       Add current to closed

9       for each child in MoveGen(current)
10          if child ∉ open AND child ∉ closed
11              parent(child) ← current
12              Enqueue(child, open)

13  return "No solution found"
```

---

## 2. Depth-First Search (DFS)

```text
DepthFirstSearch(start, goal)

1   open ← Stack()
2   closed ← {}

3   Push(start, open)

4   while open is not empty
5       current ← Pop(open)

6       if GoalTest(current)
7           return ReconstructPath(current)

8       Add current to closed

9       for each child in MoveGen(current)
10          if child ∉ open AND child ∉ closed
11              parent(child) ← current
12              Push(child, open)

13  return "No solution found"
```

---

## 3. Depth-Bounded DFS (Depth-Limited Search)

```text
DepthBoundedDFS(node, goal, depthLimit)

1   if GoalTest(node)
2       return SUCCESS

3   if depthLimit = 0
4       return FAILURE

5   for each child in MoveGen(node)
6       result ← DepthBoundedDFS(child, goal, depthLimit - 1)
7       if result = SUCCESS
8           return SUCCESS

9   return FAILURE
```

---

## 4. Best-First Search

```text
BestFirstSearch(start, goal)

1   open ← PriorityQueue()
2   closed ← {}

3   Insert start into open with priority h(start)

4   while open is not empty
5       current ← Remove node with minimum heuristic value

6       if GoalTest(current)
7           return ReconstructPath(current)

8       Add current to closed

9       for each child in MoveGen(current)
10          if child ∉ open AND child ∉ closed
11              parent(child) ← current
12              Insert child into open with priority h(child)

13  return "No solution found"
```

---

## 5. Hill Climbing

```text
HillClimbing(start, goal)

1   current ← start

2   while TRUE
3       if GoalTest(current)
4           return current

5       neighbors ← MoveGen(current)

6       if neighbors = {}
7           return current

8       best ← neighbor with lowest h-value

9       if h(best) ≥ h(current)
10          return current

11      current ← best
```

---

## 6. A* Search

```text
AStar(start, goal)

1   open ← PriorityQueue()
2   closed ← {}

3   g(start) ← 0
4   f(start) ← g(start) + h(start)
5   Insert start into open

6   while open is not empty
7       current ← Remove node with minimum f-value

8       if current = goal
9           return ReconstructPath(current)

10      Add current to closed

11      for each child in MoveGen(current)
12          if child ∈ closed
13              continue

14          tentative_g ← g(current) + Cost(current, child)

15          if child not in open OR tentative_g < g(child)
16              parent(child) ← current
17              g(child) ← tentative_g
18              f(child) ← g(child) + h(child)

19              if child not in open
20                  Insert child into open

21  return "No solution found"
```

---

## 7. MiniMax Algorithm

```text
MiniMax(node, depth, maximizingPlayer)

1   if GoalTest(node) OR depth = 0
2       return Evaluate(node)

3   if maximizingPlayer
4       bestValue ← -∞
5       for each child in MoveGen(node)
6           value ← MiniMax(child, depth - 1, FALSE)
7           bestValue ← max(bestValue, value)
8       return bestValue

9   else
10      bestValue ← +∞
11      for each child in MoveGen(node)
12          value ← MiniMax(child, depth - 1, TRUE)
13          bestValue ← min(bestValue, value)
14      return bestValue
```

---

## 8. Alpha-Beta Pruning

```text
AlphaBeta(node, depth, α, β, maximizingPlayer)

1   if GoalTest(node) OR depth = 0
2       return Evaluate(node)

3   if maximizingPlayer
4       value ← -∞
5       for each child in MoveGen(node)
6           value ← max(value, AlphaBeta(child, depth-1, α, β, FALSE))
7           α ← max(α, value)
8           if α ≥ β
9               break
10      return value

11  else
12      value ← +∞
13      for each child in MoveGen(node)
14          value ← min(value, AlphaBeta(child, depth-1, α, β, TRUE))
15          β ← min(β, value)
16          if β ≤ α
17              break
18      return value
```