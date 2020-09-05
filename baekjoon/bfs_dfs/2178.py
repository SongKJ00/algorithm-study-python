from collections import deque

N, M = map(int, input().split())
m = []
dist = []
visited = [[False for i in range(M)] for j in range(N)]
for i in range(N):
  m.append(list(map(int, list(input()))))
  dist.append([0 for _ in range(M)])

depth = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque()
q.append((0, 0, depth))
visited[0][0] = True
while q:
  y, x, d = q.popleft()
  for dir in range(4):
    next_y = y + dy[dir]
    next_x = x + dx[dir]
    next_d = d + 1
    if 0 <= next_y < N and 0 <= next_x < M:
      if not visited[next_y][next_x] and m[next_y][next_x] == 1:
        dist[next_y][next_x] = next_d
        visited[next_y][next_x] = True
        q.append((next_y, next_x, next_d))


print(dist[N-1][M-1])