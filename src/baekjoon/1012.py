from collections import deque

T = int(input())

def bfs(y, x):
	visited[y][x] = True
	q = deque()
	q.append((y, x))
	dx = [0, 0, -1, 1]
	dy = [-1, 1, 0, 0]
	while not len(q) == 0:
		currY, currX = q.pop()
		for dir in range(4):
			nextY = currY + dy[dir]
			nextX = currX + dx[dir]
			if nextX < 0 or nextX >= M:
				continue
			if nextY < 0 or nextY >= N:
				continue
				
			if userMap[nextY][nextX] == 1 and not visited[nextY][nextX]:
				q.append((nextY, nextX))
				visited[nextY][nextX] = True
	
for _ in range(T):
	M, N, K = map(int, input().split())
	userMap = [[0] * M for _ in range(N)]
	visited = [[False] * M for _ in range(N)]
	for _ in range(K):
		x, y = map(int, input().split())
		userMap[y][x] = 1
		
	result = 0
	for y in range(N):
		for x in range(M):
			if userMap[y][x] == 1 and not visited[y][x]:
				bfs(y, x)
				result += 1
				
	print(result)
