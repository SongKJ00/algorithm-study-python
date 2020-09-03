import heapq
import sys
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
inf = 100000000
adj = [[] for _ in range(V+1)]
for i in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  adj[u].append([v, w])

dist = [inf for _ in range(V+1)]
dist[K] = 0
heap = []
heapq.heappush(heap, [dist[K], K])
while heap:
  d, i = heapq.heappop(heap)
  for v, w in adj[i]:
    d_w = dist[i] + w
    if d_w < dist[v]:
      dist[v] = d_w
      heapq.heappush(heap, [d_w, v])

for d in dist[1:]:
  if d == inf:
    print('INF')
  else:
    print(d)