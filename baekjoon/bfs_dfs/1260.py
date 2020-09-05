import heapq
import copy
from collections import deque

def dfs(curr_node, visited, adj):
  visited[curr_node] = True
  print(curr_node, end=' ')

  v_adjs = adj[curr_node]
  for v_adj in v_adjs:
    if not visited[v_adj]:
      dfs(v_adj, visited, adj)

def bfs(visited, adj):
  q = deque()
  q.append(V)
  visited[V] = True
  print(V, end=' ')

  while q:
    v = q.popleft()
    v_adjs = adj[v]
    for v_adj in v_adjs:
      if not visited[v_adj]:
        visited[v_adj] = True
        print(v_adj, end=' ')
        q.append(v_adj)

  print()

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M):
  v1, v2 = map(int, input().split())
  adj[v1].append(v2)
  adj[v2].append(v1)
  adj[v1].sort()
  adj[v2].sort()

temp_adj = copy.deepcopy(adj)
temp_visited = copy.deepcopy(visited)
dfs(V, temp_visited, temp_adj)
print()
temp_adj = copy.deepcopy(adj)
temp_visited = copy.deepcopy(visited)
bfs(temp_visited, temp_adj)