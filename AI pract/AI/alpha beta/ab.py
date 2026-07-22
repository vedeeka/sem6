import math

def alphabeta(node, alpha, beta, depth):
    if node not in tree:
        return value[node]

    if depth % 2 == 0:     
        best = -math.inf
        for child in tree[node]:
            best = max(best, alphabeta(child, alpha, beta, depth + 1))
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    else:                
        best = math.inf
        for child in tree[node]:
            best = min(best, alphabeta(child, alpha, beta, depth + 1))
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best


tree = {}
value = {}

n = int(input("Enter number of parent nodes: "))

for i in range(n):
    parent = input("Parent: ")
    children = input("Children: ").split()
    tree[parent] = children

m = int(input("Enter number of leaf nodes: "))

for i in range(m):
    leaf = input("Leaf: ")
    val = int(input("Value: "))
    value[leaf] = val

root = input("Enter root: ")

ans = alphabeta(root, -math.inf, math.inf, 0)

print("Answer =", ans)

# root L, R
# L LL, LR
# R RL, RR
# LL LLL, LLR
# LR LRL, LRR
# RL RLL, RLR
# RR RRL, RRR
# LLL a, b
# LLR c, d
# LRL e, f
# LRR g, h
# RLL i, j
# RLR k, l
# RRL m, n
# RRR o, p
# a 10
# b 5
# c 7
# d 11
# e 12
# f 8
# g 9
# h 8
# i 5
# j 12
# k 11
# l 12
# m 9
# n 8
# o 7
# p 10
# done






# import math
# root = 'A'

# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G']
# }

# value = {
#     'D': 3,
#     'E': 5,
#     'F': 2,
#     'G': 9
# }


# def alphabeta(node, alpha, beta, depth):
#     if node not in tree:
#         return value[node],[node]

#     if depth%2==0:
#         best_path = []
#         best=-math.inf

#         for n in tree[node]:
#             val, path = alphabeta(n, alpha, beta, depth + 1)

#             if val > best:
#                 best = val
#                 best_path = [node] + path

#             alpha=max(alpha,best)
#             if alpha>=beta:
#                 break

#         return best,best_path


#     else:
#         best=math.inf
#         best_path = []
#         for n in tree[node]:

#             val, path = alphabeta(n, alpha, beta, depth + 1)

#             if val < best:
#                 best = val
#                 best_path = [node] + path

#             beta=min(beta,best)

#             if alpha>=beta:
#                 break

#         return best,best_path




# ans, path = alphabeta(root, -math.inf, math.inf, 0)

# print("Answer =", ans)
# print("Path =", " -> ".join(path))