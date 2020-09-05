from collections import deque

M, N = map(int, input().split())
m = []
visited = []
for _ in range(N):
  m.append(list(map(int, input().split())))
  visited.append([False]*M)

def bfs(start):
  depth = 0
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  q = deque()
  for s in start:
    q.append(s)
    visited[s[0]][s[1]] = True

  while q:
    y, x, d = q.popleft()
    for dir in range(4):
      next_y = y + dy[dir]
      next_x = x + dx[dir]
      next_d = d + 1
      if 0 <= next_y < N and 0 <= next_x < M:
        if not visited[next_y][next_x] and m[next_y][next_x] == 0:
          depth = next_d
          visited[next_y][next_x] = True
          m[next_y][next_x] = 1
          q.append((next_y, next_x, next_d))

  return depth

def check():
  for y in range(N):
    for x in range(M):
      if m[y][x] == 0:
        return False
  return True

start = []
for y in range(N):
  for x in range(M):
    if m[y][x] == 1:
      start.append((y, x, 0))

answer = bfs(start)
if not check():
  print(-1)
else:
  print(answer)
