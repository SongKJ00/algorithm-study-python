from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
	A, B = map(int, input().split())
	adj[B].append(A)
	
def bfs(curr_idx):
	q = deque()
	visited = [False] * (N+1)
	visited[curr_idx] = True
	q.append(curr_idx)
	count = 1
	while not len(q) == 0:
		next_idx = q.pop()
		for i in adj[next_idx]:
			if not visited[i]:
				visited[i] = True
				q.append(i)
				count += 1
	return count
	
result = []
max_value = -1

for i in range(N+1):
	c = bfs(i)
	if c > max_value:
		result = [i]
		max_value = c
	elif c == max_value:
		result.append(i)
		max_value = c
	
for r in result:
	print(r, end=' ')