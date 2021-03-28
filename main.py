from collections import deque
import math
n = 0
capacity = list(list())
flow = list(list()) 
height = list() 
excess = list() 
seen = list() 
excess_vertices = deque() 

def push(u, v):
    global flow
    global excess
    global excess_vertices
    d = min(excess[u], capacity[u][v] - flow[u][v])
    flow[u][v] += d
    flow[v][u] -= d
    excess[u] -= d
    excess[v] += d
    if d and excess[v] == d:
        excess_vertices.append(v)

def relabel(u):
    global height
    d = math.inf
    for i in range(n):
        if capacity[u][i] - flow[u][i] > 0:
            d = min(d, height[i])
    if d < math.inf:
        height[u] = d + 1

def discharge(u):
    global seen
    while excess[u] > 0:
        if seen[u] < n:
            v = seen[u]
            if capacity[u][v] - flow[u][v] > 0 and height[u] > height[v]:
                push(u, v)
            else:
                seen[u] += 1
        else:
            relabel(u)
            seen[u] = 0

def max_flow(s, t):
    global height
    global flow
    global excess
    global seen
    height = [0 for i in range(n)]
    height[s] = n
    flow = [[0 for j in range(n)] for i in range(n)]
    excess = [0 for i in range(n)]
    excess[s] = math.inf
    for i in range(n):
        if i != s:
            push(s, i)
    seen = [0] * n
    while len(excess_vertices) != 0:
        u = excess_vertices.popleft()
        if u != s and u != t:
            discharge(u)
    max_flow = 0
    for i in range(n):
        max_flow += flow[i][t]
    return max_flow

if __name__ == "__main__":
    n = 6
    capacity = [[0, 16, 13, 0, 0, 0],
                [0, 0, 10, 12, 0, 0],
                [0, 4, 0, 0, 14, 0],
                [0, 0, 9, 0, 0, 20],
                [0, 0, 0, 7, 0, 4],
                [0, 0, 0, 0, 0, 0]]
    print(max_flow(0, 5))
